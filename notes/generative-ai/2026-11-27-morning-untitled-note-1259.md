# Untitled Note - 1259

**Category:** Generative AI  
**Date:** 2026-11-27 (morning)

---

# Plug-and-Play Language Models (PPLM)

Plug‑and‑Play Language Models (PPLM) are a lightweight technique for steering a pretrained language model toward desired attributes **without** fine‑tuning the entire model.  
A small “attribute model” (e.g., a classifier or a bag‑of‑words bag) provides gradient signals that are injected into the hidden states of a frozen decoder (like GPT‑2) during generation. By iteratively adjusting the hidden representation, the output text gradually aligns with the target style, topic, or sentiment while retaining fluency.

**Why use PPLM?**  
- **Zero‑shot controllability:** No costly retraining on large corpora.  
- **Modular:** Swap attribute models on‑the‑fly for different constraints (e.g., political bias, formality, domain‑specific jargon).  
- **Preserves knowledge:** The base LM’s world knowledge stays intact because its weights remain frozen.

**Typical applications**  
- Controlled story generation (e.g., “write a sci‑fi narrative with a hopeful tone”).  
- Targeted data augmentation for low‑resource domains.  
- Safe‑guarding LLM outputs against undesired content.

**Simple example (PyTorch + 🤗 Transformers)**

```python
import torch
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from pplm import PPLMGenerator  # hypothetical wrapper

tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2
