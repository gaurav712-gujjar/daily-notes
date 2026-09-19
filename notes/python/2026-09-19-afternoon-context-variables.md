# Context Variables

**Category:** Python  
**Date:** 2026-09-19 (afternoon)

---

# Context Variables (`contextvars`)

`contextvars` is a standard‑library module introduced in Python 3.7 that provides **context‑local storage**. Unlike thread‑local data (`threading.local`), a context variable’s value is tied to the *execution context* rather than the thread. This makes it safe for asynchronous code (e.g., `asyncio`) where many coroutines share the same thread but need isolated state.

### Why use it?
- **Async frameworks** (FastAPI, Starlette, Quart) often need request‑scoped data (user ID, DB session) without passing it explicitly through every call.
- **Testing**: you can temporarily override a variable’s value in a controlled context, then automatically revert.
- **Libraries**: enables “transparent” propagation of context (e.g., tracing, logging correlation IDs) across `await` boundaries.

### Basic usage
```python
import contextvars

# Declare a context variable with a default
request_id = contextvars.ContextVar('request_id', default='unknown')

def handler():
    # Read current value
    print('Request ID:', request_id.get())

async def process():
    # Set a value for this async task only
    token = request_id.set('abc-123')
    try:
        await some_coroutine()
        handler()                 # prints abc-123
    finally:
        # Restore previous value (important for cleanup)
        request_id.reset(token)

# In another coroutine the default remains
async def other():
    handler()                     # prints unknown
```

The `ContextVar.set()` call returns a token that can later restore the prior state with `reset()`. This deterministic behavior avoids leaks and makes context propagation explicit yet lightweight.

**When to choose**: Prefer `contextvars` over globals or thread‑locals whenever you need per‑task state in asynchronous or concurrent code, especially in web servers, background workers, or tracing libraries.
