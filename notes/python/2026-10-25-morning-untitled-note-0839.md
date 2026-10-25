# Untitled Note - 0839

**Category:** Python  
**Date:** 2026-10-25 (morning)

---

# contextlib.ExitStack

`ExitStack` is a flexible context‑manager helper from the **contextlib** module that lets you enter and clean up an arbitrary number of context managers programmatically. Unlike a static `with` block, an `ExitStack` can dynamically add resources (files, locks, network connections, etc.) at runtime and guarantees that all of them are correctly closed, even if an exception occurs part‑way through.

### When to use it
- **Dynamic resource handling**: when the number of resources isn’t known until the code runs (e.g., opening a list of files supplied by the user).
- **Combining heterogeneous clean‑up actions**: you can register arbitrary callables (like `obj.close`) alongside regular context managers.
- **Simplifying nested `with` statements**: replaces deep nesting (`with A() as a, B() as b, C() as c:`) with a single, readable block.

### Quick example
```python
from contextlib import ExitStack

filenames = ['data1.txt', 'data2.txt', 'missing.txt']

with ExitStack() as stack:
    # Open all existing files; missing ones are skipped gracefully
    files = []
    for name in filenames:
        try:
            f = stack.enter_context(open(name, 'r'))
            files.append(f)
        except FileNotFoundError:
            print(f'⚠️  {name} not found – skipping')
    
    # At this point all successfully opened files are in `files`
    for f in files:
        print(f.readline().strip())
# All opened files are automatically closed here, even if an error occurs
