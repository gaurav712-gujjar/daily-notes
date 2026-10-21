# Denoising Diffusion Implicit Models

**Category:** Generative AI  
**Date:** 2026-10-21 (morning)

---

# Denoising Diffusion Implicit Models (DDIM)

DDIM is a sampling technique for diffusion generative models that trades off speed for fidelity.  
While the original Denoising Diffusion Probabilistic Model (DDPM) requires many (e.g., 1000) reverse‑diffusion steps, DDIM introduces a deterministic, non‑Markovian update rule that can generate high‑quality samples in as few as 10‑50 steps. The key idea is to view diffusion as solving an ordinary differential equation (ODE) in latent space; by discretizing this ODE with larger step sizes, DDIM retains most of the image quality while dramatically reducing inference time.

**Why it’s used**  
- **Fast inference** for real‑time applications (e.g., image editing, video generation).  
- **Consistent latent trajectories**, enabling latent space interpolation and controllable generation.  
- **Compatibility**: DDIM can be swapped into any pre‑trained diffusion model without retraining.

**Example (🤗 Diffusers)**  

```python
from diffusers import StableDiffusionPipeline, DDIMScheduler
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5", torch_dtype=torch.float16
).to("cuda")

# Replace the default scheduler with DDIM (10 steps)
pipe.scheduler = DDIMScheduler.from_config(pipe.scheduler.config)
pipe.scheduler.set_timesteps(10)

prompt = "a futuristic cityscape at sunset, ultra‑realistic"
image = pipe(prompt).images[0]
image.save("ddim_city.png")
```

The code loads a Stable Diffusion model, swaps in a DDIM scheduler, and generates an image in only ten diffusion steps, illustrating the speed‑quality trade‑off DDIM offers.

---
