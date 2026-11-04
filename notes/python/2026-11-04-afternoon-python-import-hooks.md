# Python import hooks

**Category:** Python  
**Date:** 2026-11-04 (afternoon)

---

# Python Import Hooks (PEP 302)

Python’s import system is extensible via *import hooks*. By inserting custom finder or loader objects into `sys.meta_path`, you can control how modules are located, read, and executed. A **finder** decides whether it can handle a given module name, while a **loader** actually provides the module’s code (as source, byte‑code, or even a compiled extension).

Typical use‑cases include:
- Loading modules from non‑standard sources (e.g., zip archives, HTTP URLs, databases).
- Transforming source on the fly (e.g., transpiling a DSL to Python, applying code instrumentation).
- Implementing sandboxed environments where only a whitelist of modules may be imported.

### Minimal Example

```python
import sys
import importlib.abc
import importlib.util

class HelloWorldLoader(importlib.abc.Loader):
    def create_module(self, spec):
        return None                     # use default module creation

    def exec_module(self, module):
        module.msg = "Hello from a custom loader!"

class HelloWorldFinder(importlib.abc.MetaPathFinder):
    def find_spec(self, fullname, path, target=None):
        if fullname == "hello_world":
            return importlib.util.spec_from_loader(fullname, HelloWorldLoader())
        return None

# Register the finder
sys.meta_path.insert(0, HelloWorldFinder())

# Import triggers the hook
import hello_world
print(hello_world.msg)   # → Hello from a custom loader!
```

In this snippet, any `import hello_world` triggers the custom finder, which supplies a loader that injects a `msg` attribute into the module. Real‑world projects often combine this pattern with caching, byte‑code compilation, or security checks.

**Key take‑away:** Import hooks let you rewrite the import pipeline without altering existing code, making them powerful for plugins, testing frameworks, and domain‑specific languages.
