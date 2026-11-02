# __init_subclass__ Hook

**Category:** Python  
**Date:** 2026-11-02 (morning)

---

# __init_subclass__ Hook

`__init_subclass__` is a special class method that Python calls automatically whenever a class is subclassed. It receives the newly created subclass as its first argument (`cls`) and can be used to enforce constraints, register subclasses, or inject common behavior into all descendants. Unlike `__new__` or `__init__`, which run when *instances* are created, `__init_subclass__` runs at *class definition* time, making it ideal for metaprogramming patterns without requiring a full metaclass.

**Why use it?**  
- **Automatic registration**: Build plugin systems where every subclass registers itself in a registry.  
- **Interface enforcement**: Ensure that subclasses implement required methods or attributes, raising errors early.  
- **Mixin initialization**: Provide default class‑level attributes or modify the subclass’s namespace.

**Example**

```python
class PluginBase:
    registry = {}

    def __init_subclass__(cls, *, name: str, **kwargs):
        super().__init_subclass__(**kwargs)
        if not hasattr(cls, "run"):
            raise TypeError(f"{cls.__name__} must define a 'run' method")
        PluginBase.registry[name] = cls

# concrete plugins
class HelloPlugin(PluginBase, name="hello"):
    def run(self):
        print("Hello, world!")

class AddPlugin(PluginBase, name="add"):
    def run(self, a, b):
        print(a + b)

print(PluginBase.registry)
# {'hello': <class '__main__.HelloPlugin'>, 'add': <class '__main__.AddPlugin'>}
```

In this snippet, every subclass of `PluginBase` must provide a `run` method and automatically registers itself under a given name, simplifying discovery and usage of plugins.
