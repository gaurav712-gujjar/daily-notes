# Untitled Note - 2027

**Category:** Deep Learning  
**Date:** 2026-11-02 (afternoon)

---

# Dynamic Routing in Capsule Networks

Capsule Networks (CapsNets) replace scalar neurons with *capsules*—vectors that encode both the probability of an entity’s presence and its pose (orientation, scale, etc.). The core operation is **dynamic routing by agreement**, an iterative process that routes lower‑level capsule outputs to higher‑level capsules whose predictions agree the most. Unlike max‑pooling, routing preserves spatial hierarchies and is equivariant to viewpoint changes.

**Why use it?**  
- **Robustness to affine transformations**: Pose information lets the model recognize objects even when they appear rotated or scaled.  
- **Reduced need for data augmentation**: The network learns transformation invariance internally.  
- **Interpretability**: Each capsule’s vector can be inspected to infer pose parameters.

**Typical applications**  
- Handwritten digit recognition (original MNIST experiments).  
- 3‑D object classification and medical imaging where spatial relationships matter.

**Simple PyTorch example (single routing iteration)**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class PrimaryCaps(nn.Module):
    def __init__(self, in_channels, out_caps, cap_dim, kernel=9, stride=2):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_caps * cap_dim,
                              kernel_size=kernel, stride=stride)
        self.out_caps, self.cap_dim = out_caps, cap_dim

    def forward(self, x):
        u = self.conv(x)                     # [B, out_caps*cap_dim, H, W]
