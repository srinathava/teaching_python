from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional, Dict
from datetime import datetime
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from ..validator.ast_validator import ASTValidator, ValidationResult
from ..validator.security import SecurityChecker, SecurityViolation
from ..validator.limits import ResourceLimiter, ResourceError
from ..validator.llm import LLMTranslator
from ..database import get_db
from ..models import Progress, User
from sqlalchemy.orm import Session
from sqlalchemy import select

app = FastAPI(title="Code Validator API")

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Configure this properly for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize validators
ast_validator = ASTValidator()
security_checker = SecurityChecker()
resource_limiter = ResourceLimiter()

# Initialize LLM translator if API key is available
llm_translator = None
try:
    llm_translator = LLMTranslator()
except ValueError as e:
    print("Warning: LLM translation disabled -", str(e))

class CodeValidationRequest(BaseModel):
    """Request model for code validation."""
    code: str = Field(..., max_length=1000)
    exercise_id: str
    concept: str = Field(..., description="The programming concept being taught")
    exercise_description: Optional[str] = None
    expected_outcome: Optional[str] = None

class ValidationResponse(BaseModel):
    """Response model for code validation results."""
    success: bool
    message: str
    hints: Optional[List[str]] = None
    error_line: Optional[int] = None
    error_column: Optional[int] = None

class ProgressRequest(BaseModel):
    """Request model for updating progress."""
    exercise_slug: str
    code: str
    is_correct: bool
    user_id: int = 1  # Temporary until auth is implemented

class ProgressResponse(BaseModel):
    """Response model for progress updates."""
    success: bool
    message: Optional[str] = None

class ProgressRecord(BaseModel):
    """Model for progress record in responses."""
    exercise_slug: str
    completed: bool
    completed_at: Optional[datetime]
    attempts: int
    last_attempted_code: Optional[str]

class UserProgressResponse(BaseModel):
    """Response model for user progress fetch."""
    progress: List[ProgressRecord]

@app.post("/api/validate", response_model=ValidationResponse)
async def validate_code(request: CodeValidationRequest) -> ValidationResponse:
    """
    Validate Python code for syntax, security, and resource usage.
    """
    try:
        # Check for security violations
        security_violations = security_checker.check_code(request.code)
        if security_violations:
            violation = security_violations[0]  # Report first violation
            return ValidationResponse(
                success=False,
                message="I noticed something that might not be safe in your code.",
                hints=[violation.message],
                error_line=violation.line
            )
        
        # Check code size limits first
        resource_limiter.check_code_size(request.code)

        # Perform syntax validation
        syntax_result = ast_validator.validate_syntax(request.code)
        if not syntax_result.success:
            # Convert syntax error to kid-friendly message
            if llm_translator:
                friendly_error = llm_translator.translate_syntax_error(
                    request.code,
                    str(syntax_result.message),
                    request.concept
                )
                return ValidationResponse(
                    success=False,
                    message=friendly_error["message"],
                    hints=friendly_error["hints"],
                    error_line=friendly_error.get("errorLine", syntax_result.error_line),
                    error_column=friendly_error.get("errorColumn", syntax_result.error_column)
                )
            else:
                return ValidationResponse(
                    success=False,
                    message=f"Oops! There's a small problem: {syntax_result.message}",
                    hints=["Check if you've typed everything correctly"],
                    error_line=syntax_result.error_line,
                    error_column=syntax_result.error_column
                )

        # If exercise details are provided, use LLM for semantic validation
        if request.exercise_description and request.expected_outcome and llm_translator:
            llm_result = llm_translator.validate_code(
                request.code,
                request.exercise_description,
                request.expected_outcome
            )
            return ValidationResponse(
                success=llm_result["success"],
                message=llm_result["message"],
                hints=llm_result.get("hints")
            )

        # If all checks pass, return success
        return ValidationResponse(
            success=True,
            message="Great job! Your code looks good!",
            hints=["Try running your code to see what it does!",
                  "Can you think of ways to make your code even better?"]
        )

    except ResourceError as e:
        return ValidationResponse(
            success=False,
            message=f"Your code is a bit too big: {str(e)}",
            hints=["Try breaking your code into smaller parts",
                  "Remove any extra code you don't need"]
        )
    
    except Exception as e:
        print(f"Unexpected error in code validation: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while checking your code. Please try again!"
        )

@app.post("/api/progress", response_model=ProgressResponse)
async def update_progress(request: ProgressRequest, db: Session = Depends(get_db)) -> ProgressResponse:
    """
    Update user progress for an exercise.
    """
    try:
        # Get or create user (temporary until auth is implemented)
        user = db.query(User).filter(User.id == request.user_id).first()
        if not user:
            user = User(id=request.user_id)
            db.add(user)
            db.flush()

        # Get existing progress or create new
        progress = db.query(Progress).filter(
            Progress.user_id == request.user_id,
            Progress.exercise_slug == request.exercise_slug
        ).first()

        if progress:
            # Update existing progress
            progress.attempts += 1
            progress.last_attempted_code = request.code
            if request.is_correct and not progress.completed:
                progress.completed = True
                progress.completed_at = datetime.utcnow()
        else:
            # Create new progress
            progress = Progress(
                user_id=request.user_id,
                exercise_slug=request.exercise_slug,
                completed=request.is_correct,
                completed_at=datetime.utcnow() if request.is_correct else None,
                attempts=1,
                last_attempted_code=request.code
            )
            db.add(progress)

        db.commit()
        return ProgressResponse(
            success=True,
            message="Progress updated successfully"
        )

    except Exception as e:
        print(f"Error updating progress: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to update progress"
        )

@app.get("/api/progress/{user_id}", response_model=UserProgressResponse)
async def get_user_progress(user_id: int, db: Session = Depends(get_db)) -> UserProgressResponse:
    """
    Get all progress records for a user.
    """
    try:
        # Get or create user (temporary until auth is implemented)
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            user = User(id=user_id)
            db.add(user)
            db.commit()

        # Get progress records
        progress_records = db.query(Progress).filter(
            Progress.user_id == user_id
        ).all()

        return UserProgressResponse(
            progress=[
                ProgressRecord(
                    exercise_slug=p.exercise_slug,
                    completed=p.completed,
                    completed_at=p.completed_at,
                    attempts=p.attempts,
                    last_attempted_code=p.last_attempted_code
                ) for p in progress_records
            ]
        )

    except Exception as e:
        print(f"Error fetching progress: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Failed to fetch progress"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)