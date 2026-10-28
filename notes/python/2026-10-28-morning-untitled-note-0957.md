# Untitled Note - 0957

**Category:** Python  
**Date:** 2026-10-28 (morning)

---

# TypedDict

`TypedDict` lets you describe dictionary objects with a fixed set of keys and specific value types, while still behaving like regular dicts at runtime. Introduced in **PEP 589**, it lives in the `typing` module (or `typing_extensions` for older Python versions).  

**Why use it?**  
- **Static type checking:** Tools such as *mypy* can verify that you’re accessing the right keys and assigning the correct value types.  
- **Self‑documenting code:** The expected shape of a dict is explicit, reducing bugs caused by misspelled keys or wrong data types.  
- **Interoperability:** Works with JSON‑like structures (e.g., API payloads) where a full dataclass would be overkill.

**Typical scenario** – handling a JSON response from a web service:

```python
from typing import TypedDict, Literal

class UserResponse(TypedDict):
    id: int
    name:
