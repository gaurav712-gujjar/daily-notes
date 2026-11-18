# Untitled Note - 1206

**Category:** Python  
**Date:** 2026-11-18 (morning)

---

# __all__ Variable

`__all__` is a module‑level list that defines the public interface of a Python module. When a user executes `from mymodule import *`, only the names listed in `__all__` are imported; everything else stays hidden. If `__all__` is absent, the import‑star statement brings in every name that does **not** start with an underscore.

### Why use it?
- **Encapsulation** – Prevents internal helpers, constants, or experimental functions from being exposed unintentionally.
- **Documentation** – Signals to readers which symbols are meant for external use.
- **Namespace hygiene** – Reduces the risk of name clashes in the consuming code, especially in large projects or libraries.

### Typical usage
```python
# mymodule.py
__all__ = ["add", "multiply"]

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def _helper(x):
    # internal use only
    return x ** 2
```

```python
# consumer.py
from mymodule import *

print(add(2, 3))        # works
print(multiply(4, 5))   # works
print(_helper(3))       # NameError: name '_helper' is not defined
```

Even without `import *`, tools like `pydoc` and IDEs respect `__all__` when generating public API listings, making it a lightweight yet powerful way to control a module’s outward‑facing contract
