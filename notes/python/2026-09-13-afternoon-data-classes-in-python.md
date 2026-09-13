# Data Classes in Python

**Category:** Python  
**Date:** 2026-09-13 (afternoon)

---

# Data Classes in Python

**What they are**  
Introduced in Python 3.7, the `@dataclass` decorator automatically generates special methods like `__init__`, `__repr__`, `__eq__`, and optionally `__lt__` for classes that primarily store data. By declaring fields with type hints, the decorator handles boiler‑plate code, making the class definition concise and readable.

**Why / where to use**  
Data classes shine when you need lightweight containers for structured data—e.g., configuration objects, API response models, or domain entities in a small‑scale application. They improve maintainability because changes to the data schema are reflected instantly without manually updating constructors or comparators. Additionally, they cooperate well with tools that rely on type hints (mypy, IDEs) and can be frozen to create immutable instances, useful for hashable keys in dictionaries or sets.

**Quick example**

```python
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class Point:
    x: float
    y: float

@dataclass
class Polygon:
    vertices: List[Point] = field(default_factory=list)

    def area(self) -> float:
        # simple shoelace formula assuming vertices are ordered
        s = 0.0
        n = len(self.vertices)
        for i in range(n):
            x1, y1 = self.vertices[i].x, self.vertices[i].y
            x2, y2 = self.vertices[(i + 1) % n].x, self.vertices[(i + 1) % n].y
            s += x1 * y2 - x2 * y1
        return abs(s) / 2
```

`Point` instances are immutable and hashable, while `Polygon` automatically gets an initializer and a readable `repr`. This eliminates repetitive code and keeps the focus on the domain logic.
