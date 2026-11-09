# Untitled Note - 2056

**Category:** Machine Learning  
**Date:** 2026-11-09 (afternoon)

---

# Mish Activation Function

The **Mish** activation is a smooth, non‑monotonic function defined as  

\[
\text{Mish}(x)=x\cdot\tanh(\ln(1+e^{x}))
\]

It combines the benefits of **ReLU** (unbounded positive side) and **Swish** (smoothness) while retaining a self‑regularizing property that helps gradient flow for negative inputs. The function is continuously differentiable, which can lead to better optimization dynamics and improved feature representation.

### When to Use Mish
- **Computer Vision** models (e.g., ResNet, EfficientNet) where deeper networks suffer from vanishing gradients.
- **Natural Language Processing** transformers that benefit from smoother activation landscapes.
- Scenarios where **training stability** and **generalization** are critical, especially with limited data or noisy labels.

Empirical studies show Mish often yields modest accuracy gains over ReLU/Swish on image classification benchmarks, at the cost of a slightly higher compute overhead due to the `tanh` and `softplus` operations.

### PyTorch Example

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class Mish(nn.Module):
    def forward(self, x):
        return x * torch.tanh(F.softplus(x))

# Simple CNN block using Mish
class ConvBlock(nn.Module):
    def __init__(self, in_ch, out_ch):
        super().__init__()
        self.conv = nn.Conv2d(in_ch, out_ch, kernel_size=3, padding=1)
        self.act = Mish()
        self.bn
