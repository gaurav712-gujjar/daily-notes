# Goal Decomposition

**Category:** Agentic AI  
**Date:** 2026-09-18 (morning)

---

# Goal Decomposition for Agentic LLMs  

Goal decomposition is the process of breaking a high‑level user intent into a sequence of concrete, executable sub‑goals that an autonomous language‑model agent can act on step‑by‑step. Instead of asking the model to “plan a weekend trip to Tokyo,” the system first splits the request into tasks such as *search flights*, *book accommodation*, *create an itinerary*, and *send confirmations*. Each sub‑goal is then handed to a specialized tool (search API, calendar API, email sender, etc.), and the agent monitors progress, revises plans when a step fails, and finally aggregates the results.

**Why it matters**  
- **Reliability**: Smaller, well‑defined actions reduce hallucinations and make error handling tractable.  
- **Transparency**: The intermediate plan can be inspected or edited by a human supervisor.  
- **Scalability**: Complex workflows (e.g., multi‑day research projects) become composable from reusable sub‑tasks.

**Typical usage**  
Agentic frameworks like LangChain, AutoGPT, or OpenAI Function Calling embed a planner that outputs a JSON list of sub‑goals. The planner is often a prompting pattern (“You are a planner. Decompose the user request…”) combined with a validator that checks each sub‑goal’s feasibility before execution.

```python
# Simple goal‑decomposer using OpenAI function calling
import openai, json

def decompose(goal: str):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user",
                   "content":f"Break the following request into ordered sub‑goals with a short description each:\n\n{goal}"}],
        functions=[{
            "name":"subgoals",
            "parameters":{
                "type":"object",
                "properties":{
                    "steps":{"type":"array","items":{"type":"object",
                        "properties":{"action":{"type":"string"},
                                      "detail":{"type":"string"}}}}}}],
        function_call={"name":"subgoals"}
    )
    steps = json.loads(response.choices[0].message.function_call.arguments)["steps"]
    return steps

print(decompose("Plan a weekend trip to Tokyo for 2 adults, including flights, hotel, and a food tour."))
```

The returned list can then be fed to an orchestrator that calls the appropriate tools for each `action`.
