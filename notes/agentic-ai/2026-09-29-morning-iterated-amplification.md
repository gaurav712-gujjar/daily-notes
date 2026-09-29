# Iterated Amplification

**Category:** Agentic AI  
**Date:** 2026-09-29 (morning)

---

# Iterated Amplification

Iterated Amplification (IA) is a training paradigm for building **agentic AI systems** that can perform tasks beyond the immediate capability of a single model. The core idea is to recursively combine a *base model* with a *human overseer* (or a surrogate overseer) to form an **amplifier** that can solve more complex problems. The amplified system then generates new training data, which is used to improve the base model. Repeating this loop—amplify → train → amplify—allows the system to progressively acquire sophisticated reasoning and planning abilities without requiring the human to directly solve the hardest sub‑tasks.

**Why it matters:**  
- **Alignment:** IA provides a systematic way to align powerful models by keeping humans (or trustworthy proxies) in the loop at every amplification step.  
- **Scalability:** By delegating sub‑tasks to the model itself, the human workload grows only logarithmically with task difficulty.  
- **Generalization:** The base model learns from a diverse set of amplified solutions, encouraging robust, transferable skills.

**Typical workflow**

```python
# Pseudo‑code for one IA iteration
def amplify(problem):
    # Decompose problem with the overseer (human or surrogate)
    subproblems = overseer.decompose(problem)
    # Solve each subproblem with the current model
    answers = [model.solve(sp) for sp in subproblems]
    # Combine answers via overseer synthesis
    return overseer.synthesize(answers)

# Generate training data
train_set = []
for task in curriculum:
    solution = amplify(task)
    train_set.append((task, solution))

# Fine‑tune the base model
model = train(model, train_set)
```

In practice, IA has been explored for **formal theorem proving**, **complex game playing**, and **long‑horizon planning** where direct supervision is infeasible.

---
