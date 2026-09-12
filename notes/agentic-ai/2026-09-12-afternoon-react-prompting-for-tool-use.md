# ReAct Prompting for Tool Use

**Category:** Agentic AI  
**Date:** 2026-09-12 (afternoon)

---

# ReAct Prompting for Tool Use

ReAct (Reason & Act) is a prompting pattern that equips large language model (LLM) agents with the ability to **reason** about a task and **act** by invoking external tools (e.g., calculators, web search, database queries). The prompt interleaves natural‑language thoughts with explicit tool‑call actions, allowing the model to decompose problems, retrieve needed information, and iteratively refine its answer.

**Why it matters**  
- **Robustness**: By grounding reasoning in verifiable tool outputs, agents avoid hallucinations on factual queries.  
- **Extensibility**: New tools can be added without retraining the LLM—just extend the action vocabulary.  
- **Transparency**: The reasoning trace (thought → action → observation) is readable, aiding debugging and alignment audits.  

**Typical use‑cases**  
- Open‑domain question answering that requires up‑to‑date web data.  
- Data‑analysis assistants that call SQL or pandas APIs.  
- Personal assistants that schedule events via calendar APIs.

**Python example (using OpenAI’s `gpt‑4o‑mini` and a mock calculator tool)**

```python
import json, openai

def calculator(expr: str) -> str:
    """Simple safe eval for arithmetic expressions."""
    try:
        return str(eval(expr, {"__builtins__": {} }))
    except Exception as e:
        return f"Error: {e}"

def run_react(prompt: str, tools):
    messages = [{"role": "system", "content": "You are a ReAct agent. Use the following tool when needed: calculator."},
                {"role": "user", "content": prompt}]
    while True:
        resp = openai.ChatCompletion.create(model="gpt-4o-mini", messages=messages)
        out = resp.choices[0].message.content.strip()
        print(out)                         # show thought/action trace
        if out.startswith("Action:"):
            arg = out.split("Action:")[1].strip()
            result = calculator(arg)
            messages.append({"role": "assistant", "content": out})
            messages.append({"role": "tool", "content": result})
        else:
            break

run_react("What is the sum of the first 12 prime numbers?", tools=["calculator"])
```

The agent first reasons about needing a sum, calls `calculator` with the expression, receives the result, and finally returns the answer.

---
