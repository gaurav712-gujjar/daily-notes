# Untitled Note - 0759

**Category:** Generative AI  
**Date:** 2026-10-17 (morning)

---

# ControlNet: Spatial Conditioning for Diffusion Models  

ControlNet augments a pretrained diffusion model with an extra “control” branch that injects spatial hints (e.g., edge maps, sketches, depth maps) while keeping the original generative capabilities intact. The control branch is trained to predict the same latent noise as the base model but conditioned on both the noisy latent and the auxiliary map. During inference, the control map guides the diffusion process, letting users steer image synthesis without retraining the whole model.

**Why it matters**  
- **Fine‑grained control**: Artists can dictate composition, pose, or layout while still benefiting from the model’s learned creativity.  
- **Zero‑shot adaptation**: A single pretrained diffusion model can be repurposed for many tasks (edge‑to‑photo, pose‑to‑image, depth‑guided generation) by swapping the control map.  
- **Efficiency**: Only a lightweight side network is added; training costs are modest compared to training a new diffusion model from scratch.

**Typical use cases**  
- Sketch‑to‑photo conversion in graphic design.  
- Depth‑guided image synthesis for AR/VR scene generation.  
- Pose‑conditioned character creation in game development.

**Minimal example (🤗 Diffusers)**  

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch, cv2

# Load pretrained ControlNet (edge‑conditioned) and base Stable Diffusion
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

# Prepare a Canny edge map as conditioning input
image = cv2.imread("portrait.jpg")
edge = cv2.Canny(image, 100, 200)
edge = edge[:, :, None]  # (H, W, 1) required by pipeline

prompt = "A photorealistic portrait of a woman in a
