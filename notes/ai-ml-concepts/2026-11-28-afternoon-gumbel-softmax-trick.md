# Gumbel-Softmax Trick

**Category:** AI/ML Concepts  
**Date:** 2026-11-28 (afternoon)

---

# Gumbel‑Softmax Trick  

The Gumbel‑Softmax (also called Concrete) distribution provides a differentiable approximation to sampling from a categorical distribution. By adding Gumbel noise to the logits and applying a softmax with a temperature parameter, we obtain a “soft” one‑hot vector that can be back‑propagated through. As the temperature → 0, the sample becomes indistinguishable from a true one‑hot draw.

**Why use it?**  
- Enables end‑to‑end training of models that involve discrete decisions (e.g., neural architecture search, hard attention, text generation) without resorting to REINFORCE‑style high‑variance gradients.  
- Keeps the stochastic nature of sampling while preserving gradient flow, making it suitable for variational autoencoders with discrete latent variables and for reinforcement‑learning‑free policy learning.

**Typical applications**  
- Neural Architecture Search (selecting operations).  
- Hard attention mechanisms in vision and NLP.  
- Discrete latent variable VAEs.

**Simple PyTorch example**

```python
import torch
import torch.nn.functional as F

def gumbel_softmax_sample(logits, tau=0.5):
    # Sample Gumbel noise
    gumbel = -torch.log(-torch.log(torch.rand_like(logits) + 1e-20) + 1e-20)
    y = logits + gumbel
    return F.softmax(y / tau, dim=-1)

logits = torch.randn(4)          # e.g., scores for 4 classes
soft_one_hot = gumbel_softmax_sample(logits, tau=0.7)
print(soft_one_hot)  # differentiable approximation of a one‑hot vector
```

When `tau` is lowered during training, the output sharpens, eventually yielding near‑exact categorical samples while still allowing gradient‑based optimization.
