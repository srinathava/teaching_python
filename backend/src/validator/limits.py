import resource
import signal
from dataclasses import dataclass
from typing import Optional, Callable, Any
import threading
from contextlib import contextmanager

@dataclass
class ResourceLimits:
    """Configuration for resource limits."""
    max_memory: int = 32 * 1024 * 1024  # 32MB
    max_stack: int = 8 * 1024 * 1024    # 8MB
    max_time: float = 3.0               # 3 seconds
    max_cpu_time: float = 1.0           # 1 second

class ResourceError(Exception):
    """Raised when code exceeds resource limits."""
    pass

class TimeoutError(ResourceError):
    """Raised when code execution times out."""
    pass

class MemoryError(ResourceError):
    """Raised when code exceeds memory limits."""
    pass

def _timeout_handler(signum: int, frame: Any) -> None:
    """Signal handler for timeout."""
    raise TimeoutError("Code execution timed out")

class ResourceLimiter:
    """Enforces resource limits on code execution."""

    def __init__(self, limits: Optional[ResourceLimits] = None):
        self.limits = limits or ResourceLimits()

    def _set_memory_limits(self) -> None:
        """Set memory limits using resource module."""
        # Set maximum heap size
        resource.setrlimit(resource.RLIMIT_AS, (self.limits.max_memory, self.limits.max_memory))
        # Set maximum stack size
        resource.setrlimit(resource.RLIMIT_STACK, (self.limits.max_stack, self.limits.max_stack))

    def _set_cpu_limits(self) -> None:
        """Set CPU time limits using resource module."""
        resource.setrlimit(
            resource.RLIMIT_CPU, 
            (int(self.limits.max_cpu_time), int(self.limits.max_cpu_time))
        )

    @contextmanager
    def apply_limits(self):
        """
        Context manager that applies resource limits.
        
        Usage:
            limiter = ResourceLimiter()
            with limiter.apply_limits():
                # Run restricted code here
        
        Raises:
            ResourceError: If code exceeds resource limits
        """
        old_handler = signal.signal(signal.SIGALRM, _timeout_handler)
        timer = threading.Timer(self.limits.max_time, signal.alarm, args=[1])

        try:
            # Set resource limits
            self._set_memory_limits()
            self._set_cpu_limits()

            # Start timeout timer
            timer.start()
            yield

        finally:
            # Clean up
            timer.cancel()
            signal.signal(signal.SIGALRM, old_handler)
            signal.alarm(0)

    def run_with_limits(self, func: Callable, *args, **kwargs) -> Any:
        """
        Run a function with resource limits applied.
        
        Args:
            func: Function to run
            *args: Positional arguments for the function
            **kwargs: Keyword arguments for the function
            
        Returns:
            The return value of the function
            
        Raises:
            ResourceError: If code exceeds resource limits
        """
        with self.apply_limits():
            return func(*args, **kwargs)

    @staticmethod
    def check_code_size(code: str) -> None:
        """
        Check if code size is within limits.
        
        Args:
            code: The Python code to check
            
        Raises:
            ResourceError: If code exceeds size limits
        """
        # Check character count
        if len(code) > 1000:
            raise ResourceError("Code exceeds maximum length of 1000 characters")

        # Check line count
        if len(code.splitlines()) > 50:
            raise ResourceError("Code exceeds maximum of 50 lines")

    @staticmethod
    def check_collection_size(collection: Any) -> None:
        """
        Check if a collection's size is within limits.
        
        Args:
            collection: The collection to check
            
        Raises:
            ResourceError: If collection exceeds size limits
        """
        try:
            if len(collection) > 10000:
                raise ResourceError("Collection size exceeds maximum of 10000 elements")
        except TypeError:
            # Object doesn't support len()
            pass