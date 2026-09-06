# Mixed Precision Training

**Category:** Deep Learning  
**Date:** 2026-09-06 (afternoon)

---

# Mixed Precision Training

Mixed Precision Training (MPT) leverages both 16‑bit (half‑precision) and 32‑bit (single‑precision) floating‑point formats during neural‑network training. The bulk of the compute‑intensive matrix multiplications are performed in FP16, which halves memory bandwidth and doubles throughput on modern GPUs (e.g., NVIDIA Ampere). To preserve numerical stability, a small subset of operations—such as loss scaling and weight updates—remain in FP32.  

**Why use it?**  
- **Speed:** FP16 kernels run up to 2× faster on tensor‑core‑enabled hardware.  
- **Memory:** Model activations occupy half the memory, allowing larger batch sizes or deeper networks.  
- **Energy efficiency:** Reduced precision cuts power consumption, valuable for large‑scale training farms.  

MPT is especially popular in computer‑vision (ResNet, EfficientNet) and large‑scale language models (BERT, GPT) where training time and GPU memory are critical bottlenecks.

**PyTorch example**

```python
import torch
from torch import nn, optim
from torch.cuda.amp import autocast, GradScaler

model = nn.ResNet50().cuda()
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=3e-4)

scaler = GradScaler()          # handles dynamic loss scaling

for imgs, targets in dataloader:
    imgs, targets = imgs.cuda(), targets.cuda()
    optimizer.zero_grad()

    # FP16 forward pass
    with autocast():
        outputs = model(imgs)
        loss = criterion(outputs, targets)

    # Scaled back‑propagation
    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

The `autocast` context automatically chooses the optimal precision for each operation, while `GradScaler` prevents underflow in the loss gradient.

**When to avoid:**  
- Very small models where the overhead of scaling outweighs gains.  
- GPUs lacking tensor cores (e.g., older architectures) may see limited speedup.

---
