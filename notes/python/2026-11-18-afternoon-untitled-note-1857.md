# Untitled Note - 1857

**Category:** Python  
**Date:** 2026-11-18 (afternoon)

---

# Python __new__ Method

`__new__` is the first step in the object creation process. It is a static method that receives the class (`cls`) and the arguments passed to the constructor, creates and returns a new instance (usually by calling `super().__new__(cls)`). After `__new__` returns the instance, Python invokes `__init__` to initialise it.  

**Why use it?**  
- **Immutable types**: For classes that subclass immutable built‑ins (e.g., `int`, `str`, `tuple`), you must customise the value before the object becomes immutable, which can only be done in `__new__`.  
- **Singleton / caching**: Controlling instance creation lets you implement singletons or object
