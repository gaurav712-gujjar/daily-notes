# Untitled Note - 0846

**Category:** AI/ML Concepts  
**Date:** 2026-10-23 (morning)

---

# Model-Agnostic Meta-Learning (MAML)

**What it is**  
MAML is a meta‑learning algorithm that seeks a set of model parameters θ which can be *quickly* adapted to new tasks with only a few gradient steps. During meta‑training, the algorithm samples many tasks, performs a small inner‑loop update on each task, and then updates the original θ by back‑propagating the post‑adaptation loss. Because the update rule is agnostic to the model architecture, MAML works with any differentiable learner (e.g., CNNs, RNNs, Transformers).

**Why/where it’s used**  
- **Few‑shot learning**: classification or regression where only a handful of labeled examples are available per new class.  
- **Robotics**: rapid adaptation to new dynamics or objects without retraining from scratch.  
- **Personalized medicine**: customizing predictive models to individual patients with limited data.  

MAML shines when the distribution of tasks is known during training but the exact downstream tasks are unseen at test time.

**Minimal PyTorch example**

```python
import torch, torch.nn as nn, torch.optim as optim

class SimpleNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc = nn.Linear(10, 1)

    def forward(self, x):
        return self.fc(x)

def inner_update(model, loss, lr=0.01):
    grads = torch.autograd.grad(loss, model.parameters(),
                                create_graph=True)
    updated = [p - lr * g for p, g in zip(model.parameters(), grads)]
    return updated

model = SimpleNet()
meta_opt = optim.Adam(model.parameters(), lr=1e-3)

for meta_step in range(1000):
    meta_loss = 0
    for task in sampled_tasks:            # each task provides (x_spt, y_spt, x_qry, y_qry)
        # ----- inner loop -----
        preds = model(task.x_spt)
        loss = nn.MSELoss()(preds, task.y_spt)
        fast_weights = inner_update(model, loss)

        # ----- outer loop -----
        qry_pred = nn.functional.linear(task.x_qry, fast_weights[0], fast_weights[1])
        meta_loss += nn.MSELoss()(qry_pred, task.y_qry)

    meta_opt.zero_grad()
    meta_loss.backward()
    meta_opt.step()
```

The snippet shows a single‑step inner update followed by a meta‑
