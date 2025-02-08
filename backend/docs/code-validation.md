# Code Validation System Design

## Overview
The code validation system uses a two-stage approach combining local syntax checking with LLM-based semantic validation to provide kid-friendly feedback for Python exercises.

## Validation Flow

### Stage 1: Quick Syntax Check
- Uses Python's built-in `ast.parse()` to perform fast, local syntax validation
- No API cost for basic syntax checking
- If syntax error is found, sends error to LLM for translation into kid-friendly terms
- Prevents unnecessary API calls for code that wouldn't execute anyway

### Stage 2: LLM Validation
- Only triggered if syntax check passes
- Provides semantic validation of code correctness
- Generates natural, kid-friendly feedback
- Can understand multiple correct solutions
- Provides contextual hints based on common mistakes

## Security & Sandboxing

### Restricted Python Environment
- Blocked builtins:
  ```python
  BLOCKED_BUILTINS = {
      'eval', 'exec', 'compile',    # Code execution
      'open', 'file',               # File operations
      '__import__', 'import',       # Module imports
      'input',                      # User input
      'globals', 'locals',          # Scope access
      'getattr', 'setattr',         # Attribute access
      'delattr',                    # Attribute deletion
      'breakpoint', 'exit',         # Program flow
  }
  ```

- Blocked modules:
  ```python
  BLOCKED_MODULES = {
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
  ```

### Resource Limits
- Memory limits:
  - Maximum heap size: 32MB
  - Maximum stack size: 8MB
  - Array size limit: 10000 elements
  
- Time limits:
  - Execution timeout: 3 seconds
  - CPU time limit: 1 second
  - Maximum iterations: 10000 (for loops)

- Code size limits:
  - Maximum characters: 1000
  - Maximum lines: 50
  - Maximum AST nodes: 100

### Edge Cases
- Infinite loops:
  ```python
  def count_iterations(node):
      """Count potential iterations in loops"""
      if isinstance(node, ast.For):
          if isinstance(node.iter, ast.Call):
              if isinstance(node.iter.func, ast.Name):
                  if node.iter.func.id == 'range':
                      # Check range arguments
                      pass
  ```

- Memory leaks:
  ```python
  def check_memory_patterns(node):
      """Look for patterns that might cause memory issues"""
      if isinstance(node, ast.ListComp):
          # Check list comprehension size
          pass
      elif isinstance(node, ast.While):
          # Check for growing collections in while loops
          pass
  ```

## Implementation Approaches

### Option 1: RestrictedPython
Pros:
- Battle-tested in production (used by Plone CMS)
- Built-in security policies
- Handles most common security concerns
- Regular maintenance and updates
- Good documentation

Cons:
- More complex than needed for our simple use case
- May need to override some policies for kid-friendly features
- Additional dependency to maintain
- Learning curve for customization

### Option 2: Custom AST-based Sandbox
Pros:
- Complete control over implementation
- Can be tailored exactly to our needs
- Minimal dependencies
- Easier to understand and modify
- Can start simple and add features as needed

Cons:
- Need to implement security features from scratch
- Risk of missing security edge cases
- More initial development time
- Need thorough testing

### Recommendation
Start with the custom AST-based approach because:
1. Our initial exercises are simple (variables, basic operations)
2. We can implement only what we need
3. Easier to add kid-friendly features
4. Better learning opportunity
5. Can switch to RestrictedPython later if needed

## LLM Integration

### Syntax Error Translation Prompt
```
You are a friendly Python teacher helping young students learn programming.
The student is learning about {concept} in Python.

Here is their code:
{code}

They received this error message:
{error}

Please provide a kid-friendly explanation of what went wrong and how to fix it.
Include specific line numbers and references to their code when relevant.

Provide feedback in the following JSON format:
{
  "message": "kid-friendly explanation of the error",
  "hints": ["specific suggestion 1", "specific suggestion 2"],
  "errorLine": line_number,
  "errorColumn": column_number
}
```

#### Example Syntax Error Response
```json
{
  "message": "Oops! On line 2, it looks like you forgot to put an equals sign (=) between 'blocks' and '12'. Remember, when we're creating a variable, we need to use = to give it a value!",
  "hints": [
    "Try adding an equals sign: blocks = 12",
    "Check if all your other variables use the equals sign too"
  ],
  "errorLine": 2,
  "errorColumn": 7
}
```

### Code Validation Prompt
```
You are a Python teacher evaluating student code.
Exercise: {exercise_description}
Expected outcome: {expected_outcome}

Student code:
{code}

Provide feedback in the following JSON format:
{
  "success": boolean,
  "message": "kid-friendly feedback message",
  "hints": ["hint1", "hint2"] // optional
}
```

#### Example Code Validation Response
```json
{
  "success": true,
  "message": "Fantastic job! You've correctly created variables for all the toys with the right numbers. Your toy organizer is working perfectly! 🎉",
  "hints": [
    "Try changing the numbers to see how your variables update!",
    "Can you think of other toys you might want to keep track of?"
  ]
}
```

## Optimization Strategies

### Caching
- Cache key format: `{exercise_id}:{hash_of_code}`
- TTL values:
  - Syntax error translations: 24 hours (errors are consistent)
  - Code validations: 1 hour (allows for exercise updates)
  - Failed API responses: 5 minutes (quick recovery)
- Cache storage:
  - Redis for production
  - In-memory for development
- Cache warming:
  - Pre-cache common syntax error translations
  - Update cache on exercise content changes

### Rate Limiting
- Per student limits:
  - 30 submissions per minute
  - 300 submissions per hour
  - 1000 submissions per day
- Global limits:
  - 1000 LLM requests per minute
  - 10000 LLM requests per hour
- Rate limit storage:
  - Redis sliding window
  - Separate counters for syntax and semantic validation
- Limit bypass for teachers/admins

### Error Handling
- Fallback to basic syntax error messages if LLM API fails
- Local validation rules for critical requirements:
  - Maximum code length: 1000 characters
  - Restricted Python builtins and modules
  - Memory usage limits
- Retry strategy for API failures:
  - Maximum 3 retries
  - Exponential backoff (1s, 2s, 4s)
  - Circuit breaker if error rate exceeds 10%

## API Response Format
```typescript
interface ValidationResult {
  success: boolean;
  message: string;
  hints?: string[];
  errorLine?: number;
  errorColumn?: number;
}
```

## Next Steps
1. Implement basic AST parsing and validation
2. Add simple resource limits (time, memory)
3. Implement basic security restrictions
4. Set up LLM API integration
5. Create error message cache
6. Add monitoring
7. Evaluate needs for additional security features