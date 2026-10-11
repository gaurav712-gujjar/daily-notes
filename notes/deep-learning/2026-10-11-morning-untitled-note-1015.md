# Untitled Note - 1015

**Category:** Deep Learning  
**Date:** 2026-10-11 (morning)

---

# Stochastic Weight Averaging (SWA)

**What it is**  
Stochastic Weight Averaging is a simple yet powerful training technique that improves generalization by averaging the model parameters of several checkpoints taken near the end of training. Instead of using the final weights, SWA maintains a running average of weights after the learning rate has been reduced to a low, cyclic schedule. The resulting “averaged” model typically sits in a flatter region of the loss landscape, leading to better test performance.

**Why / Where it’s used**  
- **Image classification** with CNNs and Vision Transformers, where SWA often yields a 1‑2 % boost in top‑1 accuracy.  
- **Fine‑tuning** of pretrained models on downstream tasks; averaging a few fine‑tune checkpoints stabilizes the adaptation.  
- **Limited compute scenarios**: SWA adds virtually no extra training cost—just a few extra forward‑backward passes to update the average.  
- **Robustness**: flatter minima are less sensitive to data noise and adversarial perturbations.

**Quick PyTorch example**

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision import models, datasets, transforms

# 1️⃣ Load a pretrained ResNet
model = models.resnet18(pretrained=True)
criterion = nn.CrossEntropyLoss()
optimizer = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)

# 2️⃣ Define SWA optimizer wrapper
swa_start = 30          # epoch to start averaging
swa_model = torch.optim.swa_utils.AveragedModel(model)
swa_scheduler = torch.optim.swa_utils.SWALR(optimizer, swa_lr=0.05)

for epoch in range(50):
    # standard training loop …
    for inputs, targets in train_loader:
        optimizer.zero_grad()
        outputs = model(inputs)
        loss = criterion(outputs, targets)
        loss.backward()
        optimizer.step()

    # after swa_start, update the averaged weights
    if epoch >= swa_start:
        swa_model.update_parameters(model)
        swa_scheduler.step
