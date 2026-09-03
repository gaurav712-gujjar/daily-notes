# Untitled Note - 0814

**Category:** Generative AI  
**Date:** 2026-09-03 (afternoon)

---

# ControlNet Conditional Generation

**Concept**  
ControlNet augments a pretrained diffusion model (e.g., Stable Diffusion) with an extra “conditioning” branch that injects spatial guidance—such as edges, pose maps, depth, or segmentation masks—while keeping the original model weights frozen. The extra branch learns a lightweight mapping from the guidance map to the latent space, enabling fine‑grained control over the generated image without retraining the whole diffusion network.

**Why / Where It’s Used**  
- **Creative workflows**: Artists can sketch a contour or pose and let the model fill in photorealistic details.  
- **Content creation pipelines**: Generate consistent characters or objects across frames by feeding pose sequences.  
- **Domain‑specific synthesis**: Medical imaging can be guided by anatomical masks to produce realistic yet controllable scans.  
- **Rapid prototyping**: Designers iterate by swapping simple maps (edge → depth) while preserving style.

**Quick Example (using 🤗 Diffusers)**  

```python
from diffusers import StableDiffusionControlNetPipeline, ControlNetModel
import torch, cv2

# Load pretrained ControlNet for Canny edge maps
controlnet = ControlNetModel.from_pretrained(
    "lllyasviel/sd-controlnet-canny", torch_dtype=torch.float16
)
pipe = StableDiffusionControlNetPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    controlnet=controlnet,
    torch_dtype=torch.float16,
).to("cuda")

# Prepare edge map (Canny)
image = cv2.imread("portrait.jpg")
canny = cv2.Canny(image, 100, 200)
canny = cv2.cvtColor(canny, cv2.COLOR_GRAY2RGB)  # 3‑channel for pipeline
canny = torch.from_numpy(canny).permute(2, 0, 1).unsqueeze(0) / 255.0

prompt = "A portrait of a medieval knight,
