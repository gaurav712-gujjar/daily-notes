# Early

**Category:** Machine Learning  
**Date:** 2026-09-12 (afternoon)

---

# Early Stopping

Early stopping is a regularization technique that halts model training once performance on a validation set ceases to improve. During iterative optimization (e.g., gradient descent), the training loss typically keeps decreasing, but the validation loss may start to rise after a certain point, indicating over‑fitting. By monitoring the validation metric and stopping after *patience* epochs without improvement, we capture the model at its most generalizable state.

**Practical use cases**  
- Deep neural networks where training is expensive and over‑fitting is common.  
- Gradient‑boosted trees (XGBoost, LightGBM) that support early stopping out‑of‑the‑box.  
- Any supervised learning pipeline where a hold‑out validation set is available.

**Key parameters**  
- `patience`: number of epochs to wait after the last improvement.  
- `min_delta`: minimum change to qualify as an improvement (helps ignore noise).  
- `restore_best_weights`: whether to roll back to the best checkpoint after stopping.

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, random_split

model = nn.Sequential(nn.Linear(20, 64), nn.ReLU(),
                      nn.Linear(64, 1))
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

train_set, val_set = random_split(dataset, [0.8, 0.2])
train_loader = DataLoader(train_set, batch_size=32)
val_loader   = DataLoader(val_set, batch_size=32)

best_val_loss = float('inf')
patience, wait = 5, 0

for epoch in range(100):
    model.train()
    for x, y in train_loader:
        optimizer.zero_grad()
        loss = criterion(model(x), y)
        loss.backward()
        optimizer.step()

    # validation
    model.eval()
    val_loss = 0.0
    with torch.no_grad():
        for x, y in val_loader:
            val_loss += criterion(model(x), y).item()
    val_loss /= len(val_loader)

    if val_loss < best_val_loss - 1e-4:
        best_val_loss = val_loss
        best_state = model.state_dict()
        wait = 0
    else:
        wait += 1
        if wait >= patience:
            print(f"Stopping early at epoch {epoch}")
            model.load_state_dict(best_state)
            break
```

Early stopping is lightweight, requires no extra model parameters, and often yields the best trade‑off between bias and variance.
