# Untitled Note - 1653

**Category:** Deep Learning  
**Date:** 2026-10-06 (afternoon)

---

# Squeeze‑and‑Excitation Block

The **Squeeze‑and‑Excitation (SE) block** is a lightweight attention module that adaptively recalibrates channel‑wise feature responses. It consists of two operations:

1. **Squeeze** – Global average pooling compresses each channel’s spatial information into a single descriptor (a vector of length *C*).  
2. **Excitation** – Two fully‑connected layers form a bottleneck (typically reduction ratio *r* = 16), apply a non‑linearity, and generate channel‑wise weights via a sigmoid.  

The original feature map *X* (shape *N × C × H × W*) is multiplied element‑wise by the learned weights, emphasizing informative channels and suppressing redundant ones.

### Why use SE blocks?

- **Performance boost** – Adding SE modules to classic architectures (ResNet, MobileNet, EfficientNet) consistently improves top‑1 accuracy with minimal extra parameters (< 1 %).  
- **Model‑agnostic** – SE can be inserted after any convolutional block, making it a plug‑and‑play upgrade.  
- **Computationally cheap** – Only a few dense layers and a global pooling operation; negligible impact on FLOPs, ideal for mobile or edge devices.

### Simple PyTorch example

```python
import torch
import torch.nn as nn

class SEBlock(nn.Module):
    def __init__(self, channels, reduction=16):
        super().__init__()
        self.squeeze = nn.AdaptiveAvgPool2d(1)
        self.excite = nn.Sequential(
            nn.Linear(channels, channels // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channels // reduction, channels, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.squeeze(x).view(b, c)          # (N, C)
        y = self.excite(y).view(b, c, 1, 1)      # (N, C, 1, 1)
        return x * y.expand_as(x)               # channel‑wise scaling

# usage inside a residual block
class ResSEBlock(nn.Module):
    def __init__(self
