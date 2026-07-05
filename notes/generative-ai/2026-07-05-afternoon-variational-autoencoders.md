# Variational Autoencoders

**Category:** Generative AI  
**Date:** 2026-07-05 (afternoon)

---

# Variational Autoencoders
Variational autoencoders (VAEs) are a type of generative model that combines the capabilities of autoencoders and probabilistic modeling. They consist of an encoder network that maps the input data to a latent space and a decoder network that maps the latent space back to the input data. The key difference between VAEs and traditional autoencoders is that VAEs learn a probabilistic representation of the input data, allowing them to generate new data samples.

VAEs are used in practice for a variety of tasks, including image and video generation, anomaly detection, and dimensionality reduction. They are particularly useful for generating new data samples that are similar to the training data, making them a popular choice for applications such as generative art and data augmentation.

For example, in Python using the PyTorch library, a simple VAE can be implemented as follows:
```python
import torch
import torch.nn as nn

class VAE(nn.Module):
    def __init__(self):
        super(VAE, self).__init__()
        self.encoder = nn.Sequential(
            nn.Linear(784, 256),
            nn.ReLU(),
            nn.Linear(256, 128)
        )
        self.decoder = nn.Sequential(
            nn.Linear(128, 256),
            nn.ReLU(),
            nn.Linear(256, 784)
        )

    def forward(self, x):
        z = self.encoder(x)
        x_recon = self.decoder(z)
        return x_recon
```
