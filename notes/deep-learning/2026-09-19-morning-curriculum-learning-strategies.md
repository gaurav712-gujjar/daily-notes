# Curriculum Learning Strategies

**Category:** Deep Learning  
**Date:** 2026-09-19 (morning)

---

# Curriculum Learning Strategies

Curriculum Learning (CL) is a training paradigm that orders training samples from easy to hard, mimicking the way humans acquire knowledge. Instead of presenting all data randomly, the model first learns simple patterns and gradually tackles more challenging examples. This can be implemented by defining a **curriculum schedule** that adjusts the difficulty level based on metrics such as loss, confidence, or predefined difficulty scores.

**Why use it?**  
- **Faster convergence:** Early exposure to easy examples stabilizes gradients, allowing the optimizer to find a good basin of attraction quickly.  
- **Better generalization:** By preventing the model from being overwhelmed by noisy or out‑of‑distribution samples early on, CL often yields smoother decision boundaries.  
- **Robustness to noisy data:** Difficult or mislabeled samples are introduced later, when the model has already learned a solid representation.

**Practical scenarios** include language modeling (starting with short, frequent sentences), computer vision (beginning with centered objects before adding occlusions), and reinforcement learning (simple environments before complex ones).

```python
import torch, torch.nn as nn, torch.optim as optim
from torch.utils.data import DataLoader, Subset

def curriculum_dataloader(dataset, epoch, milestones, easy_ratio=0.5):
    # Increase difficulty as epoch passes milestones
    difficulty = sum(epoch >= m for m in milestones) / len(milestones)
    # Select a proportion of easy (low loss) samples
    easy_len = int(len(dataset) * (1 - difficulty) * easy_ratio)
    indices = torch.randperm(len(dataset))[:easy_len]
    return DataLoader(Subset(dataset, indices), batch_size=64, shuffle=True)

# Example training loop
for epoch in range(num_epochs):
    loader = curriculum_dataloader(train_set, epoch, milestones=[5, 10, 15])
    for x, y in loader:
        # standard training step …
        pass
```

In this snippet, the data loader gradually includes a larger fraction of the full dataset as training progresses, embodying a simple curriculum schedule.
