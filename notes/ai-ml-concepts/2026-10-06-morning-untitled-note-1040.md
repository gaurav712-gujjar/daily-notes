# Untitled Note - 1040

**Category:** AI/ML Concepts  
**Date:** 2026-10-06 (morning)

---

# Dynamic Routing in Capsule Networks

Capsule Networks replace scalar neurons with *capsules*—vectors that encode both the presence of a feature and its instantiation parameters (pose, texture, etc.). **Dynamic routing** is the iterative agreement mechanism that decides how lower‑level capsules send their outputs to higher‑level capsules. Each lower capsule predicts the output of higher capsules via learned transformation matrices; the routing softmax coefficients are refined over a few iterations, strengthening connections where predictions agree.

**Why it matters:**  
- Preserves hierarchical relationships, improving viewpoint invariance.  
- Mitigates information loss caused by max‑pooling in CNNs.  
- Shows strong performance on tasks with overlapping objects (e.g., digit recognition, medical imaging).

**Typical use‑cases:**  
- Small‑to‑medium image classification where spatial hierarchies matter.  
- Explainable AI, since capsule activations can be visualized as pose vectors.  
- Few‑shot learning, leveraging richer feature representations.

**Simple PyTorch illustration (routing for one layer):**

```python
import torch
import torch.nn.functional as F

def squash(s):
    """Non‑linear squashing to keep vector length ≤ 1."""
    mag_sq = (s ** 2).sum(dim=-1, keepdim=True)
    scale = mag_sq / (1.0 + mag_sq)
    return scale * s / torch.sqrt(mag_sq + 1e-8)

def dynamic_routing(u_hat, num_iters=3):
    """
    u_hat: [batch, num_low, num_high, dim] predicted votes
    Returns: [batch, num_high, dim] capsule outputs
    """
    b = torch.zeros_like(u_hat[..., 0])          # routing logits
    for _ in range(num_iters):
        c = F.softmax(b, dim=2)                  # coupling coeffs
        s = (c.unsqueeze(-1) * u_hat).sum(dim=1) # weighted sum
        v = squash(s)                            # capsule output
        agreement = (u_hat * v.unsqueeze(1)).sum(dim=-1)
        b = b + agreement                         # update logits
    return v
```

The function receives the *prediction vectors* `u_hat` from lower capsules, iteratively ref
