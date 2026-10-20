# Untitled Note - 0848

**Category:** Machine Learning  
**Date:** 2026-10-20 (morning)

---

# Sharpness‑Aware Minimization (SAM)

Sharpness‑Aware Minimization is an optimizer augmentation that seeks model parameters lying in **wide, flat minima** of the loss landscape, which tend to generalize better than sharp minima. Instead of minimizing the loss at the current point θ, SAM first perturbs the parameters in the direction that **maximizes** the loss within a bounded ℓ₂‑ball of radius ρ, then updates θ to **minimize** this worst‑case loss. Formally:

\[
\min_{\theta}\; \max_{\|\epsilon\|_2\le\rho}\; L(\theta + \epsilon)
\]

The inner maximization pushes the parameters toward the steepest ascent within the ball, while the outer minimization pulls them back, encouraging flatness.

### Practical use‑cases
- **Computer vision** models (ResNet, ViT) where small gains in top‑1 accuracy matter.  
- **Natural language processing** fine‑tuning, especially on limited data.  
- Situations where **robustness to distribution shift** or adversarial perturbations is desired, because flat minima are less sensitive to input noise.

### Minimal PyTorch implementation

```python
import torch, torch.nn as nn, torch.optim as optim

model = nn.Sequential(nn.Linear(784, 256), nn.ReLU(),
                      nn.Linear(256, 10)).to('cuda')
criterion = nn.CrossEntropyLoss()
base_opt = optim.SGD(model.parameters(), lr=0.1, momentum=0.9)
rho = 0.05                      # SAM radius

for X, y in loader:            # X: [B,784], y: [B]
    X, y = X.cuda(), y.cuda()
    # ---- first forward ----
    loss = criterion(model(X), y)
    loss.backward()
    # ---- compute epsilon (worst‑case perturbation
