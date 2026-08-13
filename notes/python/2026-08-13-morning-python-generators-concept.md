# Python Generators Concept

**Category:** Python  
**Date:** 2026-08-13 (morning)

---

# Python Generators
Python generators are a type of iterable, like lists or tuples, but they do not allow indexing and can only be iterated over once. They are created using functions and the yield keyword, which produces a value from the function and suspends its execution until the next value is requested. This allows generators to be more memory-efficient than storing entire lists in memory.

Generators are useful when working with large datasets or infinite sequences, as they only store the current value in memory. They are commonly used in data processing, web scraping, and reading large files. For example, a generator can be used to read a large file line by line, processing each line without loading the entire file into memory.

Here's a simple example of a generator that produces the Fibonacci sequence:
```python
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for _ in range(10):
    print(next(fibonacci()))
```
However, the above code has a mistake as it creates a new generator for each iteration. Instead, we should create the generator once and then use it in a loop.

Generators are an essential tool in Python programming, allowing for efficient and scalable data processing.
