import os
from typing import Optional, List, Dict, Any
from openai import OpenAI
import json

class LLMTranslator:
    """Translates technical errors into kid-friendly messages using LLM."""

    def __init__(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if not api_key:
            raise ValueError("OPENAI_API_KEY environment variable is required")
        self.client = OpenAI(api_key=api_key)

    def translate_syntax_error(
        self, code: str, error: str, concept: str
    ) -> Dict[str, Any]:
        """
        Translate Python syntax errors into kid-friendly messages.
        
        Args:
            code: The Python code that caused the error
            error: The original error message
            concept: The programming concept being taught
            
        Returns:
            Dictionary containing kid-friendly error message and hints
        """
        prompt = f"""You are a friendly Python teacher helping young students learn programming.
The student is learning about {concept} in Python.

Here is their code:
{code}

They received this error message:
{error}

Please provide a kid-friendly explanation of what went wrong and how to fix it.
Include specific line numbers and references to their code when relevant.

Provide feedback in the following JSON format:
{{
  "message": "kid-friendly explanation of the error",
  "hints": ["specific suggestion 1", "specific suggestion 2"],
  "errorLine": line_number,
  "errorColumn": column_number
}}"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",  # Using GPT-4 for better understanding of code
                messages=[
                    {"role": "system", "content": "You are a friendly Python teacher helping young students."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            
            # Parse the JSON response
            result = json.loads(response.choices[0].message.content)
            return result

        except Exception as e:
            # Fallback to a simple error message if LLM fails
            return {
                "message": f"Oops! There seems to be a small problem with your code: {error}",
                "hints": [
                    "Check if you've typed everything correctly",
                    "Make sure all parentheses and quotes are properly closed"
                ],
                "errorLine": None,
                "errorColumn": None
            }

    def validate_code(
        self, code: str, exercise_description: str, expected_outcome: str
    ) -> Dict[str, Any]:
        """
        Validate code correctness using LLM.
        
        Args:
            code: The Python code to validate
            exercise_description: Description of the exercise
            expected_outcome: Expected result or behavior
            
        Returns:
            Dictionary containing validation results and feedback
        """
        prompt = f"""You are a Python teacher evaluating student code.
Exercise: {exercise_description}
Expected outcome: {expected_outcome}

Student code:
{code}

Provide feedback in the following JSON format:
{{
  "success": boolean,
  "message": "kid-friendly feedback message",
  "hints": ["hint1", "hint2"]
}}"""

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a friendly Python teacher helping young students."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7,
                max_tokens=300
            )
            
            # Parse the JSON response
            result = json.loads(response.choices[0].message.content)
            return result

        except Exception as e:
            # Fallback to a simple response if LLM fails
            return {
                "success": False,
                "message": "I couldn't check your code properly. Let's try again!",
                "hints": ["Try running your code to see if it works as expected"]
            }