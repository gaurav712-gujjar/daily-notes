# Untitled Note - 1126

**Category:** Generative AI  
**Date:** 2026-11-04 (morning)

---

# Neural Radiance Fields (NeRF)

NeRF is a continuous 3‑D scene representation that learns a volumetric radiance field from a sparse set of posed images. By training a multilayer perceptron (MLP) to map 3‑D coordinates + view direction → color + density, NeRF can synthesize novel views with photorealistic geometry and view‑dependent effects. The core idea is differentiable volume rendering: the network’s output is integrated along camera rays to match the observed pixel colors, and gradients flow back to adjust the MLP parameters.

**Why it matters**  
- **Novel view synthesis**: Generate unseen camera angles for AR/VR, virtual tours, or movie VFX.  
- **3‑D asset creation**: Turn a handful of photos into a compact, editable 3‑D model without explicit mesh reconstruction.  
- **Scene understanding**: The learned density field implicitly encodes geometry, useful for downstream tasks like depth estimation.

**Typical workflow**  
1. Capture a set of RGB images with known camera poses (e.g., using COLMAP).  
2. Train the NeRF MLP by minimizing the photometric loss between rendered and real pixels.  
3. Render novel views by sampling rays from a new camera pose and performing volume rendering.

**Tiny PyTorch example (simplified)**

```python
import torch, torch.nn as nn, numpy as np

class NeRF(nn.Module):
    def __init__(self, D=8, W=256):
        super().__init__()
        layers = [nn.Linear(3 + 3, W), nn.ReLU()]  # xyz + view_dir
        for _ in range(D-1):
            layers += [nn.Linear(W, W), nn.ReLU()]
        self.net = nn.Sequential(*layers)
        self.rgb = nn.Linear(W, 3)
        self.sigma = nn.Linear(W, 1
