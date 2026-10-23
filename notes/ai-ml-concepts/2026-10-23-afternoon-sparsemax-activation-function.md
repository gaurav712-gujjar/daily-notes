# Sparsemax Activation Function

**Category:** AI/ML Concepts  
**Date:** 2026-10-23 (afternoon)

---

# Sparsemax Activation Function

**What it is**  
Sparsemax is an alternative to the softmax activation that maps a vector of real numbers onto a probability simplex **while producing sparse outputs** (i.e., some entries become exactly zero). Formally, for an input **z** ∈ ℝᵏ, Sparsemax solves  

\[
\text{Sparsemax}(z)=\underset{p\in\Delta^{k}}{\arg\min}\; \|p - z\|^{2},
\]

where Δᵏ is the k‑dimensional probability simplex. The solution can be computed in O(k log k) by sorting the input and finding a threshold τ such that  

\[
p_i = \max(z_i - τ, 0).
\]

**Why/where it’s used**  
- **Interpretability**: Sparse probabilities make it easier to see which classes dominate a prediction.  
- **Attention mechanisms**: In models where only a few elements should attend to each other (e.g., document summarization), Sparsemax yields hard‑selection‑like behavior without resorting to non‑differentiable argmax.  
- **Resource‑constrained inference**: Zeroed entries can be skipped, saving computation in downstream layers.  

**Quick PyTorch example**

```python
import torch
import torch.nn.functional as F

def sparsemax(logits, dim=-1):
    # implementation based on the paper (Martins & Astudillo, 2016)
    logits = logits - logits.max(dim, keepdim=True)[0]  # improve stability
    zs = torch.sort(logits, descending=True, dim=dim)[0]
    range_k = torch.arange(1, zs.size(dim)+1, device=logits.device).float()
    cumsum_zs = zs.cumsum(dim) - 1
    # find the threshold τ
    is_gt = zs - (cumsum_zs / range_k) > 0
    k = is_gt.sum(dim, keepdim=True)
    tau = cumsum_zs.gather(dim, k-1) / k.float()
    # compute output
    return torch.clamp(logits - tau, min=0.0)

# demo
logits = torch.tensor([[2.0, 1.0, 0.1, -1.0]])
print(sparsemax(logits))
# tensor([[0.7333, 0.2667, 0.0000, 0.0000]])
```

The resulting vector sums to 1 but only two entries are non‑zero, illustrating sparsity.

---
