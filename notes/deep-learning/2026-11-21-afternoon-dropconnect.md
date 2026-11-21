# DropConnect

**Category:** Deep Learning  
**Date:** 2026-11-21 (afternoon)

---

# DropConnect

**What it is**  
DropConnect is a regularization technique for neural networks that randomly zeroes out *individual weights* (connections) rather than entire activations as in standard Dropout. During each forward pass, a binary mask is sampled for the weight matrix \(W\); the effective weight becomes \(W \odot M\) where \(M\sim\text{Bernoulli}(p)\). At inference time the full weight matrix is used, typically scaled by the keep‑probability \(p\).

**Why / where it’s used**  
- **Improved generalization**: By perturbing the connectivity pattern, the model learns more robust feature detectors, especially in fully‑connected layers.  
- **Better performance on small datasets**: DropConnect can be more effective than Dropout when data is scarce, as it directly regularizes the parameter space.  
- **Architectural flexibility**: It can be applied to any layer with a weight matrix (e.g., linear, convolutional by treating each filter weight independently).  
- **Research**: Frequently appears in papers on model compression and Bayesian deep learning as a simple stochastic approximation to posterior inference.

**Simple PyTorch example**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class DropConnectLinear(nn.Module):
    def __init__(self, in_features, out_features, p=0.5):
        super().__init__()
        self.linear = nn.Linear(in_features, out_features)
        self.p = p

    def forward(self, x):
        if self.training:
            mask = torch.bernoulli(torch.full_like(self.linear.weight, 1 - self.p))
            weight = self.linear.weight * mask
            return F.linear(x, weight, self.linear.bias)
        else:
            # scale weights at test time
            return self.linear(x)

# usage
layer = DropConnectLinear(128, 64, p=0.3)
output = layer(torch.randn(32, 128))
```

The mask is regenerated each training step, giving a different sub‑network each pass while keeping the original parameter set for inference.
