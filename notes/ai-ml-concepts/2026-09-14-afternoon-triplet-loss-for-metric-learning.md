# Triplet Loss for Metric Learning

**Category:** AI/ML Concepts  
**Date:** 2026-09-14 (afternoon)

---

# Triplet Loss for Metric Learning

Triplet loss is a training objective that encourages an embedding model to place samples of the same class close together while pushing samples of different classes apart. Each training step uses a **triplet**: an anchor \(a\), a positive example \(p\) (same class as the anchor), and a negative example \(n\) (different class). The loss enforces the margin condition  

\[
\|f(a)-f(p)\|_2^2 + \alpha \;<\; \|f(a)-f(n)\|_2^2,
\]

where \(f(\cdot)\) is the embedding function and \(\alpha\) is a margin hyper‑parameter. If the inequality is violated, the loss is proportional to the shortfall, otherwise it is zero.

### Why use it?
- **Face verification & recognition:** embeddings that cluster faces of the same person improve matching without a separate classifier.
- **Product search / retrieval:** learns a space where visually or semantically similar items are near each other, enabling nearest‑neighbor queries.
- **Zero‑shot learning:** a well‑structured embedding can be used with simple similarity metrics for classes unseen during training.

### Practical tips
- **Hard‑negative mining:** selecting negatives that are close to the anchor accelerates convergence.
- **Batch‑all vs. batch‑hard:** compute loss over all possible triplets in a batch (more stable) or only the hardest ones (faster but riskier).
- **Embedding normalization:** L2‑normalize vectors before computing distances to keep the scale consistent.

### Minimal PyTorch example
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class SimpleEmbedder(nn.Module):
    def __init__(self, out_dim=128):
        super().__init__()
        self.net = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28*28, 256),
            nn.ReLU(),
            nn.Linear(256, out_dim)
        )
    def forward(self, x):
        return F.normalize(self.net(x), p=2, dim=1)   # L2‑norm

def triplet_loss(anchor, positive, negative, margin=0.2):
    d_ap = F.pairwise_distance(anchor, positive, p=2)
    d_an = F.pairwise_distance(anchor, negative, p=2)
    loss = F.relu(d_ap - d_an + margin)
    return loss.mean()
```
The model learns to map images into a space where the Euclidean distance reflects semantic similarity, driven solely by the triplet loss.
