# Magic attribute methods

**Category:** Python  
**Date:** 2026-10-13 (afternoon)

---

# Magic Attribute Methods (`__getattr__` & `__setattr__`)

Python lets classes intercept attribute access through special “magic” methods.  
- `__getattr__(self, name)` is invoked **only when** the requested attribute isn’t found in the instance’s normal dictionary (`__dict__`). It can compute a value on‑the‑fly, delegate to another object, or raise a custom error.  
- `__setattr__(self, name, value)` runs **every time** an attribute is assigned, giving a hook to validate data, enforce immutability, or store values elsewhere (e.g., in a database or a C extension).

These hooks are useful for:
* **Lazy loading** – defer expensive computation until the attribute is actually needed.  
* **Proxy objects** – forward attribute look‑ups to a wrapped object without exposing it directly.  
* **Data validation** – enforce type or range checks centrally, avoiding repetitive boiler‑plate.  

```python
class Config:
    def __init__(self):
        self._store = {}

    def __getattr__(self, name):
        # Called only if attribute not in __dict__
        try:
            return self._store[name]
        except KeyError:
            raise AttributeError(f"{name} not defined")

    def __setattr__(self, name, value):
        # Allow normal attribute for internal dicts
        if name.startswith('_'):
            super().__setattr__(name, value)
        else:
            # Simple validation example
            if not isinstance(value, (int, float)):
                raise TypeError("Config values must be numeric")
            self._store[name] = value

cfg = Config()
cfg.learning_rate = 0.01      # validated and stored in _store
print(cfg.learning_rate)      # retrieved via __getattr__
```

In this pattern, the public API (`cfg.learning_rate`) feels like a normal attribute, while the class internally controls storage and validation.
