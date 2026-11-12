# Python __name__ Main Guard

**Category:** Python  
**Date:** 2026-11-12 (afternoon)

---

# Python __name__ Main Guard

When a Python file is executed, the interpreter sets a special variable `__name__`. If the file is run directly, `__name__` becomes the string `"__main__"`; if it is imported as a module, `__name__` holds the module’s filename (e.g., `"utils"`).  

The idiom

```python
if __name__ == "__main__":
    # code that runs only when the file is executed directly
    main()
```

acts as a *guard* that separates reusable library code from script‑level execution. This prevents heavy‑weight operations—such as parsing command‑line arguments, launching a server, or running tests—from occurring unintentionally when the file is imported elsewhere.

**Why use it?**

- **Modularity:** Write functions and classes once and reuse them across projects without side effects.
- **Testing:** Allows quick manual testing of a module by running it directly while keeping the same code importable in test suites.
- **Entry‑point clarity:** Makes the script’s entry point explicit, improving readability.

**Example**

```python
# utils.py
def add(a, b):
    """Return the sum of two numbers."""
    return a + b

def main():
    import sys
    a, b = map(int, sys.argv[1:3])
    print(f"{a} + {b} = {add(a, b)}")

if __name__ == "__main__":
    main()
```

Running `python utils.py 3 5` prints `3 + 5 = 8`, while `import utils` in another script gives access to `add` without triggering `main()`.

---
