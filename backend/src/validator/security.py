import ast
from typing import Set, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class SecurityViolation:
    """Represents a security violation found in code."""
    message: str
    line: Optional[int] = None
    node: Optional[ast.AST] = None

class SecurityChecker:
    """Enforces security restrictions on Python code execution."""

    # Blocked built-in functions that could be dangerous
    BLOCKED_BUILTINS: Set[str] = {
        'eval', 'exec', 'compile',    # Code execution
        'open', 'file',               # File operations
        '__import__', 'import',       # Module imports
        'input',                      # User input
        'globals', 'locals',          # Scope access
        'getattr', 'setattr',         # Attribute access
        'delattr',                    # Attribute deletion
        'breakpoint', 'exit',         # Program flow
    }

    # Blocked modules that could be used maliciously
    BLOCKED_MODULES: Set[str] = {
        'os',        # System operations
        'sys',       # System-specific
        'subprocess',# Command execution
        'socket',    # Network
        'requests',  # HTTP requests
        'urllib',    # URL handling
        'pathlib',   # File paths
        'pickle',    # Serialization
        'json',      # Not needed for basic exercises
        're',        # Regular expressions
    }

    def check_code(self, code: str) -> list[SecurityViolation]:
        """
        Check code for security violations.
        
        Args:
            code: The Python code to check
            
        Returns:
            List of SecurityViolation objects describing any violations found
        """
        violations = []
        try:
            tree = ast.parse(code)
            violations.extend(self._check_imports(tree))
            violations.extend(self._check_builtins(tree))
            violations.extend(self._check_attributes(tree))
        except SyntaxError:
            # Syntax errors are handled by the validator, not security
            pass
        return violations

    def _check_imports(self, tree: ast.AST) -> list[SecurityViolation]:
        """Check for blocked module imports."""
        violations = []
        for node in ast.walk(tree):
            # Check import statements
            if isinstance(node, ast.Import):
                for name in node.names:
                    if name.name.split('.')[0] in self.BLOCKED_MODULES:
                        violations.append(SecurityViolation(
                            f"The module '{name.name}' is not allowed for security reasons",
                            node.lineno,
                            node
                        ))
            
            # Check from ... import statements
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.module.split('.')[0] in self.BLOCKED_MODULES:
                    violations.append(SecurityViolation(
                        f"The module '{node.module}' is not allowed for security reasons",
                        node.lineno,
                        node
                    ))
        
        return violations

    def _check_builtins(self, tree: ast.AST) -> list[SecurityViolation]:
        """Check for use of blocked built-in functions."""
        violations = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Name) and node.id in self.BLOCKED_BUILTINS:
                violations.append(SecurityViolation(
                    f"The built-in function '{node.id}' is not allowed for security reasons",
                    getattr(node, 'lineno', None),
                    node
                ))
        return violations

    def _check_attributes(self, tree: ast.AST) -> list[SecurityViolation]:
        """Check for dangerous attribute access."""
        violations = []
        for node in ast.walk(tree):
            if isinstance(node, ast.Attribute):
                # Check for access to dunder methods
                if node.attr.startswith('__') and node.attr.endswith('__'):
                    violations.append(SecurityViolation(
                        f"Access to dunder method '{node.attr}' is not allowed",
                        getattr(node, 'lineno', None),
                        node
                    ))
                
                # Check for dangerous attributes
                if node.attr in {'__globals__', '__code__', '__closure__'}:
                    violations.append(SecurityViolation(
                        f"Access to '{node.attr}' is not allowed for security reasons",
                        getattr(node, 'lineno', None),
                        node
                    ))
        
        return violations

    def create_restricted_globals(self) -> Dict[str, Any]:
        """
        Create a restricted globals dictionary for code execution.
        
        Returns:
            Dictionary of allowed global variables and functions
        """
        restricted_globals = {}
        
        # Add safe builtins
        safe_builtins = dict(__builtins__)
        for name in self.BLOCKED_BUILTINS:
            safe_builtins.pop(name, None)
        
        restricted_globals['__builtins__'] = safe_builtins
        
        return restricted_globals