# Untitled Note - 1428

**Category:** Generative AI  
**Date:** 2026-10-25 (afternoon)

---

# DreamBooth Fine‑Tuning

**What it is**  
DreamBooth is a lightweight fine‑tuning technique for text‑to‑image diffusion models (e.g., Stable Diffusion). Instead of retraining the whole model, DreamBooth learns a small set of *concept embeddings* that associate a user‑provided subject (a person, object, or style) with a unique token. During generation, the model can render the new subject in arbitrary contexts while preserving its original visual quality.

**Why / Where it’s used**  
- **Personalized content creation** – generate images of a specific product, pet, or character without large‑scale data collection.  
- **Brand‑consistent marketing** – inject a logo or mascot into diverse scenes while keeping the diffusion model’s aesthetics.  
- **Rapid prototyping** – a handful of reference images (≈3‑5) are enough to teach the model, making it feasible for designers and hobbyists.

**Typical workflow**  
1. Pick a rare placeholder token (e.g., `<newperson>`).  
2. Prepare 3‑5 high‑resolution photos of the target subject.  
3. Fine‑tune the UNet and text encoder on a combined loss of diffusion denoising and a *prior preservation* term that keeps the model from collapsing to the new concept only.  
4. Use the new token in any prompt: `"A portrait of <newperson> riding a bicycle in the rain"`.

**Minimal code example (🤗 Diffusers)**

```python
from diffusers import StableDiffusionPipeline, StableDiffusionDreamBoothTrainer
import torch

# Load base model
pipe = StableDiffusionPipeline.from_pretrained("runwayml/stable-diffusion-v1-5")
pipe.to("cuda")

# Prepare DreamBooth trainer
trainer = StableDiffusionDreamBoothTrainer(
    model=pipe,
    instance_prompt="a photo of <newperson>",
    instance_images="./data/newperson/",   # 3‑5 images
    class_prompt="a photo of a person",
    class_images="./data/person/",         # optional for prior preservation
)

trainer.train(num_train_epochs=3, learning_rate=5e-6)

# Save and reload
pipe.save_pretrained("./dreambooth
