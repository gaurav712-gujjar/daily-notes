# Untitled Note - 1843

**Category:** Machine Learning  
**Date:** 2026-11-20 (afternoon)

---

# Sharpness‑Aware Minimization (SAM)

Sharpness‑Aware Minimization is an optimizer augmentation that seeks model parameters lying in flat regions of the loss landscape. Instead of minimizing the loss at the current point θ, SAM first perturbs θ in the direction that **maximizes** the loss within a bounded ℓ₂‑ball (radius ρ), then updates θ to reduce this worst‑case loss. Formally:

\[
\min_{\theta}\; \max_{\|\epsilon\|\le\rho} \; L(\theta + \epsilon)
\]

Flat minima are empirically linked to better generalization because small parameter changes (e.g., due to data noise or distribution shift) cause little loss increase.

### When to use SAM
- **Computer vision** models trained on limited data where over‑fitting is a risk.  
- **Natural language processing** fine‑tuning of large pre‑trained transformers.  
- Any deep‑learning pipeline where the default optimizer (Adam/SGD) yields high training accuracy but lower validation performance.

### Quick PyTorch example

```python
import torch, torch.nn as nn, torch.optim as optim
from torch.nn.utils import clip_grad_norm_

class SAM(optim.Optimizer):
    def __init__(self, base_optimizer, rho=0.05, adaptive=False):
        self.base_optimizer = base_optimizer
        self.rho = rho
        self.adaptive = adaptive
        defaults = dict(rho=rho, adaptive=adaptive)
        super().__init__(base_optimizer.param_groups, defaults)

    @torch.no_grad()
    def step(self, closure):
        # 1️⃣ first forward‑backward pass
        loss = closure()
        loss.backward()
        grad_norm = self._grad_norm()
        # 2️⃣ ascent step
        epsilon = [(self.rho / (grad_norm + 1e-12)) * p.grad
                   for p in self.base_optimizer.param_groups[0]['params']]
        for p, e in zip(self.base_optimizer.param_groups[0]['params'], epsilon):
            p.add_(e)               # θ + ε
        # 3️⃣ second forward‑backward pass
        loss_adv =
