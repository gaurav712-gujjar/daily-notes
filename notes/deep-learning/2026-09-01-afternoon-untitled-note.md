# Untitled Note

**Category:** Deep Learning  
**Date:** 2026-09-01 (afternoon)

---

# Stochastic Depth (DropPath)

Stochastic Depth is a regularization technique for very deep residual networks. During training, each residual block is randomly **skipped** with a predefined probability, effectively shortening the network on that forward/backward pass. The skipped block’s output is replaced by its input (the identity shortcut). At inference time, all blocks are active, and the learned weights are used unchanged.

**Why use it?**  
- Mitigates the vanishing‑gradient problem in ultra‑deep models (e.g., ResNet‑101+).  
- Acts like an ensemble of networks of varying depths, improving generalization without extra parameters.  
- Reduces training time per epoch because fewer layers are evaluated on average.

**Typical settings**  
- Survival probability \(p_l = 1 - \frac{l}{L}(1-p_0)\), where \(l\) is the block index, \(L\) total blocks, and \(p_0\) the final survival rate (e.g., 0.5).  
- Applied only to **training**; inference uses the full depth.

**PyTorch example**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class StochasticDepth(nn.Module):
    def __init__(self, survival_prob):
        super().__init__()
        self.survival_prob = survival_prob

    def forward(self, x, residual):
        if not self.training:
            return x + residual
        # Bernoulli mask
        mask = torch.rand(x.shape[0], 1, 1, 1, device=x.device) < self.survival_prob
        mask = mask.type_as(x)
        return x + residual * mask / self.survival_prob   # rescale to keep expectation unchanged

class ResidualBlock(nn.Module):
    def __init__(self, in_ch, out_ch, survival_prob):
        super().__init__()
        self.conv = nn.Conv2d(in
