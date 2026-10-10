# Gradient Checkpointing

**Category:** Deep Learning  
**Date:** 2026-10-10 (morning)

---

# Gradient Checkpointing

Gradient checkpointing (also called activation recomputation) is a memory‑saving technique for training very deep neural networks. During the forward pass, instead of storing every intermediate activation needed for back‑propagation, only a subset (checkpoints) are kept. When the backward pass reaches a region without stored activations, the forward computation for that region is re‑executed on‑the‑fly to reconstruct the missing tensors. This trades extra compute time for a substantial reduction in GPU memory usage, enabling larger batch sizes or deeper models on limited hardware.

**When to use it**  
- Training Transformer‑style or ResNet‑like models that exceed GPU memory.  
- Conducting neural architecture search where many candidate networks are evaluated.  
- Fine‑tuning massive pre‑trained models (e.g., BERT‑large) on a single GPU.

**PyTorch example**

```python
import torch
from torch.utils.checkpoint import checkpoint

def block(x):
    # a simple two‑layer MLP block
    x = torch.nn.functional.relu(torch.nn.Linear(256, 256)(x))
    return torch.nn.functional.relu(torch.nn.Linear(256, 256)(x))

def forward(x):
    # checkpoint every block to save memory
    for _ in range(12):          # 12 deep blocks
        x = checkpoint(block, x)
    return x

inp = torch.randn(32, 256, requires_grad=True)  # batch size 32
out = forward(inp)
loss = out.mean()
loss.backward()
```

In this snippet, `torch.utils.checkpoint.checkpoint` stores only the input‑output boundary of each block, recomputing the interior activations during back‑propagation, cutting memory roughly by half with modest extra runtime.
