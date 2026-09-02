# Label Smoothing

**Category:** Deep Learning  
**Date:** 2026-09-02 (afternoon)

---

# Label Smoothing

Label smoothing is a regularization technique that softens the hard one‑hot targets used in classification. Instead of assigning a probability of 1 to the correct class and 0 to all others, the target distribution is blended with a uniform distribution:

\[
y_{\text{smooth}} = (1 - \epsilon) \cdot y_{\text{one‑hot}} + \epsilon / K
\]

where \( \epsilon \) (typically 0.1) is the smoothing factor and \( K \) is the number of classes. The resulting target vector contains values like 0.9 for the true class and 0.01 for each of the 99 other classes in a 100‑class problem.

### Why use it?
- **Reduces over‑confidence:** Models trained with hard targets often output near‑certain predictions, which hurts calibration and generalization. Smoothing spreads probability mass, encouraging the network to be less certain.
- **Improves robustness:** Slightly penalizing over‑confident logits can make the model more tolerant to label noise and adversarial attacks.
- **Boosts performance:** Empirically, many vision and language models (e.g., ResNet, BERT) achieve higher accuracy when label smoothing is applied.

### Quick PyTorch example
```python
import torch
import torch.nn as nn
import torch.nn.functional as F

criterion = nn.CrossEntropyLoss(label_smoothing=0.1)  # ε = 0.1

logits = torch.randn(8, 5)            # batch of 8, 5 classes
targets = torch.tensor([1, 3, 0, 2, 4, 1, 2, 0])

loss = criterion(logits, targets)
loss.backward()
```
The `CrossEntropyLoss` with `label_smoothing` automatically creates the softened target distribution, so no manual preprocessing is needed.

**Bottom line:** Label smoothing is a lightweight, plug‑and‑play regularizer that yields better‑calibrated and often more accurate deep classifiers.
