# Untitled Note - 1022

**Category:** AI/ML Concepts  
**Date:** 2026-10-30 (morning)

---

# Sharpness‑Aware Minimization (SAM)

Sharpness‑Aware Minimization is an optimizer‑level regularization technique that seeks parameters lying in *flat* minima of the loss landscape. Instead of minimizing the loss at the current weights θ, SAM first perturbs the weights in the direction that maximally increases the loss (within a small radius ρ) and then updates θ to reduce this worst‑case loss:

\[
\min_{\theta}\; \max_{\|\epsilon\|\le\rho} \; L(\theta + \epsilon)
\]

The inner maximization pushes the optimizer toward regions where the loss surface is smooth, which empirically improves generalization and robustness to adversarial attacks.

### When to use it
- Training vision models (ResNet, ConvNeXt) where over‑fitting is common.  
- Fine‑tuning large language models when data is limited.  
- Scenarios demanding stable performance under distribution shift.

### PyTorch example

```python
import torch, torch.nn as nn, torch.optim as optim

model = torchvision.models.resnet18(pretrained=False)
criterion = nn.CrossEntropyLoss()
base_opt = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
rho = 0.05                     # SAM radius

for x, y in loader:
    # ---- SAM inner step ----
    loss = criterion(model(x), y)
    loss.backward()
    # compute epsilon = rho * grad / ||grad||
    epsilon = []
    for p in model.parameters():
        if p.grad is None: continue
        eps = rho * p.grad / (p.grad.norm() + 1e-12)
        p.data.add_(eps)               # θ + ε
        epsilon.append(eps)

    # ---- SAM outer step ----
    loss_perturbed = criterion(model(x), y)
    loss_perturbed.backward()
    base_opt.step()
    base_opt.zero_grad()

    # restore original weights
    for p, eps in zip(model.parameters(), epsilon):
        p.data.sub_(eps)
```

SAM adds only a modest overhead (one extra forward‑backward pass) but often yields noticeable gains in validation accuracy and out‑
