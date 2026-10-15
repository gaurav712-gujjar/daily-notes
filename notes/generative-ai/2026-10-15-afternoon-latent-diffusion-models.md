# Latent Diffusion Models

**Category:** Generative AI  
**Date:** 2026-10-15 (afternoon)

---

# Latent Diffusion Models (LDM)

Latent Diffusion Models move the diffusion process from pixel‑space to a compact latent space learned by an autoencoder. An encoder compresses high‑resolution images into low‑dimensional latents; diffusion (forward‑noising and reverse‑denoising) operates there, dramatically reducing memory and compute. A decoder then reconstructs the image from the denoised latent. Because the latent space captures semantic structure, LDMs can generate high‑quality, high‑resolution images with far fewer diffusion steps than pixel‑space models.

**Why use LDMs?**  
- **Efficiency:** Training and inference cost drop by 10‑20× compared to full‑resolution diffusion.  
- **Scalability:** Enables diffusion on 1024×1024 or larger images on modest GPUs.  
- **Flexibility:** Latent representations can be conditioned on text, segmentation maps, or depth, making LDMs a backbone for many multimodal generators (e.g., Stable Diffusion).

**Typical workflow**

```python
from diffusers import StableDiffusionPipeline
import torch

pipe = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16,
    revision="fp16"
).to("cuda")

prompt = "A futuristic cityscape at sunset, cinematic lighting"
image = pipe(prompt, num_inference_steps=30).images[0]
image.save("output.png")
```

The code loads a pretrained LDM (Stable Diffusion), runs only 30 denoising steps in latent space, and decodes the result to a high‑resolution image.

*Key takeaway:* By delegating diffusion to a learned latent manifold, LDMs make large‑scale generative modeling tractable without sacrificing visual fidelity.
