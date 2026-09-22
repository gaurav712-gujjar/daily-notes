# Swish Activation Function

**Category:** Deep Learning  
**Date:** 2026-09-22 (afternoon)

---

# Swish Activation Function

The **Swish** activation, introduced by Google Brain, is defined as  
\[
\text{Swish}(x) = x \cdot \sigma(\beta x)
\]  
where σ is the sigmoid function and β is a trainable (or fixed) parameter, often set to 1. Unlike ReLU, Swish is smooth and non‑monotonic, allowing small negative values to pass through, which can improve gradient flow in deep nets.

**Why use Swish?**  
- **Better performance**: Empirically yields higher accuracy on image classification benchmarks (e.g., ImageNet) compared to ReLU or Leaky ReLU.  
- **Self‑gating**: The sigmoid term acts as a gate that adapts per‑unit, reducing the risk of dead neurons.  
- **Compatibility**: Can replace any ReLU layer without architectural changes and works with batch‑norm, dropout, etc.

**Typical use cases**  
- Vision models (e.g., EfficientNet, MobileNetV3) where a lightweight yet expressive activation is desired.  
- Deep residual or transformer blocks where preserving gradient magnitude is critical.  

**PyTorch example**

```python
import torch
import torch.nn as nn

class Swish(nn.Module):
    def __init__(self, beta=1.0):
        super().__init__()
        self.beta = nn.Parameter(torch.tensor(beta))

    def forward(self, x):
        return x * torch.sigmoid(self.beta * x)

# usage in a simple MLP
model = nn.Sequential(
    nn.Linear(784, 256),
    Swish(),
    nn.Linear(256, 10)
)
```

Swish can also be accessed directly via `torch.nn.SiLU`, which uses β = 1 by default.

---
