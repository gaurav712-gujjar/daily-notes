# Untitled Note - 1705

**Category:** Deep Learning  
**Date:** 2026-10-01 (afternoon)

---

# Cyclical Learning Rate (CLR)

A **Cyclical Learning Rate** varies the optimizer’s learning rate between a lower and upper bound in a periodic fashion during training. Instead of decaying monotonically, CLR follows a triangular (or sinusoidal) waveform, letting the model explore broader regions of the loss surface early on and fine‑tune later. The schedule is defined by three hyper‑parameters: `base_lr`, `max_lr`, and `step_size` (half‑cycle length).

**Why use CLR?**  
- **Faster convergence:** The periodic increase can escape shallow minima and saddle points, often reaching comparable accuracy in fewer epochs.  
- **Reduced tuning:** Choosing a sensible range (`base_lr`–`max_lr`) is usually easier than pinpointing a single optimal learning rate.  
- **Regularization effect:** The oscillations act like implicit noise, improving generalization in many vision and NLP tasks.

**Typical use‑cases**  
- Training convolutional networks on image classification (e.g., ResNet, EfficientNet).  
- Fine‑tuning large language models where a stable decay schedule is hard to set.  
- Early‑stage experiments to quickly gauge model capacity.

### PyTorch example

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CyclicLR

model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(),
                      nn.Linear(256, 10))
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# CLR: triangular policy, cycle length = 4 epochs (2 * step_size)
scheduler = CyclicLR(optimizer,
                     base_lr=1e-4,
                     max_lr=1e-2,
                     step_size_up=2000,   # iterations
                     mode='triangular')

for epoch in range(10):
    for xb, yb in train_loader:
        optimizer.zero_grad()
        loss = nn.CrossEntropyLoss()(model(xb), yb)
        loss.backward()
        optimizer.step()
        scheduler.step()          # update LR each batch
    print(f'Epoch {epoch+1}: LR = {scheduler.get_last_lr()[0]:.5f}')
```

The scheduler updates after every batch, producing a smooth triangular
