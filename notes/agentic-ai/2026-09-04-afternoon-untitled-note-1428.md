# Untitled Note - 1428

**Category:** Agentic AI  
**Date:** 2026-09-04 (afternoon)

---

# Tool‑Use Planning in ReAct Agents

ReAct (Reason & Act) agents combine chain‑of‑thought reasoning with explicit tool usage. The **tool‑use planning** subcomponent decides *when* to invoke external functions (e.g., a calculator, web search, or database query) and *how* to format the request. It treats tool calls as first‑class actions in the reasoning trace, enabling language models to solve tasks that exceed pure text inference.

**Why it matters**  
- **Extended competence**: By delegating arithmetic, factual lookup, or code execution to specialized tools, agents overcome the hallucination limits of LLMs.  
- **Efficiency**: Heavy computations are offloaded, keeping the LM prompt short and inference fast.  
- **Safety**: Explicit tool calls can be sandboxed and audited, reducing the risk of unsafe generation.

**Typical workflow**  
1. The LLM generates a reasoning step ending with a *tool marker* (e.g., `[[TOOL:search|query=...]`)  
2. The planner parses the marker, selects the appropriate API, and executes it.  
3. The tool’s output is injected back into the prompt as a new observation, and the LLM continues reasoning.

**Python sketch (using OpenAI‑compatible API)**

```python
import json, requests

def tool_search(query: str) -> str:
    # simple web search stub
    resp = requests.get("https://api.duckduckgo.com",
                        params={"q": query, "format": "json"})
    return resp.json().get("Abstract", "No result")

def react_step(prompt: str) -> str:
    # call LLM (pseudo)
    response = llm.complete(prompt)
    if "[[TOOL:" in response:
        marker = response.split("[[TOOL:")[1].split("]]")[0]
        name, args = marker.split("|", 1)
        args = dict(arg.split("=") for arg in args.split(","))
        if name == "search":
            tool_out = tool_search(args["query"])
        else:
            tool_out = "Unsupported tool"
        # inject observation
        return f"{response}\nObservation: {tool_out}"
