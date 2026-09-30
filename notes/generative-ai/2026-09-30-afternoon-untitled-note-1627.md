# Untitled Note - 1627

**Category:** Generative AI  
**Date:** 2026-09-30 (afternoon)

---

# ControlNet Conditioning

ControlNet is a plug‑in architecture that adds a **trainable copy of a diffusion backbone** alongside a frozen pretrained diffusion model. By feeding an extra condition (e.g., edge maps, segmentation masks, depth maps) through the ControlNet branch, the generator can be steered to produce images that obey the supplied structure while still benefiting from the powerful priors of the original diffusion model.

**Why it matters**  
- **Precise control**: Artists can dictate layout, pose, or style without retraining the entire diffusion model.  
- **Data efficiency**: Only the conditioning branch is learned, requiring far fewer training images than full fine‑tuning.  
- **Versatility**: The same pretrained diffusion checkpoint can be reused for many modalities (scribbles, canny edges, pose skeletons, etc.).

**Typical use cases**  
- Sketch‑to‑image pipelines where a rough line drawing is turned into a photorealistic render.  
- Layout‑guided content creation for game assets or storyboards.  
- Interactive tools where users iteratively adjust conditions to refine outputs.

**Quick example (🤗 Diffusers)**

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch, cv2

# Load pretrained ControlNet for Canny edges
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)

pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

# Prepare conditioning image (Canny edge map)
orig = cv2.imread("sketch.png")
edge = cv2.Canny(cv2.cvtColor(orig, cv2.COLOR_BGR2GRAY), 100, 200)
edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2RGB)

prompt = "a serene mountain landscape, ultra‑realistic"
output = pipe(prompt, image=edge, num_inference_steps=30, guidance_scale=7.5)

output.images[0].save("result.png")
```

The code
