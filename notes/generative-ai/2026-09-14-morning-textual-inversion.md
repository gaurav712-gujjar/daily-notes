# Textual Inversion

**Category:** Generative AI  
**Date:** 2026-09-14 (morning)

---

# Textual Inversion

**What it is**  
Textual Inversion is a technique that lets you teach a text‑to‑image diffusion model a new “token” that represents a custom concept (e.g., a specific artist’s style, a rare object, or a personal mascot) using only a handful of reference images. The model learns a low‑dimensional embedding for the token while keeping the original weights frozen.

**Why/where it’s used**  
- **Personalization:** Add a user‑specific logo or character to a generative pipeline without retraining the whole model.  
- **Creative control:** Capture niche visual vocabularies (e.g., “my grandma’s kitchen”) that the base model never saw.  
- **Efficiency:** Training takes minutes on a single GPU, far cheaper than full fine‑tuning.

**Simple example (🤗 Diffusers + PyTorch)**  

```python
import torch
from diffusers import StableDiffusionPipeline, TextualInversionTrainer

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda")

# Assume `imgs/` contains 5–10 reference photos of the new concept
trainer = TextualInversionTrainer(
    pipe=pipe,
    train_dataset="imgs/",
    placeholder_token="<my_token>",
    initializer_token="artwork",   # start from a similar token
    num_steps=800,
)

trainer.train()
pipe.save_pretrained("my_custom_sd")
```

After training, you can generate images like:

```python
pipe("A portrait of a knight wearing <my_token> armor")
```

The model now interprets `<my_token>` as the learned visual style.

---
