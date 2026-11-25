# Chain-of-Thought Prompting

**Category:** Generative AI  
**Date:** 2026-11-25 (morning)

---

# Chain-of-Thought Prompting

**What it is**  
Chain‑of‑Thought (CoT) prompting is a technique for large language models (LLMs) that encourages them to generate explicit intermediate reasoning steps before arriving at a final answer. Instead of asking “What is 23 × 47?” we prepend a cue such as “Let’s think step by step:” so the model produces a logical chain of deductions that leads to the solution.

**Why/where it’s used**  
CoT improves performance on tasks requiring multi‑hop reasoning, math, commonsense inference, and symbolic manipulation. By making the reasoning transparent, it also helps users audit model outputs and reduces hallucinations in high‑stakes applications like tutoring, code assistance, and decision support.

**Quick example (OpenAI API, Python)**  

```python
import openai

def cot_answer(question):
    prompt = f"""Answer the following question with a step‑by‑step explanation.

Q: {question}
A: Let's think step by step."""
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
    )
    return response.choices[0].message.content.strip()

print(cot_answer("What is the product of 23 and 47?"))
```

The model will first outline multiplication steps (e.g., “23 × 40 = 920; 23 × 7 = 161”) and then sum them, yielding a correct answer with an interpretable rationale.

---
