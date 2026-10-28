# Gradient Clipping

**Category:** AI/ML Concepts  
**Date:** 2026-10-28 (afternoon)

---

# Gradient Clipping

Gradient clipping is a technique that limits the magnitude of gradients during back‑propagation. When training deep or recurrent networks, especially with long sequences, gradients can explode (grow extremely large) or vanish (shrink to near zero). Exploding gradients cause unstable updates, leading to NaNs or loss spikes, and can prevent convergence. By clipping, we cap the norm (or individual values) of the gradient vector before the optimizer step, preserving direction while keeping step size bounded.

**Typical use‑cases**
- Training RNNs, LSTMs, or Transformers on long sequences.  
- Stabilizing training of deep convolutional nets with high learning rates.  
- Reinforcement learning where reward signals can create abrupt gradient surges.

**How it works**  
A common strategy is *norm clipping*: compute the L2 norm of all gradients in a layer (or the whole model). If the norm exceeds a threshold `C`, scale all gradients by `C / norm`. Another approach is *value clipping*, where each gradient component is limited to a range `[-c, c]`.

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.LSTM(input_size=128, hidden_size=256, num_layers=2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

for x, y in dataloader:
    optimizer.zero_grad()
    out, _ = model(x)
    loss = criterion(out.view(-1, out.size(-1)), y.view(-1))
    loss.backward()
    # Clip gradients globally to a max norm of 1.0
    torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
    optimizer.step()
```

In this snippet, `clip_grad_norm_` ensures that the overall gradient norm never exceeds 1.0, protecting the training dynamics from exploding updates.

---
