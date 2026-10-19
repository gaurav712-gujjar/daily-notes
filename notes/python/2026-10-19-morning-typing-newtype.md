# typing.NewType

**Category:** Python  
**Date:** 2026-10-19 (morning)

---

# typing.NewType

`typing.NewType` lets you create distinct type aliases that are treated as separate types by static type checkers (like mypy) while incurring **no runtime overhead**. It’s essentially a thin wrapper around the underlying type, used only for static analysis.

```python
from typing import NewType

UserId = NewType('UserId', int)   # distinct type for user identifiers
Score  = NewType('Score',  float) # distinct type for game scores

def get_user_name(uid: UserId) -> str:
    ...

uid = UserId(42)      # cast int → UserId
score = Score(99.5)   # cast float → Score

# The following would raise a type‑checker error:
# get_user_name(score)   # Incompatible type "Score"; expected "UserId"
```

**Why use it?**  
- **Clarity:** Communicates intent (e.g., differentiating between `UserId` and `ProductId` even though both are `int`).  
- **Safety:** Prevents accidental mix‑ups in large codebases; static checkers catch mismatched usages.  
- **Zero cost:** At runtime `UserId` is just an `int`; the conversion is a simple identity function.

Typical scenarios include API layers, database models, and any place where primitive types represent different domain concepts. By defining lightweight, purpose‑specific types, you improve readability and reduce bugs without sacrificing performance.
