# Squeeze-and-Excitation Blocks

**Category:** Deep Learning  
**Date:** 2026-10-09 (morning)

---

# Squeeze-and-Excitation (SE) Blocks

**Concept**  
Squeeze‑and‑Excitation (SE) blocks are a lightweight architectural unit that adaptively recalibrates channel‑wise feature responses. They consist of two operations:  

1. **Squeeze** – Global average pooling compresses each channel’s spatial map into a single descriptor, capturing global context.  
2. **Excitation** – A small bottleneck MLP (usually two fully‑connected layers with a reduction ratio *r*) learns channel‑wise weights, followed by a sigmoid activation.  

The resulting scaling factors are multiplied back onto the original feature map, emphasizing informative channels and suppressing less useful ones.

**Why / Where Used**  
- **Improving representational power** of convolutional networks without a large parameter increase.  
- Integrated into many backbone models (ResNet‑SE, MobileNetV3, EfficientNet) to boost accuracy on image classification, detection, and segmentation tasks.  
- Helpful when model size or latency is constrained, because the overhead is modest (≈ 0.1 % of FLOPs).  

**Simple PyTorch Implementation**

```python
import torch
import torch.nn as nn

class SEBlock(nn.Module):
    def __init__(self, channels, reduction=16):
        super().__init__()
        self.squeeze = nn.AdaptiveAvgPool2d(1)          # (B, C, 1, 1)
        self.excite  = nn.Sequential(
            nn.Linear(channels, channels // reduction, bias=False),
            nn.ReLU(inplace=True),
            nn.Linear(channels // reduction, channels, bias=False),
            nn.Sigmoid()
        )

    def forward(self, x):
        b, c, _, _ = x.size()
        y = self.squeeze(x).view(b, c)                 # (B, C)
        y = self.excite(y).view(b, c, 1, 1)            # (B, C, 1, 1)
        return x * y                                   # channel‑wise scaling

# Example usage inside a conv block
class ConvSEBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Conv2d(in_ch, out_ch, 3, padding=1)
        self.bn   = nn.BatchNorm2d(out_ch)
        self.relu = nn.ReLU(inplace=True)
        self.se   = SEBlock(out_ch)

    def forward(self, x):
        return self.se(self.relu(self.bn(self.conv(x))))
```

In practice, swapping a standard residual block with its SE‑augmented version often yields a 1–2 % top‑1 accuracy gain on ImageNet while adding negligible computational cost.

---
