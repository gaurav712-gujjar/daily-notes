# Python Decorators

**Category:** Python  
**Date:** 2026-07-10 (afternoon)

---

# Python Decorators
Python decorators are a special type of function that can modify or extend the behavior of another function without permanently changing it. They allow developers to wrap a function with additional functionality without altering the original function's code. This concept is useful for adding logging, authentication, or other types of functionality to existing functions.

Decorators are commonly used in practice to implement aspects such as logging, security, and caching. They provide a flexible way to add new behaviors to functions without modifying their source code. For example, a decorator can be used to log the execution time of a function or to check if a user is authenticated before allowing them to access a certain function.

Here's a simple example of a decorator that logs the execution time of a function:
```python
import time
def timer_decorator(func):
    def wrapper():
        start_time = time.time()
        func()
        end_time = time.time()
        print(f"Function executed in {end_time - start_time} seconds")
    return wrapper

@timer_decorator
def example_function():
    time.sleep(2)

example_function()
```
This code defines a decorator `timer_decorator` that logs the execution time of the `example_function`.
