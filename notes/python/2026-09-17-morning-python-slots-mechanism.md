# Python __slots__ Mechanism

**Category:** Python  
**Date:** 2026-09-17 (morning)

---

# Python __slots__ Mechanism

`__slots__` is a special class attribute that tells Python to allocate a fixed set of attributes for each instance, bypassing the per‑object `__dict__`. By doing so, it reduces memory consumption and can speed up attribute access, especially when creating many lightweight objects (e.g., nodes in a graph, data‑record objects, or parsers).

**When to use it**

- **Large collections of simple objects** – millions of instances where the overhead of a dict per object becomes significant.  
- **Performance‑critical code** – tighter attribute lookup and less memory churn can improve cache locality.  
- **Restricting attribute creation** – helps catch typos by raising `AttributeError` for undefined attributes.

**Key points**

- Define `__slots__` as an iterable of attribute names (strings).  
- Instances will no longer have a `__dict__` unless you explicitly include `'__dict__'` in `__slots__`.  
- Inheritance works, but each subclass must define its own `__slots__` (or inherit the parent’s).  
- You cannot add attributes not listed in `__slots__` at runtime.

```python
class Point:
    __slots__ = ('x', 'y')      # only allow x and y attributes

    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

p = Point(1.5, 2.5)
print(p.x, p.y)   # → 1.5 2.5
p.z = 3            # AttributeError: 'Point' object has no attribute 'z'
```

In the example, each `Point` instance stores only two floats without the overhead of a dictionary, yielding noticeable memory savings when many points are created.

---
