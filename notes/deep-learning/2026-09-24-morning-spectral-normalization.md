# Spectral Normalization

**Category:** Deep Learning  
**Date:** 2026-09-24 (morning)

---

# Spectral Normalization

Spectral Normalization (SN) stabilizes the training of deep neural networks—especially generative models—by constraining the Lipschitz constant of each layer. It does so by dividing the weight matrix **W** by its largest singular value σ₁(W):

\[
\hat{W} = \frac{W}{\sigma_1(W)}
\]

The singular value is approximated with a few power‑iteration steps, keeping the overhead minimal.

**Why it matters**  
- **GANs:** SN prevents the discriminator from becoming too “sharp,” which otherwise leads to vanishing gradients for the generator.  
- **Robustness:** Bounding the Lipschitz constant improves adversarial robustness and generalization.  
- **Compatibility:** It works with any linear, convolutional, or embedding layer without altering the architecture.

**Typical use‑case**  
Apply SN to the discriminator of a GAN (e.g., StyleGAN2) or to any network where controlling the gradient norm is critical.

**PyTorch example**

```python
import torch
import torch.nn as nn
import torch.nn.utils.spectral_norm as spectral_norm

class SNDiscriminator(nn.Module):
    def __init__(self, in_channels=3, hidden=64):
        super().__init__()
        self.conv1 = spectral_norm(nn.Conv2d(in_channels, hidden, 4, stride=2, padding=1))
        self.conv2 = spectral_norm(nn.Conv2d(hidden, hidden * 2, 4, stride=2, padding=1))
        self.fc = spectral_norm(nn.Linear(hidden * 2 * 8 * 8, 1))

    def forward(self, x):
        x = torch.leaky_relu(self.conv1(x), 0.2)
        x = torch.leaky_relu(self.conv2(x), 0.2)
        x = x.view(x.size(0), -1)
        return self.fc(x)

# instantiate
D = SNDiscriminator()
```

In this snippet, each layer’s weights are automatically normalized at every forward pass, ensuring a controlled Lipschitz bound throughout training.

---
