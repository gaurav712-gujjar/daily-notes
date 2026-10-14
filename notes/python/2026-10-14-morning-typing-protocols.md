# Typing Protocols

**Category:** Python  
**Date:** 2026-10-14 (morning)

---

# Typing Protocols (PEP 544)

**What it is**  
`typing.Protocol` lets you define an interface‑like contract without requiring explicit inheritance. A class that implements the required attributes and methods is considered a subtype (structural subtyping), even if it doesn’t inherit from the protocol class.

**Why/where it’s used**  
- **Static type checking**: Tools like MyPy can verify that objects passed to a function conform to the expected shape, catching bugs early.  
- **Duck‑typing safety**: You retain Python’s dynamic flexibility while gaining compile‑time guarantees.  
- **Library design**: Public APIs can describe required behaviours without forcing users into a specific class hierarchy.

**Example**

```python
from typing import Protocol, runtime_checkable

class SupportsClose(Protocol):
    def close(self) -> None: ...

@runtime_checkable
class JsonSerializable(Protocol):
    def to_json(self) -> str: ...

def cleanup(resource: SupportsClose) -> None:
    """Close any resource that follows the SupportsClose protocol."""
    resource.close()

class FileWrapper:
    def __init__(self, path: str):
        self.f = open(path, "r")
    def close(self) -> None:
        self.f.close()

cleanup(FileWrapper("example.txt"))   # ✅ type‑checked as valid

# Runtime check for JsonSerializable
def is_json_serializable(obj: object) -> bool:
    return isinstance(obj, JsonSerializable)

class User:
    def to_json(self) -> str: return '{"name":"Alice"}'

print(is_json_serializable(User()))   # True
```

In the snippet, `cleanup` accepts any object with a `close` method, regardless of its inheritance chain. The `runtime_checkable` decorator enables `isinstance` checks on protocols at runtime.

**Key take‑aways**  
- Use protocols to describe required methods/attributes.  
- Combine with `@runtime_checkable` for dynamic checks.  
- They improve readability and safety while preserving Python’s dynamic nature.
