# Differential Privacy Training

**Category:** AI/ML Concepts  
**Date:** 2026-11-11 (afternoon)

---

# Differential Privacy for Model Training  

Differential privacy (DP) provides a mathematically rigorous way to limit how much information about any single training example can be inferred from a trained model. The core idea is to add carefully calibrated random noise to the learning process—typically to the gradients—so that the model’s output distribution remains almost unchanged whether any one record is present or not. The privacy guarantee is expressed as (ε, δ)-DP, where smaller ε means stronger privacy.

**Why it’s used**  
- **Sensitive data**: Healthcare, finance, and user‑behavior logs often contain personal information that must stay confidential.  
- **Regulatory compliance**: GDPR, HIPAA, and other statutes encourage or require privacy‑preserving analytics.  
- **Trust**: Deploying models that provably protect individual data can increase user confidence and enable data sharing across organizations.

**Typical workflow**  
1. Clip per‑example gradients to bound their influence.  
2. Add Gaussian noise scaled to the clipping norm and a privacy budget.  
3. Track the cumulative privacy loss using a composition accountant (e.g., moments accountant).  

**Simple PyTorch example (using Opacus)**  

```python
import torch, torch.nn as nn, torch.optim as optim
from opacus import PrivacyEngine

model = nn.Linear(20, 2)
optimizer = optim.SGD(model.parameters(), lr=0.01)
privacy_engine = PrivacyEngine(
    model,
    batch_size=64,
    sample_size=10000,
    alphas=[10, 100],
    noise_multiplier=1.2,
    max_grad_norm=1.0,
)
privacy_engine.attach(optimizer)

for X, y in dataloader:          # X: (batch, 20), y: (batch,)
    optimizer.zero_grad()
    loss = nn.CrossEntropyLoss()(model(X), y)
    loss.backward()
    optimizer.step()
```

The `PrivacyEngine` handles gradient clipping, noise addition, and tracks the (ε, δ) budget automatically.  

*Differential privacy enables training useful models while providing strong, provable guarantees that individual records cannot be reverse‑engineered from the model’s parameters.*
