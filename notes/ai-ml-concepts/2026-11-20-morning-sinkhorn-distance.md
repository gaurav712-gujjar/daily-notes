# Sinkhorn Distance

**Category:** AI/ML Concepts  
**Date:** 2026-11-20 (morning)

---

# Sinkhorn Distance (Entropic Regularized Optimal Transport)

The **Sinkhorn distance** is a computationally efficient approximation of the classic optimal transport (OT) problem. By adding an entropic regularization term to the transport cost matrix, the problem becomes strictly convex and can be solved with the iterative **Sinkhorn‑Knopp** matrix scaling algorithm. The resulting distance retains many desirable properties of the Wasserstein metric while being differentiable and fast to compute (≈ O(n²) per iteration).

**Why it matters**  
- **Domain adaptation & generative modeling**: Aligning feature distributions between source and target domains.  
- **Deep learning losses**: Used as a differentiable loss (e.g., in **Wasserstein GANs**, **optimal transport embeddings**, or **point cloud registration**).  
- **Clustering & barycenters**: Computing Wasserstein barycenters for aggregating distributions.  
- **Scalability**: The entropic term enables GPU‑accelerated matrix operations, making it viable for large‑scale datasets where exact OT would be prohibitive.

**Basic Python example (PyTorch)**  

```python
import torch

def sinkhorn_distance(x, y, eps=0.1, n_iter=100):
    """Compute Sinkhorn distance between two point clouds x, y.
    x, y: (N, d) tensors
    eps: entropic regularization strength
    """
    C = torch.cdist(x, y, p=2) ** 2               # squared Euclidean cost
    K = torch.exp(-C / eps)                       # kernel matrix
    a = torch.full((x.size(0),), 1.0 / x.size(0), device=x.device)
    b = torch.full((y.size(0),), 1.0 / y.size(0), device=y.device)

    u = torch.ones_like(a)
    v = torch.ones_like(b)
    for _ in range(n_iter):
        u = a / (K @ v)
        v = b / (K.t() @ u)

    transport = torch.diag(u) @ K @ torch.diag(v)
    return torch.sum(transport * C)

# Example usage
x = torch.randn(128, 2)   # source points
y = torch.randn(128, 2)   # target points
dist = sinkhorn_distance(x, y)
print(f"Sinkhorn distance ≈ {dist.item():.4f}")
```

The function computes a differentiable distance that can be plugged directly into neural‑network training loops, enabling end‑to‑end learning of distribution‑matching objectives.

---
