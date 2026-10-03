# Group Normalization

**Category:** Deep Learning  
**Date:** 2026-10-03 (afternoon)

---

# Group Normalization

Group Normalization (GN) is a normalization technique that divides the channels of a convolutional feature map into **G** groups and computes mean/variance statistics within each group. Unlike Batch Normalization, GN does **not** depend on the batch dimension, making it robust to small batch sizes or even batch size = 1. The normalized output is then scaled and shifted by learnable parameters γ and β.

**Why use it?**  
- **Small or variable batch sizes:** In object detection, segmentation, or video models, memory constraints often force batch sizes of 1–2, where BatchNorm fails.  
- **Consistent inference:** GN behaves identically during training and inference, eliminating the need for running statistics.  
- **Better transfer to new domains:** Since GN relies only on per‑sample statistics, it adapts more readily to domain shift.

**Typical settings:**  
- **G = 32** is common for ResNet‑style backbones (when channel count ≥ 32).  
- For very shallow layers, G can be set to the number of channels (equivalent to LayerNorm).

### PyTorch example

```python
import torch
import torch.nn as nn

class GNResBlock(nn.Module):
    def __init__(self, in_channels, out_channels, groups=32):
        super().__init__()
        self.conv = nn.Conv2d(in_channels, out_channels, kernel_size=3,
                              padding=1, bias=False)
        self.gn   = nn.GroupNorm(groups, out_channels)
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        return self.relu(self.gn(self.conv(x)))

# usage
x = torch.randn(2, 64, 56, 56)          # batch size 2, 64 channels
block = GNResBlock(64, 128, groups=16) # 16 groups → 8 channels per group
y = block(x)                           # shape: (2, 128, 56, 56)
```

In this snippet, `GroupNorm` replaces the usual `BatchNorm2d`. The same layer works unchanged during training and evaluation, making it ideal for tasks like instance segmentation where per‑image statistics are crucial.

---
