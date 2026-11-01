# Untitled Note - 1652

**Category:** Generative AI  
**Date:** 2026-11-01 (afternoon)

---

# Low‑Rank Adaptation (LoRA)

LoRA is a parameter‑efficient fine‑tuning technique for large generative models, especially transformer‑based LLMs and diffusion models. Instead of updating every weight, LoRA injects two low‑rank matrices **ΔA = BAᵀ** into each target linear layer, where **B** and **A** have a small rank *r* (e.g., 4 or 8). During training only these low‑rank matrices are learned; the original pretrained weights remain frozen. Mathematically, a weight matrix **W** becomes **W + ΔA**, preserving the knowledge of the base model while adapting to new tasks with a tiny number of extra parameters.

**Why use LoRA?**  
- **Memory‑efficient:** The added parameters are often <1 % of the original model size, enabling fine‑tuning on a single GPU.  
- **Fast convergence:** Low‑dimensional updates reduce the optimization landscape’s complexity.  
- **Modular:** Multiple LoRA adapters can be stacked or swapped, supporting multi‑task or domain‑specific deployment without re‑training the whole model.

**Typical applications** include instruction‑following LLMs, domain‑specific chatbots, and style‑transfer for diffusion models.

```python
from transformers import AutoModelForCausalLM, AutoTokenizer
from peft import get_peft_model, LoraConfig

model_name = "meta-llama/Meta-Llama-3-8B"
tokenizer = AutoTokenizer.from_pretrained(model_name)

base = AutoModelForCausalLM.from_pretrained(model_name, device_map="auto")
lora_cfg = LoraConfig(r=8, lora_alpha=32, target_modules=["q_proj", "v_proj"])
model = get_peft_model(base, lora_cfg)

inputs = tokenizer("Explain quantum tunneling
