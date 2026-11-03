# Weight Normalization

**Category:** AI/ML Concepts  
**Date:** 2026-11-03 (morning)

---

# Weight Normalization

Weight Normalization (WN) is a re‑parameterization of a neural network’s weight vectors that decouples their magnitude from direction. Each weight vector **w** is expressed as **w = g·(v / ‖v‖)**, where *v* is a learnable vector that determines direction, and *g* is a scalar controlling the norm. During back‑propagation the optimizer updates *v* and *g* separately, which often leads to faster convergence and more stable training, especially in deep convolutional or recurrent models.

**Why it’s useful**  
- **Accelerated training**: By fixing the scale of weight vectors early, gradients become more predictable, reducing the need for aggressive learning‑rate schedules.  
- **Better conditioning**: Separating length from direction mitigates exploding/vanishing gradients, similar to batch normalization but without dependence on batch statistics.  
- **Compatibility**: WN can be combined with other regularizers (dropout, weight decay) and works for both fully‑connected and convolutional layers.

**Typical use‑cases**  
- Training GAN generators where batch statistics are unstable.  
- Large‑scale language models that benefit from stable gradient flow across many layers.  
- Scenarios where batch size is tiny or variable, making batch normalization impractical.

```python
import torch
import torch.nn as nn
import torch.nn.utils.weight_norm as wn

class ConvWN(nn.Module):
    def __init__(self, in_ch, out_ch, kernel=3, stride=1, padding=1):
        super().__init__()
        self.conv = wn(nn.Conv2d(in_ch, out_ch, kernel, stride, padding))

    def forward(self, x):
        return torch.relu(self.conv(x))

# Example
x = torch.randn(8, 3, 32, 32)          # batch of images
model = ConvWN(3, 16)
y = model(x)                           # forward pass with weight‑normalized conv
```

The snippet shows how a single convolutional layer can be weight‑normalized in PyTorch with just one line of code.
