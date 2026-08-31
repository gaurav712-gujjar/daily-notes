# Classifier-Free Guidance

**Category:** Generative AI  
**Date:** 2026-08-31 (afternoon)

---

# Classifier‑Free Guidance in Diffusion Models  

Classifier‑free guidance (CFG) is a technique for steering conditional diffusion samplers without training an external classifier. During training the diffusion model receives a conditioning signal (e.g., a text prompt) **and** a null conditioning (often an empty token). At inference time the model is queried twice: once with the true condition *c* and once with the null condition *null*. The two predicted noise terms ε(c) and ε(null) are combined as  

\[
\hat\epsilon = \epsilon(\text{null}) + w \bigl(\epsilon(c) - \epsilon(\text{null})\bigr)
\]

where *w* (the guidance scale) amplifies the influence of the condition. When *w* = 1 the output is the original unconditional sample; larger *w* values yield images that more closely follow the prompt, at the cost of reduced diversity.

**Why it’s used**  
- **Simpler pipeline**: No separate classifier network is needed, saving memory and training effort.  
- **Fine‑grained control**: Adjusting *w* lets users trade off fidelity vs. creativity in real‑time.  
- **Broad applicability**: Works with any conditional diffusion model (text‑to‑image, image‑to‑image, inpainting).

**Example (using 🤗 Diffusers)**  

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda")

prompt = "a futuristic cityscape at sunset"
guidance_scale = 7.5   # classic CFG value

image = pipe(prompt, guidance_scale=guidance_scale).images[0]
image.save("cityscape.png")
```

The `guidance_scale` argument implements classifier‑free guidance under the hood, blending the conditioned and unconditional predictions.

---
