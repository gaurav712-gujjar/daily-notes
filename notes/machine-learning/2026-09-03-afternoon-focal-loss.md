# Focal Loss

**Category:** Machine Learning  
**Date:** 2026-09-03 (afternoon)

---

# Focal Loss

Focal Loss is a modification of the standard cross‑entropy loss designed to address class imbalance in dense prediction tasks such as object detection. It introduces a modulating factor *(1‑pₜ)^γ* that down‑weights easy, well‑classified examples (where the predicted probability *pₜ* is high) and focuses learning on hard, mis‑classified samples. The loss formula is:

\[
\text{FL}(p_t) = -\alpha \,(1-p_t)^\gamma \log(p_t)
\]

- **α** balances the importance of positive/negative classes.  
- **γ** (gamma) controls the strength of down‑weighting; γ = 0 reduces to ordinary cross‑entropy.

**Why use it?**  
In datasets where background examples vastly outnumber foreground objects (e.g., detecting rare objects in images), standard cross‑entropy causes the model to be dominated by easy negatives, leading to poor recall on the minority class. Focal Loss mitigates this by emphasizing the few hard positives, yielding higher precision/recall without extra sampling tricks.

**Practical applications**  
- RetinaNet object detector (the paper that introduced it).  
- Medical image segmentation where lesions are tiny compared to healthy tissue.  
- Any binary/multi‑class problem with severe imbalance.

**PyTorch example**

```python
import torch
import torch.nn as nn

class FocalLoss(nn.Module):
    def __init__(self, alpha=0.25, gamma=2.0, reduction='mean'):
        super().__init__()
        self.alpha = alpha
        self.gamma = gamma
        self.reduction = reduction
        self.ce = nn.BCEWithLogitsLoss(reduction='none')

    def forward(self, logits, targets):
        # BCE loss per element
        bce_loss = self.ce(logits, targets)
        prob = torch.sigmoid(logits)
        pt = prob * targets + (1 - prob) * (1 - targets)   # p_t
        loss = self.alpha * (1 - pt).pow(self.gamma) * bce_loss
        return loss.mean() if self.reduction == 'mean' else loss.sum()

# usage
logits = torch.randn(8, 1)
labels = torch.randint(0, 2, (8, 1)).float()
loss = FocalLoss()(logits, labels)
loss.backward()
```

This implementation can be swapped for `nn.BCEWithLogitsLoss` in any binary classification pipeline to improve performance on imbalanced data.
