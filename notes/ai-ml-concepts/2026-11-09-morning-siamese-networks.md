# Siamese Networks

**Category:** AI/ML Concepts  
**Date:** 2026-11-09 (morning)

---

# Siamese Networks

A **Siamese network** is a neural architecture that processes two (or more) inputs through identical subnetworks sharing weights, producing embeddings that can be compared using a distance metric. The core idea is to learn a representation space where similar items are close together while dissimilar ones are far apart. Training typically uses a contrastive loss (or triplet loss) that penalizes large distances for matching pairs and small distances for mismatched pairs.

**Why it’s used**  
- **One‑shot / few‑shot learning**: By learning a similarity function, the model can classify new classes from a single example.  
- **Verification tasks**: Face verification, signature verification, and duplicate detection rely on measuring similarity rather than explicit class labels.  
- **Metric learning**: Embeddings can be reused for downstream tasks such as clustering or retrieval.

**Simple PyTorch example**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class Twin(nn.Module):
    def __init__(self):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(1, 32, 5), nn.ReLU(),
            nn.MaxPool2d(2),
            nn.Conv2d(32, 64, 5), nn.ReLU(),
            nn.MaxPool2d(2)
        )
        self.fc = nn.Linear(64 * 4 * 4, 128)

    def forward(self, x):
        x = self.conv(x)
        x = x.view(x.size(0), -1)
        return self.fc(x)

class Siamese(nn.Module):
    def __init__(self):
        super().__init__()
        self.twin = Twin()

    def forward(self, img1, img2):
        out1, out2 = self.twin(img1), self.twin(img2)
        # Euclidean distance between embeddings
        return F.pairwise_distance(out1, out2)

# contrastive loss
def contrastive_loss(dist, label, margin=1.0):
    return torch.mean(label * dist.pow(2) +
                      (1 - label) * F.relu(margin - dist).pow(2))
```

In practice, you feed pairs of images (or other data) with a binary label indicating whether they belong to the same class. The network learns a space where the distance aligns with that label, enabling efficient similarity queries at inference time.
