# Weak References

**Category:** Python  
**Date:** 2026-09-20 (afternoon)

---

# Weak References (`weakref` Module)

A **weak reference** points to an object without increasing its reference count. When the only remaining references to an object are weak, the garbage collector is free to reclaim it. Python’s `weakref` module lets you create such references, monitor object finalization, and build caches that don’t prevent memory release.

**Why use it?**  
- **Cache without leaks:** Store large objects (e.g., parsed XML trees) in a dictionary that automatically discards entries once the original objects are gone.  
- **Circular‑reference safety:** Break reference cycles in structures like graph nodes where each node holds references to its neighbors.  
- **Observer patterns:** Keep a list of listeners without forcing them to stay alive solely because they’re registered.

**Typical tools**  
- `weakref.ref(obj)`: a callable returning the referenced object or `None` if it’s dead.  
- `weakref.WeakKeyDictionary` / `WeakValueDictionary`: dict‑like containers that drop entries when keys or values are collected.  
- `weakref.finalize(obj, callback, *args, **kwargs)`: registers a cleanup function executed when `obj` is about to be finalized.

```python
import weakref

class Node:
    def __init__(self, name):
        self.name = name
        self.neighbors = weakref.WeakSet()   # holds weak refs to other nodes

    def connect(self, other):
        self.neighbors.add(other)

a = Node('A')
b = Node('B')
a.connect(b)
b.connect(a)

print(len(a.neighbors))   # 1
del b                     # b has no strong refs now
print(len(a.neighbors))   # 0, weak reference removed automatically
```

In this snippet, `WeakSet` ensures that neighbor links don’t keep nodes alive beyond their intended lifetime, preventing memory bloat in large, dynamic graphs.
