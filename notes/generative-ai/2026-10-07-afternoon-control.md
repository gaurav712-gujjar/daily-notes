# Control

**Category:** Generative AI  
**Date:** 2026-10-07 (afternoon)

---

# ControlNet Conditioning for Diffusion Models  

ControlNet is a plug‑and‑play neural network that adds fine‑grained spatial control to pretrained diffusion models (e.g., Stable Diffusion) without re‑training the entire generator. It takes an extra condition map—such as edge maps, depth maps, poses, or segmentation masks—and learns a lightweight set of residual blocks that steer the diffusion denoising process toward respecting that condition. Because the base diffusion weights stay frozen, training is fast and data‑efficient, making it ideal for tasks where only a modest amount of paired data (image + condition) is available.

**Practical uses**  
- **Image editing**: Users sketch edges, and ControlNet generates photorealistic images that follow the sketch.  
- **Content creation**: Artists supply pose or depth maps to guide character or landscape synthesis.  
- **Domain adaptation**: Adding semantic maps lets the model respect scene layout while keeping the original style.  

**Minimal example (Diffusers + PyTorch)**  

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch, cv2

# Load pretrained ControlNet for edge maps and the base Stable Diffusion model
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

# Prepare conditioning image (Canny edges)
image = cv2.imread("photo.jpg")
edges = cv2.Canny(image, 100, 200)
edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2RGB)  # 3‑channel for pipeline
edges = torch.from_numpy(edges).unsqueeze(0).permute(0, 3, 1, 2) / 255.0

prompt = "a futuristic city skyline at sunset"
output = pipe(prompt, image=edges, num_inference_steps=30)
output.images[0].save("generated.png")
```

In this snippet, the edge map steers the diffusion process, yielding an image that follows the supplied structure while preserving the artistic style of the base model.
