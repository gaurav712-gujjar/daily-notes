# Descriptor Protocol in Python

**Category:** Python  
**Date:** 2026-09-01 (afternoon)

---

# Descriptor Protocol in Python

A **descriptor** is any object that defines one or more of the methods `__get__`, `__set__`, and `__delete__`. When such an object is assigned to a class attribute, Python automatically routes attribute access through these methods. Descriptors give fine‑grained control over attribute behavior, enabling patterns like computed properties, type checking, lazy loading, and managing storage without exposing implementation details.

**Why use descriptors?**  
- **Reusable attribute logic**: Define a single descriptor class and reuse it across many attributes or classes.  
- **Encapsulation**: Hide storage details (e.g., keep data in a private dictionary) while exposing a clean public API.  
- **Performance**: Implement cached or lazily evaluated properties without the overhead of `@property` each time.  
- **Framework internals**: Django ORM fields, `attrs` library, and many ORM/serialization tools rely on descriptors.

### Simple example

```python
class Typed:
    """Descriptor that enforces a type on assignment."""
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(f'Expected {self.expected_type}')
        instance.__dict__[self.name] = value

class Person:
    age = Typed('age', int)      # age must be an int
    name = Typed('name', str)    # name must be a str

p = Person()
p.age = 30          # works
p.name = 'Alice'    # works
# p.age = 'old'     # raises TypeError
```

In this snippet, `Typed` centralizes type‑checking logic, making the `Person` class concise and safe.

---
