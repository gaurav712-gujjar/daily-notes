# Untitled Note - 0916

**Category:** Generative AI  
**Date:** 2026-10-26 (morning)

---

# DDIM Sampling Technique

Denoising Diffusion Implicit Models (DDIM) provide a deterministic, non‑Markovian sampler for diffusion models. While the original Denoising Diffusion Probabilistic Model (DDPM) generates samples by iteratively applying a stochastic reverse‑diffusion process, DDIM re‑parameterizes the transition so that the same latent trajectory can be traversed with fewer steps and without random noise injection. This yields **faster generation** and **more controllable** outputs, making it popular for real‑time image synthesis and latent space exploration.

**Practical uses**
- **Speed‑up**: Reducing inference steps from 1000 (DDPM) to ~50‑100 while preserving visual quality.
- **Deterministic editing**: Because the path is fixed, the same seed produces identical results, useful for reproducible image editing.
- **Interpolation**: By moving along the deterministic trajectory, one can smoothly interpolate between latent codes.

**Minimal PyTorch example**

```python
import torch, torch.nn as nn
from diffusers import DDPMScheduler, UNet2DModel, DDIMScheduler

# Load a pretrained diffusion UNet (e.g., from HuggingFace)
unet =
