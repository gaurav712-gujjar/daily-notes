# Untitled Note - 0811

**Category:** Generative AI  
**Date:** 2026-09-04 (afternoon)

---

# ControlNet for Diffusion Models  

ControlNet is a lightweight neural “plug‑in” that adds conditional control to pretrained diffusion generators (e.g., Stable Diffusion) without retraining the whole model. It learns a parallel branch that takes extra guidance maps—such as edge maps, pose skeletons, or segmentation masks—and injects their features into the diffusion UNet via cross‑attention. Because the base diffusion weights stay frozen, training is fast (often a few hundred thousand steps) and the same ControlNet can be swapped to guide many downstream tasks.

**Why it matters**  
- **Fine‑grained control**: Users can dictate structure (lines, depth, layout) while still benefiting from the rich visual quality of large diffusion models.  
- **Zero‑shot adaptability**: A single pretrained ControlNet can be applied to any prompt, enabling image‑to‑image, pose‑to‑image, or depth‑to‑image generation without task‑specific finetuning.  
- **Modular workflow**: Designers can compose multiple ControlNets (e.g., edge + color) to progressively refine outputs.

**Simple example (🤗 Diffusers)**  

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch
from PIL import Image
import requests, numpy as np

# 1️⃣ Load pretrained ControlNet (edge condition)
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)

# 2️⃣ Build the pipeline with frozen Stable Diffusion
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

# 3️⃣ Prepare a canny edge map as conditioning image
url = "https://example.com/photo.jpg"
image = Image.open(requests.get(url, stream=True).raw).convert("RGB")
edge = pipe.controlnet_processor(image, low_threshold=100, high_threshold=200)

# 4️⃣ Generate a guided result
output = pipe
