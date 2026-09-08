# Stochastic Depth

**Category:** Deep Learning  
**Date:** 2026-09-08 (afternoon)

---

# Stochastic Depth (DropPath)

Stochastic Depth, also called **DropPath**, randomly skips whole residual blocks during training. Instead of dropping individual neurons (like Dropout), it bypasses an entire layer, forwarding the input unchanged. Mathematically, for a residual block output `y = x + F(x)`, the training forward pass becomes  

\[
y = x + \mathbf{b}\,F(x),\quad \mathbf{b}\sim\text{Bernoulli}(p)
\]

where `p` is the keep‑probability. At inference time all blocks are kept, so the full depth is used. This regularization mitigates over‑fitting in very deep networks (e.g., ResNets‑1000+), improves gradient flow, and reduces the effective depth on the fly, leading to faster convergence.

**When to use**  
- Very deep CNNs (ResNet, ResNeXt) where training becomes unstable.  
- Scenarios with limited data where over‑parameterization hurts.  
- Mobile/edge models: DropPath can be combined with other efficiency tricks (e.g., depthwise convolutions) for a better accuracy‑efficiency trade‑off.

**PyTorch example**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class StochasticDepth(nn.Module):
    def __init__(self, p: float):
        super().__init__()
        self.p = p  # keep probability

    def forward(self, x, residual):
        if not self.training:
            return x + residual
        if torch.rand(1).item() < self.p:
            return x + residual
        else:  # drop the residual branch
            return x

class Bottleneck(nn.Module):
    def __init__(self, in_ch, out_ch, stride=1, drop_prob=0.2):
        super().__init__()
        self.conv = nn.Conv2d(in_ch, out_ch, kernel_size=3, stride=stride, padding=1)
        self.bn = nn.BatchNorm2d(out_ch)
        self.drop = StochasticDepth(p=1-drop_prob)

    def forward(self, x):
        residual = F.relu(self.bn(self.conv(x)))
        out = self.drop(x, residual)
        return out
```

In this snippet, each `Bottleneck` block may bypass its convolutional path with probability `drop_prob` during training, while inference always uses the full residual connection.

---
