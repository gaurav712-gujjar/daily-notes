# Untitled Note - 1121

**Category:** Agentic AI  
**Date:** 2026-11-11 (morning)

---

# Tree‑of‑Thoughts Planning for Agentic AI  

**Concept**  
Tree‑of‑Thoughts (ToT) extends the classic chain‑of‑thought prompting by exploring multiple reasoning paths in a tree structure. At each step an LLM generates several candidate “thoughts” (intermediate actions or answers). A selection policy—often a simple scoring function or a secondary model—picks the most promising nodes, which are then expanded further. The process continues until a leaf node satisfies the task or a depth limit is reached.  

**Practical Use**  
- **Complex problem solving** where a single linear chain may miss viable solutions (e.g., combinatorial puzzles, code synthesis, theorem proving).  
- **Autonomous agents** that must plan actions in uncertain environments; the tree lets the agent evaluate alternative futures before committing.  
- **Tool‑augmented agents** that can decide whether to call an external API, query a database, or continue reasoning internally.  

**Minimal Example (Python + OpenAI API)**  

```python
import openai, itertools, math

def score_thought(thought):
    # simple heuristic: shorter, more specific thoughts get higher scores
    return -len(thought) + thought.count(":") * 2

def tree_of_thoughts(prompt, depth=2, breadth=3):
    frontier = [(prompt, [])]                     # (current_text, path)
    for d in range(depth):
        new_frontier = []
        for text, path in frontier:
            # generate multiple candidate thoughts
            resp = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=[{"role":"user","content":text}],
                temperature=0.7,
                n=breadth,
                stop=None,
            )
            candidates = [c['message']['content'] for c in resp['choices']]
            # evaluate and keep the best one
            scores = [score_thought(c) for c in candidates]
            best_idx = scores.index(max(scores))
            best = candidates[best_idx]
