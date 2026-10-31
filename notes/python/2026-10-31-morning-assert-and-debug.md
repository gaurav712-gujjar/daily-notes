# assert and __debug__

**Category:** Python  
**Date:** 2026-10-31 (morning)

---

# assert Statement and the __debug__ Flag

The `assert` statement is a debugging aid that tests a condition at runtime.  
If the condition evaluates to `False`, Python raises an `AssertionError` with an optional message.  
Crucially, `assert` is a *statement*, not a function, and it can be stripped out of the bytecode when the interpreter is run with the `-O` (optimize) flag. In that mode, the global variable `__debug__` is set to `False` and all `assert` statements are ignored.

**Why it matters**

- **Quick sanity checks**: During development you can verify invariants (e.g., function arguments, internal state) without writing explicit `if` checks.
- **Zero‑cost in production**: By launching Python with `python -O script.py`, asserts disappear, eliminating any performance overhead while keeping the source unchanged.
- **Conditional debugging logic**: Code that should only run when debugging can be guarded by `if __debug__: …`, ensuring it’s omitted in optimized runs.

**Typical usage**

```python
def divide(a: float, b: float) -> float:
    assert b != 0, "Denominator must not be zero"
    return a / b

# Code executed only in debug mode
if __debug__:
    print("Running in debug mode")
```

When executed normally, the `assert` validates the denominator. Running `python -O script.py` disables the check and the `if __debug__` block, allowing the function to proceed unchecked (which may raise a `ZeroDivisionError`). Use asserts for development‑time guarantees, not for handling user‑input errors.
