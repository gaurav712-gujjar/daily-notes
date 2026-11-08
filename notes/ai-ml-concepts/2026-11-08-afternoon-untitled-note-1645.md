# Untitled Note - 1645

**Category:** AI/ML Concepts  
**Date:** 2026-11-08 (afternoon)

---

# Model-Agnostic Meta-Learning (MAML)

**Concept**  
MAML is a meta‑learning algorithm that trains a model’s parameters such that only a few gradient steps on a new task yield good performance. It treats the learning process itself as an optimization problem: the outer loop updates the initial parameters to maximize post‑adaptation performance, while the inner loop performs task‑specific fine‑tuning.

**Why/Where it’s used**  
- **Few‑shot learning**: when labeled data for a target task are scarce (e.g., medical imaging with limited annotations).  
- **Rapid adaptation**: robotics or personalization systems that must adjust to new environments or users on‑the‑fly.  
- **Task‑agnostic pretraining**: unlike task‑specific pretraining, MAML’s learned initialization works across a distribution of tasks, making it versatile for downstream problems.

**Simple PyTorch illustration**

```python
import torch
from torch import nn, optim

class Net(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

def inner_update(model, loss, lr):
    grads = torch.autograd.grad(loss, model.parameters(),
                                create_graph=True)
    updated = [p - lr * g for p, g in zip(model.parameters(), grads)]
    return updated

# meta‑training loop (high‑level)
model = Net()
meta_opt = optim.Adam(model.parameters(), lr=1e-3)

for task in tasks:                     # sample a batch of tasks
    # -------- inner loop (task‑specific) ----------
    support_x, support_y = task['support']
    preds = model(support_x)
    loss = nn.MSELoss()(preds, support_y)
    fast_weights = inner_update(model, loss, lr=0.01)

    # -------- outer loop (meta) ----------
    query_x, query_y = task['query']
    # forward with adapted weights
    def forward_fast(x):
        out = x
        for layer, w in zip([model.fc], fast_weights):
            out = nn.functional.linear(out, w, layer.bias)
