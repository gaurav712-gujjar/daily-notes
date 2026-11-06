# Untitled Note - 1122

**Category:** Deep Learning  
**Date:** 2026-11-06 (morning)

---

# Mixup Data Augmentation

Mixup is a simple yet powerful data‑augmentation technique that creates new training samples by taking a convex combination of two random examples and their labels. Formally, given two inputs \\((x_i, y_i)\\) and \\((x_j, y_j)\\), a mixed sample is  

\[
\tilde{x}= \lambda x_i + (1-\lambda) x_j,\quad
\tilde{y}= \lambda y_i + (1-\lambda) y_j,
\]

where \\(\lambda \sim \text{Beta}(\alpha, \alpha)\\) and \\(\alpha > 0\\) controls the strength of mixing. The resulting label is a soft target, encouraging the model to behave linearly between training points, which improves robustness and generalization.

### When to use it
- **Image classification** pipelines where over‑fitting is a risk.  
- **Small‑to‑medium datasets** that benefit from richer training distributions.  
- Scenarios requiring **smooth decision boundaries**, such as adversarial‑defense research.  

Mixup works well with standard architectures (ResNet, EfficientNet) and can be combined with other augmentations (random crop, color jitter).

### PyTorch example

```python
import torch
import torch.nn.functional as F
import numpy as np

def mixup_data(x, y, alpha=0.4):
    """Return mixed inputs, pairs of targets, and lambda."""
    lam = np.random.beta(alpha, alpha)
    batch_size = x.size(0)
    index = torch.randperm(batch_size)

    mixed_x = lam * x + (1 - lam) * x[index, :]
    y_a, y_b = y
