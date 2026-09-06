# Untitled Note - 1344

**Category:** Agentic AI  
**Date:** 2026-09-06 (afternoon)

---

# ReAct Prompting for Agents

**Concept**  
ReAct (Reason + Act) prompting is a lightweight recipe that equips a language model with a loop of reasoning steps followed by concrete actions. The prompt instructs the model to output *thought* strings (e.g., “I need to look up the current price”) and *action* strings (e.g., “search[Apple stock price]”). After each action, the environment returns a result, which is fed back into the model, allowing it to iteratively refine its plan until a final answer is produced.

**Why/where it’s used**  
- **Tool‑augmented agents**: enables LLMs to call APIs, browse the web, or query a database without hard‑coded pipelines.  
- **Explainability**: the interleaved reasoning trace makes the agent’s decision process transparent.  
- **Robustness**: errors in early steps can be corrected in later iterations because the model continuously re‑evaluates the context.  
- **Rapid prototyping**: developers can build capable agents with just a few prompt examples, avoiding complex RL‑fine‑tuning.

**Simple Python example (using OpenAI’s `gpt‑3.5‑turbo`)**

```python
import openai, json

def react_agent(user_query):
    messages = [
        {"role": "system",
         "content": "You are a ReAct agent. Respond with 'Thought: ...' then optionally 'Action: <tool>[arg]'."},
        {"role": "user", "content": user_query}
    ]

    while True:
        resp = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=messages,
                                            temperature=0.0)
        out = resp.choices[0].message.content.strip()
        print(out)

        if out.startswith("Action:"):
