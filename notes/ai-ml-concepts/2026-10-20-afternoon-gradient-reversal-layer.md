# Gradient Reversal Layer

**Category:** AI/ML Concepts  
**Date:** 2026-10-20 (afternoon)

---

# Gradient Reversal Layer (GRL) for Domain Adaptation  

The Gradient Reversal Layer is a simple yet powerful building block for unsupervised domain adaptation. During the forward pass it acts as the identity function, passing its input unchanged to the next layer. During back‑propagation it multiplies the gradient by a negative scalar λ, effectively *reversing* the direction of the gradient that flows into the feature extractor. This forces the feature encoder to produce representations that are indistinguishable across source and target domains while still being useful for the primary task (e.g., classification).

**Why it’s used**  
- **Domain‑Invariant Features:** By adversarially confusing a domain discriminator, the encoder learns features that generalize to unseen domains.  
- **End‑to‑End Training:** GRL integrates seamlessly into standard deep‑learning pipelines, requiring no extra optimization loops.  
- **Flexibility:** λ can be scheduled (e.g., gradually increased) to balance task performance and domain alignment.

**Typical architecture**  

```
input → Feature Encoder → Classifier (source loss)
                         ↘
                          → Gradient Reversal Layer → Domain Discriminator (domain loss)
```

**PyTorch example**

```python
import torch
from torch import nn
from torch.autograd import Function

class GradientReversalFunction(Function):
    @staticmethod
    def forward(ctx, x, lambd):
        ctx.lambd = lambd
        return x.clone()

    @staticmethod
    def backward(ctx, grad_output):
        return -ctx.lambd * grad_output, None

class GradientReversal(nn.Module):
    def __init__(self, lambd=1.0):
        super().__init__()
        self.lambd = lambd
    def forward(self, x):
        return GradientReversalFunction.apply(x, self.lambd)

# usage
features = encoder(x)
class_pred = classifier(features)

rev_features = GradientReversal(lambd=0.5)(features)
domain_pred = domain_discriminator(rev_features)
```

The reversed gradients push the encoder toward domain‑invariant representations, enabling better performance on target data without labels.
