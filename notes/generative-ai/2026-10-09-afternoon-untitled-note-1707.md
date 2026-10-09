# Untitled Note - 1707

**Category:** Generative AI  
**Date:** 2026-10-09 (afternoon)

---

# Classifier Guidance in Diffusion Models

Classifier guidance is a technique that steers the sampling process of a diffusion model toward a desired class by leveraging gradients from an external classifier. During generation, the diffusion model predicts the noise to remove at each timestep; the classifier provides a gradient ∂ log p(class | x) / ∂ x that nudges the intermediate image *x* toward higher likelihood under the target class. This yields higher-fidelity, class‑conditional samples without retraining the diffusion model itself.

**Why use it?**  
- **Zero‑shot conditioning:** Existing unconditional diffusion models can be repurposed for class‑conditional synthesis.  
- **Fine‑grained control:** Adjust the guidance strength (scale λ) to trade off realism vs. class adherence.  
- **Modularity:** The classifier can be swapped (e.g., CLIP, a ResNet) to target different semantic spaces.

**Typical workflow**  
1. Sample a noisy image `x_t` from the diffusion prior.  
2. Compute the diffusion model’s noise prediction `ε_θ(x_t, t)`.  
3. Obtain classifier gradient `grad = ∇_x log p(y|x_t)`.  
4. Modify the predicted noise: `ε̂ = ε_θ - λ * grad`.  
5. Perform the usual denoising step with `ε̂`.

```python
import torch, torch.nn.functional as F
from diffusers import DDPMScheduler, UNet2DModel

# pretrained diffusion and classifier (e.g., ResNet18)
unet = UNet2DModel.from_pretrained("google/ddpm-cifar10-32")
classifier = torch.hub.load('pytorch/vision:v0.10.0', 'resnet18', pretrained=True).eval()
scheduler = DDPMScheduler(num_train_timesteps=1000)

def classifier_guided_step(x, t, target_class, lambda_guidance=1.5):
    x.requires_grad_(True)
