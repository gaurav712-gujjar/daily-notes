# ControlNet Conditioning

**Category:** Generative AI  
**Date:** 2026-10-22 (afternoon)

---

# ControlNet Conditioning for Diffusion Models  

ControlNet is a plug‑and‑play neural network that augments a pre‑trained diffusion model (e.g., Stable Diffusion) with additional conditioning signals such as edges, depth maps, pose keypoints, or segmentation masks. It learns a *zero‑rank* copy of the original model’s weights and a small set of trainable “control” blocks that inject the extra information without disturbing the base generative capabilities. Because the backbone remains frozen, training is fast and data‑efficient, enabling users to steer image synthesis toward precise layouts while retaining the high fidelity of the original diffusion model.  

**Practical uses**  
- **Image‑to‑image editing**: give a rough sketch (Canny edges) and let ControlNet generate a photorealistic version.  
- **Pose‑guided generation**: feed human pose keypoints to create characters in exact stances.  
- **Depth‑aware synthesis**: use a depth map to maintain consistent geometry across frames in video generation.  

**Minimal example (🤗 Diffusers)**  

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch, cv2

# Load pretrained ControlNet (Canny edge version) and base Stable Diffusion
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
edges = torch.from_numpy(edges).unsqueeze(0).unsqueeze(0) / 255.0

prompt = "A futuristic cityscape at sunset, ultra‑realistic"
output = pipe(prompt, image=edges, num_inference_steps=30, guidance_scale=7.5)
output.images[0].save("generated.png")
```

The snippet shows how a single line of code swaps in a ControlNet branch, letting the same diffusion model respect the supplied edge map while preserving its original artistic style.
