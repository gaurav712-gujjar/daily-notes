# Untitled Note - 0959

**Category:** Generative AI  
**Date:** 2026-10-02 (morning)

---

# ControlNet: Conditional Control for Diffusion Models  

ControlNet is a plug‑and‑play neural network architecture that adds **explicit conditioning** to pre‑trained diffusion models (e.g., Stable Diffusion). It learns a **parallel “control” branch** that takes an additional map—such as edge maps, pose skeletons, or depth—and injects this information into the diffusion UNet via **zero‑initialized convolutional layers**. Because the control branch starts with zero weights, the original diffusion model’s generative capability remains unchanged; training only tunes the control path, making fine‑tuning fast and memory‑efficient.

**Why use it?**  
- **Precise layout control**: Generate images that follow a user‑provided structure (e.g., a sketch or human pose).  
- **Multi‑modal guidance**: Combine depth, segmentation, or keypoints with text prompts for richer synthesis.  
- **Parameter efficiency**: Only a few million extra parameters are needed, enabling rapid adaptation to new tasks without retraining the whole diffusion model.  
- **Versatility**: Works with any diffusion backbone that exposes cross‑attention features.

**Typical workflow**  
1. Extract a conditioning map (Canny edge, pose, etc.).  
2. Feed the map and the text prompt to the ControlNet‑augmented diffusion pipeline.  
3. The model produces images that respect both the textual description and the structural cue.

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import cv2, torch

# 1️⃣ Load ControlNet (edge‑conditioned) and Stable Diffusion
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)
pipe
