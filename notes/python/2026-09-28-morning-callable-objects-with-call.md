# Callable Objects with __call__

**Category:** Python  
**Date:** 2026-09-28 (morning)

---

# Callable Objects with `__call__`

In Python, any object that implements the special method `__call__(self, *args, **kwargs)` becomes **callable**, i.e., it can be invoked using the function‑call syntax `obj()`. This turns classes into lightweight function‑like entities while preserving state, making them ideal for configurable behaviours, strategy patterns, or simple factories.

**Why use `__call__`?**  
- **Encapsulation:** Keep related data and logic together without exposing a separate function.  
- **Flexibility:** Swap out behaviours at runtime by passing different callable instances.  
- **Readability:** Code that reads like a function call but carries its own context (e.g., a trained model object).  

**Typical scenarios** include custom loss functions in machine learning, on‑the‑fly data transformations, and simple command objects in CLI tools.

```python
class Power:
    """Raise numbers to a fixed exponent."""
    def __init__(self, exponent: int):
        self.exponent = exponent

    def __call__(self, x: float) -> float:
        return x ** self.exponent

square = Power(2)
cube   = Power(3)

print(square(5))  # 25
print(cube(2))    # 8
```

Here `Power` objects store the exponent and behave like functions, allowing interchangeable usage wherever a callable is expected.

---
