from validator.ast_validator import ASTValidator
from validator.security import SecurityChecker
from validator.limits import ResourceLimiter

def test_validation():
    """Test various code validation scenarios."""
    ast_validator = ASTValidator()
    security_checker = SecurityChecker()
    resource_limiter = ResourceLimiter()

    test_cases = [
        # Valid code
        {
            "name": "Valid variable assignment",
            "code": "x = 42\ny = x + 10\nprint(y)",
            "should_pass": True
        },
        # Syntax error
        {
            "name": "Syntax error",
            "code": "x = 42;\ny = x +\nprint(y)",
            "should_pass": False
        },
        # Security violation
        {
            "name": "Security violation - os import",
            "code": "import os\nos.system('ls')",
            "should_pass": False
        },
        # Resource limit violation
        {
            "name": "Resource limit - code too long",
            "code": "x = 1\n" * 100,  # More than 50 lines
            "should_pass": False
        },
        # Infinite loop detection
        {
            "name": "Infinite loop detection",
            "code": "while True:\n    x = 1",
            "should_pass": False
        }
    ]

    print("Running validation tests...\n")

    for test in test_cases:
        print(f"Testing: {test['name']}")
        print(f"Code:\n{test['code']}\n")

        try:
            # Check resource limits
            try:
                resource_limiter.check_code_size(test['code'])
            except Exception as e:
                print(f"Resource limit violation: {str(e)}")
                if test['should_pass']:
                    print("❌ Test failed: Expected pass but got resource error\n")
                else:
                    print("✅ Test passed: Caught resource violation as expected\n")
                continue

            # Check syntax
            syntax_result = ast_validator.validate_syntax(test['code'])
            if not syntax_result.success:
                print(f"Syntax error: {syntax_result.message}")
                if test['should_pass']:
                    print("❌ Test failed: Expected pass but got syntax error\n")
                else:
                    print("✅ Test passed: Caught syntax error as expected\n")
                continue

            # Check security
            security_violations = security_checker.check_code(test['code'])
            if security_violations:
                print(f"Security violation: {security_violations[0].message}")
                if test['should_pass']:
                    print("❌ Test failed: Expected pass but got security violation\n")
                else:
                    print("✅ Test passed: Caught security violation as expected\n")
                continue

            # All checks passed
            if test['should_pass']:
                print("✅ Test passed: Code validated successfully\n")
            else:
                print("❌ Test failed: Expected failure but code passed validation\n")

        except Exception as e:
            print(f"Unexpected error: {str(e)}")
            print("❌ Test failed due to unexpected error\n")

if __name__ == "__main__":
    test_validation()