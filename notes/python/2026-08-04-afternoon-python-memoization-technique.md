# Python Memoization Technique

**Category:** Python  
**Date:** 2026-08-04 (afternoon)

---

# Python Memoization
Python memoization is an optimization technique that stores the results of expensive function calls so that they can be reused instead of recomputed. This technique is particularly useful when dealing with recursive functions or functions that perform complex computations. By storing the results of these function calls, memoization can significantly improve the performance of an application.

Memoization is commonly used in practice to optimize functions that are called repeatedly with the same arguments, such as in dynamic programming, recursive algorithms, and web applications. It can be implemented using a cache data structure, such as a dictionary, to store the results of function calls.

Here's a simple example of memoization in Python:
```python
def fibonacci(n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]
```
This example demonstrates how memoization can be used to optimize the Fibonacci function, which is a classic example of a recursive function that can benefit from memoization.
