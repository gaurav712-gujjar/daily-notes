# Untitled Note - 1136

**Category:** Deep Learning  
**Date:** 2026-11-10 (morning)

---

# CutMix Data Augmentation

CutMix is a data‑augmentation technique that creates new training samples by cutting a rectangular region from one image and pasting it onto another, while also mixing their labels proportionally to the area of the patch. Formally, given images *x₁, x₂* and one‑hot labels *y₁, y₂*, the mixed sample is  

\[
\tilde{x}=M\odot x_1 + (1-M)\odot x_2,\quad 
\tilde{y}= \lambda y_1 + (1-\lambda) y_2,
\]

where *M* is a binary mask defining the cut region and λ = area(M)/area(image). The label interpolation forces the model to predict both classes, encouraging it to focus on all discriminative parts rather than over‑fitting to specific textures.

**Why use CutMix?**  
- Improves robustness to occlusion and localization errors.  
- Acts as a regularizer, often yielding higher top‑1 accuracy on image classification benchmarks (e.g., ImageNet, CIFAR‑10).  
- Benefits object detection and segmentation when combined with other augmentations.

**PyTorch example**

```python
import torch, torch.nn.functional as F
import numpy as np

def rand_bbox(size, lam):
    W, H = size[2], size[3]
    cut_rat = np.sqrt(1. - lam)
    cut_w = int(W * cut_rat)
    cut_h = int(H * cut_rat)

    cx = np.random.randint(W)
    cy = np.random.randint(H)

    bbx1 = np.clip(cx - cut_w // 2, 0, W)
    bby1 = np.clip(cy - cut_h // 2, 0, H)
    bbx2 = np.clip(cx + cut_w // 2, 0, W)
    bby2 = np.clip(cy + cut_h // 2, 0, H)

    return bbx1, bby1, bbx2, bby2

def cutmix(data, targets, alpha=1.0):
    lam = np.random.beta(alpha, alpha)
    rand_index = torch.randperm(data.size(0))
    shuffled_data, shuffled_targets = data[rand_index
