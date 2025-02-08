from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field
from typing import List, Optional
import json
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

from ..validator.ast_validator import ASTValidator, ValidationResult
from ..validator.security import SecurityChecker, SecurityViolation
from ..validator.limits import ResourceLimiter, ResourceError
from ..validator.llm import LLMTranslator

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

@app.post("/api/validate", response_model=ValidationResponse)
async def validate_code(request: CodeValidationRequest) -> ValidationResponse:
    """
    Validate Python code for syntax, security, and resource usage.
    
    Args:
        request: CodeValidationRequest containing the code to validate
        
    Returns:
        ValidationResponse with validation results and any error details
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
        # Log the error for debugging (implement proper logging later)
        print(f"Unexpected error in code validation: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="Something went wrong while checking your code. Please try again!"
        )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)