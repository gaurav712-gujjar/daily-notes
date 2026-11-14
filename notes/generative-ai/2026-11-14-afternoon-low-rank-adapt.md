# Low-Rank Adapt

**Category:** Generative AI  
**Date:** 2026-11-14 (afternoon)

---

# Low‑Rank Adaptation (LoRA) for LLM Fine‑Tuning  

LoRA is a parameter‑efficient technique for adapting large language models (LLMs) to new tasks. Instead of updating all the millions or billions of weights, LoRA injects two small trainable matrices **A** and **B** (rank‑r) into each linear layer:  

\[
W_{\text{new}} = W + \Delta W,\;\; \Delta W = B A
\]

Because **A** (input‑side) and **B** (output‑side) have low rank, the additional parameters are tiny (often <1 % of the original model). During fine‑tuning only **A** and **B** are optimized; the original weights **W** stay frozen, preserving the pretrained knowledge and enabling rapid convergence.

### Practical Uses  
- **Domain adaptation** (e.g., medical, legal) where data is scarce.  
- **Instruction tuning** of LLMs for chat assistants.  
- **Multi‑task or continual learning** without catastrophic forgetting, since each task gets its own LoRA pair.  
- **Deployments on limited hardware** because the storage and compute overhead are minimal.

### Quick PyTorch Example (using 🤗 PEFT)

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import LoraConfig, get_peft_model

model_name = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

base_model = AutoModelForCausalLM.from_pretrained(
    model_name, device_map="auto", torch_dtype="auto"
)

lora_cfg = LoraConfig(
    r=8,          # rank
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],  # linear layers to adapt
    bias="none",
    task_type="CAUSAL_LM",
)

lora_model = get_peft_model(base_model, lora_cfg)
lora_model.print_trainable_parameters()  # shows ~0.5% of total params

# fine‑tune on your dataset …
```

LoRA thus makes LLM customization affordable, fast, and storage‑friendly, turning massive models into versatile, task‑specific generators.
