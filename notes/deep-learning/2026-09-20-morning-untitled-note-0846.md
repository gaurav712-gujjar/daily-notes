# Untitled Note - 0846

**Category:** Deep Learning  
**Date:** 2026-09-20 (morning)

---

# Spectral Normalization

Spectral Normalization (SN) is a weight‑scaling technique that controls the Lipschitz constant of a neural network layer by normalizing its weight matrix with its largest singular value (spectral norm). Unlike standard weight decay, SN directly limits how much the output can change relative to the input, stabilizing training especially for adversarial setups.

**Why it matters**  
- **GAN training**: Prevents the discriminator from becoming overly sharp, reducing mode collapse and improving convergence.  
- **Robustness**: Enforces smoother functions, which helps in defending against adversarial attacks.  
- **Generalization**: By constraining capacity, SN can act as an implicit regularizer for deep nets.

**How it works**  
Given a weight matrix \(W\), compute its dominant singular value \(\sigma(W)\) via power iteration, then replace the weight with \(\hat{W}=W / \sigma(W)\). The operation is cheap (a few iterations) and can be applied per layer.

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SNLinear(nn.Module):
    def __init__(self, in_dim, out_dim, n_power_iterations=1, eps=1e-12):
        super().__init__()
        self.weight = nn.Parameter(torch.randn(out_dim, in_dim))
        self.bias = nn.Parameter(torch.zeros(out_dim))
        self.n_power_iterations = n_power_iterations
        self.eps = eps
        self.register_buffer('u', torch.randn(1, out_dim))

    def _spectral_norm(self, W):
        u = self.u
        for _ in range(self.n_power_iterations):
            v = F.normalize(torch.mm(u, W.t()), dim=1, eps=self.eps)
            u = F.normalize(torch.mm(v, W), dim=1, eps=self.eps)
        sigma = torch.mm(torch.mm(v, W), u.t())
        W_sn = W / sigma
        self.u = u.detach()
        return W_sn

    def forward(self, x):
        W_sn = self._spectral_norm(self.weight)
        return F.linear(x, W_sn, self.bias)
```

The `SNLinear` layer can replace standard `nn.Linear` in a discriminator to obtain more stable GAN training.

---
