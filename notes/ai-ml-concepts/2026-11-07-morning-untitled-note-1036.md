# Untitled Note - 1036

**Category:** AI/ML Concepts  
**Date:** 2026-11-07 (morning)

---

# Mixup Data Augmentation

**What it is**  
Mixup creates synthetic training examples by taking a convex combination of two random samples and their labels. For inputs *x₁, x₂* and one‑hot targets *y₁, y₂*, a new example is  

\[
\tilde{x}= \lambda x_1 + (1-\lambda) x_2,\qquad
\tilde{y}= \lambda y_1 + (1-\lambda) y_2,
\]

where λ ∈ [0,1] is drawn from a Beta(α, α) distribution (α > 0). The model learns to predict soft targets, encouraging linear behavior between classes.

**Why use it?**  
- **Regularization:** Reduces over‑fitting by smoothing the decision boundary.  
- **Robustness:** Improves resistance to adversarial perturbations and noisy labels.  
- **Calibration:** Leads to better‑calibrated probabilities because the model sees intermediate label mixtures.  
Typical in image classification (e.g., CIFAR‑10/100, ImageNet) and increasingly in speech or text tasks.

**Simple PyTorch implementation**

```python
import torch
import torch.nn.functional as F

def mixup_data(x, y, alpha=0.4):
    """Return mixed inputs, pairs of targets, and lambda."""
    if alpha > 0:
        lam = torch.distributions.Beta(alpha, alpha).sample().item()
    else:
        lam = 1.0

    batch_size = x.size(0)
    index = torch.randperm(batch_size)

    mixed_x = lam * x + (1 - lam) * x[index, :]
    y_a, y_b = y, y[index]
    return mixed_x, y_a, y_b, lam

def mixup_criterion(criterion, pred, y_a, y_b, lam):
    return lam * criterion(pred, y_a) + (1 - lam) * criterion(pred, y_b)

# usage inside training loop
inputs, targets = batch
inputs, targets_a, targets_b, lam = mixup_data(inputs, targets)
outputs = model(inputs)
loss = mix
