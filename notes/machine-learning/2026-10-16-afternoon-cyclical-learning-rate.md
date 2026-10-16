# Cyclical Learning Rate

**Category:** Machine Learning  
**Date:** 2026-10-16 (afternoon)

---

# Cyclical Learning Rate

A **Cyclical Learning Rate (CLR)** varies the optimizer’s learning rate between a lower and upper bound in a periodic fashion during training. Instead of decaying monotonically, the rate follows a triangular (or sinusoidal) wave, allowing the model to explore wider regions of the loss surface and then converge more finely. The original paper (Leslie N. Smith, 2017) showed that CLR can achieve comparable or better performance with fewer epochs and less hyper‑parameter tuning.

**Why use it?**  
- **Faster convergence:** The periodic increase can help escape shallow minima early on.  
- **Reduced tuning:** You only need to pick reasonable min/max bounds and a step size, avoiding exhaustive learning‑rate schedules.  
- **Improved generalization:** The regular oscillations act as a form of implicit regularization, similar to stochastic weight averaging.

**Typical settings**  
- **Triangular:** Linear increase then decrease.  
- **Triangular2:** Same as triangular but the amplitude halves after each cycle.  
- **Exponential:** Learning rate changes exponentially within each cycle.

### PyTorch example

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.optim.lr_scheduler import CyclicLR

model = nn.Linear(20, 1)
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Cycle between 1e-4 and 1e-2 every 2000 iterations
scheduler = CyclicLR(
    optimizer,
    base_lr=1e-4,
    max_lr=1e-2,
    step_size_up=1000,
    mode='triangular',
)

for epoch in range(5):
    for xb, yb in dataloader:
        optimizer.zero_grad()
        loss = nn.functional.mse_loss(model(xb), yb)
        loss.backward()
        optimizer.step()
        scheduler.step()   # update LR each batch
```

In practice, CLR is popular for computer‑vision tasks, language models, and any deep network where training time is a bottleneck.
