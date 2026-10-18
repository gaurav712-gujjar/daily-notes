# Stochastic Weight Averaging

**Category:** AI/ML Concepts  
**Date:** 2026-10-18 (morning)

---

# Stochastic Weight Averaging (SWA)

Stochastic Weight Averaging is a simple yet powerful technique to improve the generalization of deep neural networks. Instead of using the final checkpoint of training, SWA maintains a running average of model weights taken from the tail end of the training trajectory (typically after the learning rate has been reduced). The averaged weights tend to lie in a flatter region of the loss landscape, which correlates with better robustness to unseen data.

**Why use SWA?**  
- **Better test accuracy** with minimal extra compute.  
- **Faster convergence** when combined with cyclic or cosine learning‑rate schedules.  
- **Compatibility** with any optimizer and architecture; it requires only a few extra lines of code.

**Typical workflow**
1. Train the model with a standard optimizer (e.g., SGD) and a learning‑rate schedule that periodically raises the LR (SGDR or cosine annealing).  
2. After a warm‑up phase, start collecting weight snapshots every few epochs.  
3. Compute the element‑wise average of these snapshots to obtain the SWA model.  
4. Perform a short batch‑norm recomputation on the training data to calibrate statistics.

```python
import torch, torch.nn as nn, torch.optim as optim
from torch.optim.swa_utils import AveragedModel, SWALR

model = MyNet()
criterion = nn.CrossEntropyLoss()
base_opt = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)

# SWA wrapper
swa_model = AveragedModel(model)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(base_opt, T_max=200)
swa_scheduler = SWALR(base_opt, swa_lr=0.05)

for epoch in range(250):
    train_one_epoch(model, train_loader, criterion, base_opt)
    scheduler.step()
    if epoch > 150:               # start averaging after epoch 150
        swa_model.update_parameters(model)
        swa_scheduler.step()
# Update batch‑norm statistics
torch.optim.swa_utils.update_bn(train_loader, swa_model)
# Evaluate swa_model
```
