# Structural Pattern Matching

**Category:** Python  
**Date:** 2026-10-11 (afternoon)

---

# Structural Pattern Matching (`match` / `case`)

Python 3.10 introduced **structural pattern matching**, a powerful control‑flow construct inspired by languages like Haskell and Rust. Using the `match` statement, you can compare a subject value against a series of *patterns* and destructure complex data in a readable way, replacing verbose `if‑elif‑else` chains.

**Why use it?**  
- **Clarity:** Matching on dictionaries, sequences, or custom classes becomes declarative.  
- **Safety:** Patterns enforce exhaustive checking when combined with static type checkers.  
- **Convenience:** Automatic unpacking of nested structures eliminates manual indexing.

**Typical use‑cases** include parsing JSON payloads, interpreting abstract syntax trees, handling command‑line arguments, or routing messages in event‑driven systems.

```python
def handle_message(msg):
    match msg:
        case {"type": "error", "code": code, "msg": text}:
            print(f"⚠️ Error {code}: {text}")
        case {"type": "data", "payload": [x, y, z]}:
            print(f"Received trio: {x}, {y}, {z}")
        case {"type": "ping"}:
            return "pong"
        case _:
            print("Unknown message format")

# Example
handle_message({"type": "data", "payload": [1, 2, 3]})
```

In the example, the `match` block cleanly distinguishes between different dictionary shapes, extracting fields (`code`, `text`, `x`, `y`, `z`) without explicit key lookups.

Structural pattern matching expands Python’s expressive toolkit, making code that works with heterogeneous data both succinct and maintainable.
