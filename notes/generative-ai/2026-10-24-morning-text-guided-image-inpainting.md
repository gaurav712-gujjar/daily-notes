# Text-guided Image Inpainting

**Category:** Generative AI  
**Date:** 2026-10-24 (morning)

---

# Text‑guided Image Inpainting

**What it is**  
Text‑guided image inpainting uses a diffusion model to fill missing or masked regions of an image while following a natural‑language description. The model first corrupts the known pixels with a diffusion process, then reverses the process conditioned on both the visible context and the prompt, generating content that is semantically aligned with the text.

**Why/where it’s used**  
- Restoring damaged photographs where the user wants a specific object (e.g., “add a red balloon”).  
- Content‑aware editing in design tools, allowing non‑technical users to describe changes.  
- Generating training data by realistically removing and re‑adding objects.  

**Simple example (🤗 Diffusers)**  

```python
from diffusers import StableDiffusionInpaintPipeline
import torch, PIL.Image as Image

pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting", torch_dtype=torch.float16
).to("cuda")

# Load image and binary mask (white = region to replace)
image = Image.open("old_photo.jpg").convert("RGB")
mask  = Image.open("mask.png").convert("L")

prompt = "a vintage red sports car parked in front of the house"

result = pipe(prompt=prompt, image=image, mask_image=mask, num_inference_steps=50)
result.images[0].save("edited_photo.png")
```

The `mask_image` tells the model where to generate, and the `prompt` steers the semantics of the new content. This pipeline works out‑of‑the‑box for many common editing scenarios.

---
