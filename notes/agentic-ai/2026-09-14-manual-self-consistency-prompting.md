# Self-Consistency Prompting

**Category:** Agentic AI  
**Date:** 2026-09-14 (manual)

---

# Self‑Consistency Prompting for Language Model Agents

**Concept**  
Self‑consistency prompting is a technique that asks a language‑model‑based agent to generate multiple reasoning paths (e.g., chain‑of‑thought traces) for the same query and then selects the most common answer among them. By aggregating independent samples, the method reduces the variance caused by stochastic decoding and mitigates occasional reasoning errors.

**Why / Where it’s used**  
- **Complex decision‑making**: When an agent must solve arithmetic, logic puzzles, or multi‑step planning, a single sampled chain can be wrong. Majority voting across several chains yields higher accuracy.  
- **Safety‑critical assistants**: In medical or legal advice bots, self‑consistency adds a layer of verification without external tools.  
- **Few‑shot prompting**: The approach works with standard LLM APIs, requiring only prompt engineering and sampling parameters—no model fine‑tuning.

**Example (Python, OpenAI API)**  

```python
import openai, numpy as np

def self_consistent_answer(question, n_samples=8, temperature=0.8):
    prompt = f"""Answer the following question step‑by‑step.
Question: {question}
Answer:"""
    responses = []
    for _ in range(n_samples):
        resp = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[{"role":"user","content":prompt}],
            temperature=temperature,
            max_tokens=300,
        )
        # extract final numeric/short answer from the chain‑of‑thought
        answer = resp.choices[0].message.content.strip().splitlines()[-1]
        responses.append(answer)

    # majority vote
    return max(set(responses), key=responses.count)

print(self_consistent_answer("If a train travels 60 km/h for 2 h and then 80 km/h for 1.5 h, how far did it go?"))
```

The function samples several reasoning traces, pulls the terminal answer from each, and returns the most frequent result, achieving higher reliability than a single generation.
