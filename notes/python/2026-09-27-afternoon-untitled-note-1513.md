# Untitled Note - 1513

**Category:** Python  
**Date:** 2026-09-27 (afternoon)

---

# `__repr__` vs `__str__` in Python

Both `__repr__` and `__str__` are special (“dunder”) methods that define how an object is converted to a string, but they serve different audiences.

* **`__repr__`** – aims to produce an *unambiguous* representation, ideally one that could be used to recreate the object (`eval(repr(obj)) == obj`). It is meant for developers and debugging. If a specific `__repr__` is not provided, Python falls back to the default `<module.Class object at 0x...>`.

* **`__str__`** – produces a *readable* representation for end‑users. It is used by `print()`, `str()`, and string interpolation (`f"{obj}"`). When `__str__` is missing, Python falls back to `__repr__`.

Why it matters  
- In logs or interactive sessions, `repr` gives precise state, aiding debugging.  
- In UI output, `str` offers clean, user‑friendly text.  
- Libraries often implement both to separate internal diagnostics from public display.

```python
class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __repr__(self):
        return f"Point({self.x}, {self.y})"   # eval-able

    def __str__(self):
        return f"({self.x}, {self.y})"        # nice for users

p = Point(3, 4)
print(repr(p
