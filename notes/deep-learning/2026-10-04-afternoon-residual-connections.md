# Residual Connections

**Category:** Deep Learning  
**Date:** 2026-10-04 (afternoon)

---

# Residual Connections (ResNet)

Residual connections are a simple architectural trick that lets a neural network learn *identity mappings* alongside the usual transformations. Instead of feeding the output of layer ℓ directly into layer ℓ+1, a **skip (or shortcut) connection** adds the input of the block to its output:

\[
\mathbf{y}=F(\mathbf{x},\{W_i\})+\mathbf{x}
\]

where \(F\) is the stacked non‑linear layers (e.g., Conv‑BN‑ReLU) and \(\mathbf{x}\) is the block’s input. This formulation alleviates the *vanishing‑gradient* problem in very deep networks, making it possible to train hundreds or even thousands of layers. The seminal ResNet‑50/101 models demonstrated that deeper nets can achieve lower training error and better generalization when residual shortcuts are used.

**Practical uses**
- Image classification (ResNet, Wide‑ResNet, ResNeXt)  
- Object detection backbones (Faster‑RCNN, YOLO)  
- Semantic segmentation (DeepLab)  
- Transfer learning: pretrained ResNets are ubiquitous feature extractors.

**PyTorch example**

```python
import torch.nn as nn

class ResidualBlock(nn.Module):
    def __init__(self, in_ch, out_ch, stride=1):
        super().__init__()
        self.conv = nn.Sequential(
            nn.Conv2d(in_ch, out_ch, 3, stride, 1, bias=False),
            nn.BatchNorm2d(out_ch),
            nn.ReLU(inplace=True),
            nn.Conv2d(out_ch, out_ch, 3, 1, 1, bias=False),
            nn.BatchNorm2d(out_ch)
        )
        self.shortcut = nn.Identity()
        if stride != 1 or in_ch != out_ch:
            self.shortcut = nn.Sequential(
                nn.Conv2d(in_ch, out_ch, 1, stride, bias=False),
                nn.BatchNorm2d(out_ch)
            )
        self.relu = nn.ReLU(inplace=True)

    def forward(self, x):
        out = self.conv(x) + self.shortcut(x)
        return self.relu(out)
```

The block can be stacked to form deep ResNets, enabling stable training even with very large depth.
