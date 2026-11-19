# Reflection Loop

**Category:** Agentic AI  
**Date:** 2026-11-19 (morning)

---

# Reflection Loop for Agentic LLMs  

A **reflection loop** is a lightweight meta‑cognitive stage that lets an autonomous language model review its own output before committing to an action. After generating a plan or answer, the model re‑prompts itself with a “reflection” query (e.g., *“Is this plan feasible? Are there missing constraints?”*). The model then produces a critique, possibly revises the original response, and finally executes the refined result. This mirrors human self‑checking and helps mitigate hallucinations or unsafe actions.

**Why it matters**  
- **Safety**: Detects contradictory or risky steps before they are executed.  
- **Robustness**: Improves success rates on complex multi‑step tasks such as web‑automation or data‑pipeline orchestration.  
- **Transparency**: Generates a natural‑language audit trail that can be inspected by developers or regulators.  

**Typical usage**:  
Agentic assistants (e.g., autonomous research agents, code‑generation bots) embed a reflection loop after each reasoning cycle. The loop is often limited to a fixed number of iterations to keep latency low.

```python
def reflect_and_execute(llm, prompt, max_reflect=2):
    plan = llm.generate(prompt)                     # initial plan
    for _ in range(max_reflect):
        critique = llm.generate(f"Critique the plan:\n{plan}")
        if "no issues" in critique.lower():
            break
        plan = llm.generate(f"Revise the plan based on:\n{critique}")
    return llm.execute(plan)                        # run the final plan
```

In practice, the `llm.generate` calls use system‑level prompts that enforce the reflection role, and `llm.execute` translates the refined plan into concrete API calls or shell commands.

---
