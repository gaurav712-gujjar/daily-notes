# Untitled Note - 1555

**Category:** Machine Learning  
**Date:** 2026-10-10 (afternoon)

---

# Stochastic Weight Averaging (SWA)

Stochastic Weight Averaging is a simple yet powerful technique for improving the generalization of deep neural networks. Instead of keeping only the final set of parameters after training, SWA maintains a running average of model weights collected at several points near the end of training (typically when the learning rate is low). Because the averaged weights lie in a flatter region of the loss landscape, the resulting model is less sensitive to perturbations and usually yields higher test accuracy without extra training epochs.

**When to use it**  
- Large‑scale image or language models where training already uses a cyclical or cosine‑annealed learning rate.  
- Situations where a modest boost in validation performance is needed without altering the architecture.  
- Scenarios where inference speed must stay unchanged (the averaged model has the same size as a single checkpoint).

**How it works**  
1. Train the network with a standard optimizer (SGD, AdamW, etc.) and a learning‑rate schedule that decays to a small constant.  
2. After a burn‑in period, start collecting the current weights every *k* iterations.  
3. Update the SWA weights: `w_swa = (w_swa * n + w_current) / (n + 1)`, where *n* is the number of snapshots taken so far.

```python
import torch, torch.nn as nn, torch.optim as optim

model = MyNet()
optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=200)

swa_model = torch.optim.swa_utils.AveragedModel(model)
swa_start = 150          # epoch to begin averaging
swa_scheduler = torch.optim.swa_utils.SWALR(optimizer, swa_lr=0.05)

for epoch in range(200):
    train_one_epoch(model, optimizer)
    scheduler.step()
    if epoch >= swa_start:
        swa_model.update_parameters(model)
        swa_scheduler.step()

# Update BN statistics before evaluation
torch.optim.swa_utils.update_bn(train_loader, swa_model)
```

SWA can be combined with other regularizers (dropout, weight decay) and often yields a 0.5‑2 %
