# Elastic Weight Consolidation

**Category:** AI/ML Concepts  
**Date:** 2026-11-05 (afternoon)

---

# Elastic Weight Consolidation (EWC)

Elastic Weight Consolidation is a regularization technique for **continual (or lifelong) learning** that mitigates catastrophic forgetting when a neural network is trained sequentially on multiple tasks. After learning a task, EWC estimates the importance of each parameter using the Fisher Information Matrix. When training on a new task, a quadratic penalty is added to the loss, anchoring important weights close to their previous values while still allowing adaptation.

**Why/where it’s used**  
- **Robotic control** where a policy must acquire new skills without erasing old ones.  
- **Medical imaging** models that are updated with new disease data over time.  
- **Language models** fine‑tuned on domain‑specific corpora while preserving general language knowledge.

The method enables a single model to retain performance across tasks without storing old data, making it attractive for privacy‑sensitive or memory‑constrained settings.

```python
import torch
import torch.nn as nn
import torch.optim as optim

# simple MLP
model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(),
                      nn.Linear(256, 10))

def compute_fisher(model, dataloader, criterion):
    model.eval()
    fisher = {n: torch.zeros_like(p) for n, p in model.named_parameters()}
    for x, y in dataloader:
        model.zero_grad()
        loss = criterion(model(x), y)
        loss.backward()
        for n, p in model.named_parameters():
            fisher[n] += p.grad.detach() ** 2
    return {n: f / len(dataloader) for n, f in fisher.items()}

# after training Task A
fisher = compute_fisher(model, loader_A, nn.CrossEntropyLoss())
opt_params = {n: p.clone().detach() for n, p in model.named_parameters()}

def ewc_loss(model, criterion, x, y, lam=0.4):
    pred = model(x)
    loss = criterion(pred, y)
    # add quadratic penalty
    for n, p in model.named_parameters():
        loss += (lam / 2) * fisher[n] * (p - opt_params[n])**2
    return loss
```

The snippet shows how to compute the Fisher information after the first task and incorporate the EWC penalty during training on a subsequent task.
