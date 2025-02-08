import ast
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ValidationResult:
    """Result of code validation containing success status and error details."""
    success: bool
    message: str
    hints: Optional[List[str]] = None
    error_line: Optional[int] = None
    error_column: Optional[int] = None

class ASTValidator:
    """Validates Python code using AST parsing and analysis."""
    
    def __init__(self, max_nodes: int = 100):
        self.max_nodes = max_nodes

    def validate_syntax(self, code: str) -> ValidationResult:
        """
        Perform basic syntax validation using Python's ast.parse()
        
        Args:
            code: The Python code to validate
            
        Returns:
            ValidationResult containing success status and any error details
        """
        try:
            # Check code length
            if len(code) > 1000:
                return ValidationResult(
                    success=False,
                    message="Code is too long. Please keep it under 1000 characters.",
                )

            # Try to parse the code
            tree = ast.parse(code)
            
            # Check AST node count
            node_count = sum(1 for _ in ast.walk(tree))
            if node_count > self.max_nodes:
                return ValidationResult(
                    success=False,
                    message=f"Code is too complex. Please simplify it.",
                    hints=["Try breaking down your code into smaller parts",
                          "Remove any unnecessary code"]
                )

            # Check for potential infinite loops
            loop_warnings = self._check_infinite_loops(tree)
            if loop_warnings:
                return ValidationResult(
                    success=False,
                    message="Your code might have an infinite loop!",
                    hints=loop_warnings
                )

            return ValidationResult(
                success=True,
                message="Code syntax is valid"
            )

        except SyntaxError as e:
            # Return kid-friendly error format for LLM translation
            return ValidationResult(
                success=False,
                message=str(e),
                error_line=e.lineno,
                error_column=e.offset,
                hints=None  # Will be filled by LLM
            )
        except Exception as e:
            # Handle any other parsing errors
            return ValidationResult(
                success=False,
                message=f"Unexpected error while checking code: {str(e)}"
            )

    def _check_infinite_loops(self, tree: ast.AST) -> List[str]:
        """
        Analyze code for potential infinite loops
        
        Args:
            tree: The AST to analyze
            
        Returns:
            List of warnings about potential infinite loops
        """
        warnings = []
        for node in ast.walk(tree):
            if isinstance(node, ast.While):
                # Check for while True
                if (isinstance(node.test, ast.Constant) and 
                    node.test.value is True):
                    warnings.append(
                        f"Line {node.lineno}: Found 'while True' - make sure you have a way to break the loop!"
                    )
                
                # Check for missing loop variable updates in while loops
                loop_vars = self._find_loop_variables(node.test)
                if not self._check_variables_updated(node.body, loop_vars):
                    warnings.append(
                        f"Line {node.lineno}: Loop variables might not be updated inside the while loop"
                    )
            
            elif isinstance(node, ast.For):
                if isinstance(node.iter, ast.Call):
                    # Check for range() calls with large or invalid arguments
                    if (isinstance(node.iter.func, ast.Name) and 
                        node.iter.func.id == 'range'):
                        self._check_range_args(node.iter, warnings)

        return warnings

    def _find_loop_variables(self, node: ast.AST) -> set:
        """Find variables used in loop conditions."""
        variables = set()
        for child in ast.walk(node):
            if isinstance(child, ast.Name):
                variables.add(child.id)
        return variables

    def _check_variables_updated(self, body: List[ast.AST], variables: set) -> bool:
        """Check if any of the given variables are modified in the loop body."""
        for node in ast.walk(ast.Module(body=body)):
            if isinstance(node, ast.AugAssign):
                if isinstance(node.target, ast.Name) and node.target.id in variables:
                    return True
            elif isinstance(node, ast.Assign):
                for target in node.targets:
                    if isinstance(target, ast.Name) and target.id in variables:
                        return True
        return False

    def _check_range_args(self, node: ast.Call, warnings: List[str]) -> None:
        """Check range() arguments for potential issues."""
        args = node.args
        if len(args) >= 1:
            if isinstance(args[0], ast.Constant):
                if args[0].value > 10000:
                    warnings.append(
                        f"Line {node.lineno}: Large range value detected - this might take too long!"
                    )