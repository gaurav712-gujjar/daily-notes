# Importlib Lazy Module Loading

**Category:** Python  
**Date:** 2026-09-23 (morning)

---

# Importlib Lazy Module Loading

Python’s `importlib` module offers a programmatic way to import other modules. While the standard `import` statement loads a module eagerly, `importlib` can defer loading until the module’s attributes are actually accessed—known as lazy loading. This is valuable for reducing startup time, lowering memory usage, and avoiding heavy‑weight imports (e.g., pandas, TensorFlow) when they might never be needed in a particular execution path.

Typical use‑cases include:
- **Command‑line tools** that support many optional sub‑commands, each requiring different heavy dependencies.
- **Web applications** where each request may need only a subset of utilities.
- **Plugin architectures** that discover and load plugins on demand.

`importlib.util.LazyLoader` wraps a module spec, creating a proxy object that loads the real module upon first attribute access.

```python
import importlib.util
import sys

def lazy_import(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    lazy_mod = importlib.util.LazyLoader(importlib.util.module_from_spec(spec))
    sys.modules[name] = lazy_mod
    spec.loader.exec_module(lazy_mod)   # registers the lazy loader
    return lazy_mod

# Example: defer loading of a heavy library
np = lazy_import('numpy', '/usr/local/lib/python3.11/site-packages/numpy/__init__.py')

print("Module imported, but NumPy not loaded yet.")
# NumPy loads only when we first use it
arr = np.arange(5)
print(arr)
```

In the snippet, `numpy` is only loaded when `np.arange` is called, keeping the initial script lightweight. Use lazy loading judiciously; excessive deferral can make debugging harder and obscure import errors until runtime.
