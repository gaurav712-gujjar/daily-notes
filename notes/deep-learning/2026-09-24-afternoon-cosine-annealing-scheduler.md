# Cosine Annealing Scheduler

**Category:** Deep Learning  
**Date:** 2026-09-24 (afternoon)

---

# Cosine Annealing Scheduler

Cosine annealing is a learning‑rate scheduling technique that gradually reduces the learning rate following a half‑cosine curve, optionally restarting the cycle. The schedule is defined by  

\[
\eta_t = \eta_{\min} + \frac{1}{2}(\eta_{\max}-\eta_{\min})\bigl(1+\cos(\frac{t}{T}\pi)\bigr)
\]

where \(t\) is the current epoch, \(T\) the total epochs of the cycle, and \(\eta_{\max},\eta_{\min}\) the upper and lower bounds. The cosine shape yields a rapid decay early on and a gentle taper near the end, helping the optimizer escape shallow minima and settle into a good basin.

**Why use it?**  
- Improves convergence stability for deep nets (ResNets, Transformers).  
- Works well with stochastic optimizers like Adam or SGD with momentum.  
- When combined with restarts (SGDR), it can act as an implicit regularizer, often achieving better test accuracy than fixed or step decay schedules.

**Typical use‑cases**  
- Image classification with large CNNs.  
- Pre‑training language models where long training runs benefit from smooth LR decay.  
- Any setting where manual tuning of step‑wise decay is cumbersome.

**PyTorch example**

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CosineAnnealingLR

model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(),
                      nn.Linear(256, 10))
optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)

# decay from 0.1 to 0 over 50 epochs
scheduler = CosineAnnealingLR(optimizer, T_max=50, eta_min=0.0)

for epoch in range(50):
    train_one_epoch(model, optimizer)   # user‑defined training loop
    scheduler.step()
    print(f'Epoch {epoch+1}: LR = {scheduler.get_last_lr()[0]:.6f}')
```

The scheduler automatically updates the optimizer’s learning rate each epoch, following the cosine curve.
