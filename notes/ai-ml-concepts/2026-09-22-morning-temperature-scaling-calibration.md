# Temperature Scaling Calibration

**Category:** AI/ML Concepts  
**Date:** 2026-09-22 (morning)

---

# Temperature Scaling for Model Calibration

Temperature scaling is a post‑processing technique that adjusts the confidence of a classifier’s soft‑max outputs without changing the predicted class. By dividing the logits **z** by a learned scalar temperature **T > 0** (i.e., softmax(z / T)), the model’s probability distribution becomes either sharper (T < 1) or smoother (T > 1). The temperature is typically fitted on a held‑out validation set by minimizing the negative log‑likelihood, which aligns predicted confidences with true accuracies.

**Why use it?**  
Modern deep nets are often *over‑confident*, leading to poor reliability in safety‑critical applications such as medical diagnosis, autonomous driving, or active learning. Temperature scaling is simple (one extra parameter), preserves the model’s discriminative ability, and improves calibration metrics like Expected Calibration Error (ECE) and Brier score.

**Typical workflow**  
1. Train the model as usual.  
2. Freeze the model weights.  
3. Optimize **T** on validation logits and labels.  
4. Apply the calibrated soft‑max during inference.

```python
import torch, torch.nn as nn
import torch.nn.functional as F
from torch.optim import LBFGS

class TempScaling(nn.Module):
    def __init__(self):
        super().__init__()
        self.temperature = nn.Parameter(torch.ones(1))

    def forward(self, logits):
        return logits / self.temperature

def calibrate_temperature(model, val_loader):
    model.eval()
    logits, targets = [], []
    with torch.no_grad():
        for x, y in val_loader:
            logits.append(model(x))
            targets.append(y)
    logits = torch.cat(logits)
    targets = torch.cat(targets)

    temp = TempScaling()
    optimizer = LBFGS([temp.temperature], lr=0.01, max_iter=50)

    def loss_fn():
        scaled = temp(logits)
        loss = F.cross_entropy(scaled, targets)
        loss.backward()
        return loss

    optimizer.step(loss_fn)
    return temp.temperature.item()
```

After fitting, divide any new model logits by the learned temperature before applying `softmax`. This yields calibrated probabilities ready for downstream decision‑making.
