# Elastic Weight

**Category:** AI/ML Concepts  
**Date:** 2026-09-27 (morning)

---

# Elastic Weight Consolidation (EWC)

Elastic Weight Consolidation is a continual‑learning technique that mitigates catastrophic forgetting when a neural network is trained sequentially on multiple tasks. EWC adds a quadratic penalty to the loss that discourages important weights (identified by a Fisher information matrix) from drifting far from the values learned on previous tasks. The penalty term looks like  

\[
\mathcal{L}_{\text{EWC}} = \sum_i \frac{\lambda}{2} F_i (\theta_i - \theta_i^{*})^2,
\]

where \(F_i\) is the Fisher estimate for parameter \(i\), \(\theta_i^{*}\) are the weights after the prior task, and \(\lambda\) controls regularization strength.

**Why it’s used:**  
- **Lifelong learning:** Enables a single model to acquire new capabilities without erasing earlier knowledge.  
- **Resource‑efficient:** No need to store full datasets from previous tasks; only the Fisher diagonal and parameter snapshot are retained.  
- **Broad applicability:** Works with feed‑forward, convolutional, and transformer architectures, making it suitable for vision, language, and robotics domains.

**Simple PyTorch example**

```python
import torch, torch.nn as nn, torch.optim as optim

model = MyNet()
optimizer = optim.SGD(model.parameters(), lr=0.01)

# after training on Task A
theta_star = {n: p.clone().detach() for n, p in model.named_parameters()}
fisher = {n: torch.zeros_like(p) for n, p in model.named_parameters()}
model.eval()
for x, y in data_A:               # compute Fisher diag
    optimizer.zero_grad()
    loss = nn.CrossEntropyLoss()(model(x), y)
    loss.backward()
    for n, p in model.named_parameters():
        fisher[n] += p.grad.pow(2)

# training on Task B with EWC penalty
lam = 0.5
for x, y in data_B:
    optimizer.zero_grad()
    loss = nn.CrossEntropyLoss()(model(x), y)
    ewc_penalty = sum(lam * fisher[n] * (p - theta_star[n]).pow(2).sum()
                      for n, p in model.named_parameters())
    (loss + ewc_penalty).backward()
    optimizer.step()
```

EWC provides a lightweight, mathematically grounded way to preserve knowledge across tasks, a cornerstone for building truly adaptable AI systems.
