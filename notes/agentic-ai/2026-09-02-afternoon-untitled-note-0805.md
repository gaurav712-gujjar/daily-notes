# Untitled Note - 0805

**Category:** Agentic AI  
**Date:** 2026-09-02 (afternoon)

---

# ReAct Prompting for Tool‑Using Agents

**Concept**  
ReAct (Reason + Act) is a prompting pattern that equips large‑language‑model (LLM) agents with the ability to interleave natural‑language reasoning and external tool calls. The prompt forces the model to emit a structured “thought” (reason) followed by an “action” (e.g., a web search, database query, or code execution). The LLM then observes the tool’s output and continues reasoning, creating a loop until the final answer is produced.

**Why / Where it’s used**  
- **Open‑ended QA** where factual grounding is required (search engines, calculators).  
- **Task automation** such as scheduling, data retrieval, or API orchestration.  
- **Safety‑enhanced agents** that must verify claims before responding, reducing hallucinations.  
- **Hybrid AI systems** that combine symbolic tools with neural reasoning, common in enterprise assistants and research assistants.

**Simple Python example (using OpenAI’s `gpt‑4o-mini` and a mock web‑search tool)**  

```python
import openai

def tool_search(query):
    # placeholder for a real search API
    return f"Top result for '{query}': https://example.com"

def react_agent(user_input):
    prompt = f"""You are an AI assistant that follows the ReAct pattern.
User: {user_input}
Answer step‑by‑step using "Thought:" and "Action:" lines.
When you need external
