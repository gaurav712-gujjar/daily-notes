# One-Cycle Learning Rate Policy

**Category:** Machine Learning  
**Date:** 2026-11-14 (morning)

---

# One‑Cycle Learning Rate Policy

The **One‑Cycle Learning Rate (LR) policy** is a training schedule that varies the learning rate in a single, symmetric “cycle”: it starts low, ramps up to a maximum, then anneals back to a value even lower than the start. Typically a momentum schedule is paired, decreasing when LR rises and vice‑versa. The core idea (proposed by Leslie Smith, 2018) is that a brief period of high learning rates helps the optimizer escape sharp minima and find flatter, more generalizable solutions, while the final low LR fine‑tunes the parameters.

### Why use it?
- **Faster convergence**: Models often reach target accuracy in fewer epochs than with a constant or step‑decay LR.
- **Better generalization**: The high‑LR phase promotes exploration of the loss landscape, reducing over‑fitting.
- **Simplified hyper‑parameter tuning**: Only the maximum LR (and optionally the total training steps) need to be set; the schedule handles the rest.

### Practical scenarios
- Training deep CNNs or Transformers on image/video datasets.
- Fine‑tuning large pre‑trained language models where quick adaptation is desired.
- Situations with limited compute budget where epoch count must be minimized.

### PyTorch example
```python
import torch
from torch import nn, optim
from torch.optim.lr_scheduler import OneCycleLR

model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(),
                      nn.Linear(256, 10))
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)

# assume 1000 training batches per epoch, run for 5 epochs
scheduler = OneCycleLR(optimizer,
                       max_lr=0.5,
                       steps_per_epoch=1000,
                       epochs=5,
                       pct_start=0.3,          # 30 % of steps increase LR
                       anneal_strategy='cos') # cosine annealing

for epoch in range(5):
    for xb, yb in train_loader:
        optimizer.zero_grad()
        loss = criterion(model(xb), yb)
        loss.backward()
        optimizer.step()
        scheduler.step()   # update LR each batch
```
The scheduler automatically adjusts both learning rate and momentum according to the one‑cycle policy.

---
