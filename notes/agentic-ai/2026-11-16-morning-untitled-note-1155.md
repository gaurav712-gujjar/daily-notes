# Untitled Note - 1155

**Category:** Agentic AI  
**Date:** 2026-11-16 (morning)

---

# Reflection Loop for Agentic LLMs  

**What it is**  
A *reflection loop* is a lightweight self‑evaluation phase that an autonomous language‑model agent executes after each action (or after a short sequence of actions). The agent generates a short summary of what it just did, checks consistency with its original goal, and optionally revises its plan before proceeding. This meta‑cognitive step mimics human “think‑again” behavior and helps catch hallucinations, dead‑ends, or safety violations early.

**Why / where it’s used**  
- **Goal‑driven assistants** (e.g., research agents) where a single mistaken step can waste resources.  
- **Tool‑using agents** that invoke external APIs; reflection can verify that the API call succeeded and the result makes sense.  
- **Safety‑critical pipelines** (code generation, medical advice) where a sanity check reduces risky outputs.  
- **Iterative reasoning** tasks such as multi‑turn planning, where the agent benefits from periodically re‑aligning to the high‑level objective.

**Simple implementation sketch (Python + OpenAI API)**  

```python
import openai

def reflect(state, last_output, goal):
    prompt = f"""You are an autonomous agent.  
Goal: {goal}
Current state: {state}
Last action output: {last_output}

1. Summarize what you just did in one sentence.  
2. Does this move you closer to the goal? Answer Yes/No and why.  
3. If No, propose a corrected next step.  

Provide the answer in JSON with keys: summary, ok, correction."""
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.0,
    )
    return resp.choices[0].message.content

# Example usage
goal = "Extract all product names and prices from the PDF catalog."
state = "Fetched page 3 of catalog and ran OCR."
last_output = "Returned raw OCR text with many formatting errors."
reflection = reflect(state, last_output, goal)
print(reflection)
```

The JSON response can be parsed; if `"ok": "No"` the agent updates its plan before the next
