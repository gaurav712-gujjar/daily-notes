# Managed Attributes with Property

**Category:** Python  
**Date:** 2026-09-17 (afternoon)

---

# Managed Attributes with Property

The `property` built‑in turns ordinary methods into *managed attributes*, letting you compute values on‑the‑fly, enforce validation, or hide implementation details while preserving the simple dot‑notation syntax. Under the hood, `property` creates a descriptor object that defines `__get__`, `__set__`, and `__delete__` callbacks.

**Why use it?**  
- **Encapsulation** – expose a clean public API while keeping the internal storage private.  
- **Validation** – automatically check values whenever an attribute is assigned.  
- **Lazy computation** – compute expensive results only when needed and cache them if desired.  
- **Backward compatibility** – refactor a plain attribute to a computed one without breaking existing code.

**Typical pattern**

```python
class Circle:
    def __init__(self, radius: float):
        self._radius = radius               # “private” storage

    @property
    def radius(self) -> float:
        """Get the radius."""
        return self._radius

    @radius.setter
    def radius(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value

    @property
    def area(self) -> float:
        """Read‑only computed attribute."""
        from math import pi
        return pi * self._radius ** 2


c = Circle(5)
print(c.radius)   # 5
c.radius = 3       # validated assignment
print(c.area)      # 28.274333882308138
# c.area = 10      # AttributeError: can't set attribute
```

In this example, `radius` behaves like a normal attribute but runs validation on assignment, while `area` is a read‑only computed property. Using `property` keeps client code clean (`c.radius` instead of `c.get_radius()`) and provides a flexible hook for future changes.

---
