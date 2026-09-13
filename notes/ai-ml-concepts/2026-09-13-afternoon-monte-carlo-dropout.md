# Monte Carlo Dropout

**Category:** AI/ML Concepts  
**Date:** 2026-09-13 (afternoon)

---

# Monte Carlo Dropout for Uncertainty Estimation

Monte Carlo (MC) Dropout treats the dropout layer—normally used only during training—as a stochastic inference mechanism. By keeping dropout active at test time and performing multiple forward passes, each pass samples a different sub‑network. The variance among the predictions serves as a proxy for model uncertainty, while the mean approximates the usual deterministic output.

**Why it matters**  
- **Safety‑critical systems** (e.g., autonomous driving, medical diagnosis) need calibrated confidence estimates to trigger fallback strategies.  
- **Active learning** can query the most uncertain samples for labeling, reducing annotation cost.  
- **Out‑of‑distribution detection**: high predictive variance often signals inputs far from the training manifold.

**Typical workflow**  
```python
import torch, torch.nn as nn, torch.nn.functional as F

class MCDropoutNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(784, 256)
        self.dropout = nn.Dropout(p=0.5)          # keep during inference
        self.fc2 = nn.Linear(256, 10)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = self.dropout(x)                       # stochastic mask
        return self.fc2(x)

model = MCDropoutNet()
model.eval()                                    # still keep dropout

def mc_predict(x, n_samples=30):
    preds = torch.stack([model(x) for _ in range(n_samples)], dim=0)
    mean = preds.mean(0)
    var  = preds.var(0)                          # epistemic uncertainty
    return mean, var

logits, uncertainty = mc_predict(sample_tensor)
```
The `var` tensor highlights which classes or regions the model is less confident about, enabling downstream decisions that consider risk.

---
