# Untitled Note - 1557

**Category:** Python  
**Date:** 2026-10-27 (afternoon)

---

# `__init_subclass__` Hook

`__init_subclass__` is a special class method that Python calls automatically **whenever a new subclass is created**. It receives the subclass object as its first argument (`cls`) and any keyword arguments passed in the subclass definition. By default it does nothing, but you can override it in a base class to enforce contracts, register subclasses, or inject common behavior.

**Why use it?**  
- **Automatic registration:** Build plugin systems where each subclass registers itself in a central registry without extra boiler‑plate.  
- **Interface enforcement:** Validate that required class attributes or methods are defined, raising errors early.  
- **Mixin configuration:** Allow mixins to customize subclass creation (e.g., adding descriptors or default attributes).

**Typical pattern**

```python
class PluginBase:
    _registry = {}

    def __init_subclass__(cls, *, name: str, **kwargs):
        super().__init_subclass__(**kwargs)   # keep normal inheritance chain
        if not hasattr(cls, 'run'):
            raise TypeError(f"{cls.__name__} must implement a 'run' method")
        # Register the plugin by the provided name
        PluginBase._registry[name] = cls

# Example plugin
class HelloPlugin(PluginBase, name="hello"):
    def run(self):
        print("Hello, world!")

print(PluginBase._registry)   # {'hello': <class '__main__.HelloPlugin'>}
```

In this example, any subclass of `PluginBase` must define a `run` method and supplies a `name` keyword that the base class
