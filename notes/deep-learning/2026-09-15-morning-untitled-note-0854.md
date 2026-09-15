# Untitled Note - 0854

**Category:** Deep Learning  
**Date:** 2026-09-15 (morning)

---

# Squeeze-and-Excitation Block

The **Squeeze-and-Excitation (SE) block** is a lightweight architectural unit that adaptively recalibrates channel‑wise feature responses. It consists of two steps:

1. **Squeeze** – Global average pooling compresses each channel’s spatial information into a single descriptor.  
2. **Excitation** – A small two‑layer bottleneck (usually a reduction ratio *r* = 16) learns non‑linear channel dependencies and outputs scaling factors via a sigmoid activation.

The original feature map **X** ∈ ℝ^{H×W×C} is multiplied channel‑wise by the learned weights **s** ∈ ℝ^{C}, yielding the refined output **X' = X ⊙ s**. This simple gating mechanism boosts representational power with minimal overhead.

### When to use it
- **Image classification**: SE‑ResNet and SE‑MobileNet achieve higher accuracy on ImageNet with negligible parameter increase.  
- **Object detection / segmentation**: Adding SE blocks to backbone networks improves feature discrimination for downstream heads.  
- **Any CNN‑based model** where channel inter‑dependencies are under‑exploited, especially on resource‑constrained devices.

### PyTorch example

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
        y = self.squeeze(x).view(b, c)          # Squeeze
        y = self.excite(y).view(b, c, 1, 1)      # Excitation
        return x * y.expand_as(x)               # Scale

# Usage inside a Conv block
class ConvSE(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
