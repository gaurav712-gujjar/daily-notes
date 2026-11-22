# Untitled Note - 1758

**Category:** Python  
**Date:** 2026-11-22 (afternoon)

---

# collections.namedtuple

`collections.namedtuple` creates tuple subclasses with named fields, giving you immutable, lightweight objects that are more readable than plain tuples. The function returns a new class; you instantiate it like any other class, and its fields can be accessed by attribute name or index.

**Why use it?**  
- **Readability:** Accessing `person.name` is clearer than `person[0]`.  
- **Immutability:** Like regular tuples, instances cannot be altered, which helps avoid side‑effects.  
- **Low overhead:** No `__dict__` is created, so memory usage stays close to that of a plain tuple.  
- **Convenient methods:** Namedtuples provide `_asdict()`, `_replace()`, and `_fields` for easy conversion and manipulation.

**Typical scenarios** include returning multiple values from a function, representing simple records (e.g., points, configurations), or replacing small data classes when you don’t need mutability or methods.

```python
from collections import namedtuple

# Define the tuple subclass
Point = namedtuple('Point', ['x', 'y'])

# Create instances
p1 = Point(3, 4)
p2 = Point(x=10, y=-2)

# Access fields
print(p1.x, p1.y)          # 3 4
print(p2[0], p2[
