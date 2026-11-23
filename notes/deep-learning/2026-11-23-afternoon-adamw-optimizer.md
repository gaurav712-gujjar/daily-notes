# AdamW Optimizer

**Category:** Deep Learning  
**Date:** 2026-11-23 (afternoon)

---

# AdamW Optimizer

AdamW is a variant of the Adam optimizer that decouples weight decay (L2‑regularization) from the gradient‑based update. In classic Adam, the L2 term is added to the gradients, which unintentionally interacts with the adaptive learning‑rate moments, leading to sub‑optimal regularization. AdamW instead applies weight decay **after** the parameter update, preserving the benefits of Adam’s adaptive moments while enforcing a true L2 penalty.

**Why use AdamW?**  
- **Improved generalization**: Decoupled decay yields more consistent regularization, often boosting test accuracy.  
- **Stable training**: Works well with large learning rates and modern training tricks such as learning‑rate warm‑up and cosine annealing.  
- **Broad adoption**: Default optimizer in many libraries (e.g., PyTorch’s `torch.optim.AdamW`) and state‑of‑the‑art vision/NLP models.

**Typical usage**  
```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Sequential(
    nn.Linear(784, 256),
    nn.ReLU(),
    nn.Linear(256, 10)
)

criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(),
                        lr=3e-4,
                        weight_decay=1e-2)   # decoupled L2 penalty

for x, y in dataloader:
    optimizer.zero_grad()
    logits = model(x)
    loss = criterion(logits, y)
    loss.backward()
    optimizer.step()
```

In practice, AdamW is the go‑to choice for training deep convolutional nets, Transformers, and large language models, especially when combined with modern schedulers and regularization strategies.
