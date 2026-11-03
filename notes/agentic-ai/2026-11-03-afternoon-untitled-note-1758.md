# Untitled Note - 1758

**Category:** Agentic AI  
**Date:** 2026-11-03 (afternoon)

---

# Dynamic Tool Selection

**Concept**  
Dynamic tool selection lets an autonomous agent decide at runtime which external tool (e.g., a calculator, web search, database query, or code executor) best fits the current sub‑task. The agent maintains a lightweight policy that maps a textual description of the required operation to a tool identifier, often using a small classifier or a prompt‑based LLM that scores candidate tools.

**Why/Where Used**  
- **LLM‑powered assistants** that must alternate between reasoning, retrieval, and execution (e.g., answering a math question then fetching current stock prices).  
- **Robotic process automation** where a single workflow may involve file I/O, API calls, and visual inspection.  
- **Multi‑modal agents** that switch between vision, speech, or symbolic reasoning tools without hard‑coded branching.  

Dynamic selection improves efficiency (avoid unnecessary API calls), reduces hallucination (by delegating to reliable tools), and enables graceful degradation when a tool is unavailable.

**Minimal Example (Python + OpenAI)**  

```python
import json, openai

TOOLS = {
    "search": "https://api.search.com/query",
    "calc": "https://api.math.com/eval",
    "db": "https://api.db.com/query"
}

def choose_tool(query: str) -> str:
    prompt = f"""You are a tool selector. Choose the most appropriate tool for the user request.
Request: {query}
Tools: {', '.join(TOOLS.keys())}
Answer with only the tool name."""
    resp = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}],
        temperature=0
    )
    return resp.choices[0].message.content.strip()

def run_agent(user_input):
    tool = choose_tool(user_input)
    endpoint = TOOLS[tool]
    # simple HTTP call omitted for brevity
    print(f"Calling {tool} at {endpoint} …")

run_agent("What is the current price of Apple stock
