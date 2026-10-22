# __repr__ vs __str__

**Category:** Python  
**Date:** 2026-10-22 (morning)

---

# __repr__ vs __str__

In Python, every object can define two special methods that control how it is converted to a string: `__repr__` and `__str__`.  

- **`__repr__`** (representation) is meant to produce an *official* string that, if possible, can be fed back to `eval()` to recreate the object. It should be unambiguous and primarily useful for developers.  
- **`__str__`** (string) provides a *readable* representation intended for end‑users. It is called by `print()` and `str()` and should be concise and friendly.

If only `__repr__` is defined, Python falls back to it for `str()` as well. Conversely, defining `__str__` without `__repr__` leaves `repr()` to use the default object memory address output.

### When to use each
- Implement `__repr__` for debugging, logging, or REPL sessions where you need to inspect objects quickly.  
- Implement `__str__` for user‑facing output, such as UI messages, reports, or `print` statements.

### Example

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"   # eval-able

    def __str__(self):
        return f"({self.x}, {self.y})"        # user‑friendly

p = Point(3, 4)
print(repr(p))   # -> Point(3, 4)
print(str(p))    # -> (3, 4)
print(p)         # __str__ is used automatically
```

By distinguishing these two methods, you keep debugging output precise while presenting clean, readable strings to end users.
