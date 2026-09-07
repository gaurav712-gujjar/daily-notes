# Retrieval-Augmented Generation

**Category:** Generative AI  
**Date:** 2026-09-07 (afternoon)

---

# Retrieval‑Augmented Generation (RAG)

Retrieval‑Augmented Generation (RAG) combines a neural generator (e.g., a large language model) with an external non‑parametric knowledge store. At inference time the model first **retrieves** the most relevant documents or passages for a given query using a dense vector index (often built with a bi‑encoder). The retrieved texts are then **conditioned** on the generator, allowing it to produce answers that are both fluent and grounded in factual sources.

**Why it’s useful**  
- **Fact‑grounding:** Reduces hallucinations by anchoring generation to real documents.  
- **Scalability:** Knowledge can be updated without re‑training the entire language model.  
- **Domain adaptation:** A small, domain‑specific corpus can be plugged in to specialize a general‑purpose model.

**Typical workflow**  
1. Encode the user query → query vector.  
2. Perform a nearest‑neighbor search in the document index (FAISS, ScaNN, etc.).  
3. Concatenate the top‑k passages with the query and feed them to the generator.  
4. Optionally, apply a **fusion** step (e.g., marginalizing over retrieved passages) to improve robustness.

**Simple PyTorch example (using 🤗 transformers & faiss)**

```python
from transformers import RagTokenizer, RagRetriever, RagSequenceForGeneration
import torch

tokenizer = RagTokenizer.from_pretrained("facebook/rag-token-nq")
retriever = RagRetriever.from_pretrained(
    "facebook/rag-token-nq",
    index_name="exact",  # uses the built‑in Wikipedia index
    use_dummy_dataset=True  # for illustration only
)
model = RagSequenceForGeneration.from_pretrained("facebook/rag-token-nq",
                                                retriever=retriever)

question = "What are the main components of a transformer model?"
input_ids = tokenizer(question, return_tensors="pt").input_ids
generated = model.generate(input_ids)
print(tokenizer.batch_decode(generated, skip_special_tokens=True)[0])
```

The model first pulls relevant Wikipedia snippets about transformers, then generates a concise answer that reflects the retrieved facts.

---
