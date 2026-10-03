# Untitled Note - 0922

**Category:** Deep Learning  
**Date:** 2026-10-03 (morning)

---

# Gradient Clipping

Gradient clipping is a technique used to prevent exploding gradients during back‑propagation, especially in very deep networks or recurrent architectures. When the magnitude of gradients becomes excessively large, weight updates can overshoot optimal regions, causing loss divergence or NaNs. Clipping modifies the gradient vector g so that its norm does not exceed a predefined threshold τ:

\[
\tilde{g}= 
\begin{cases}
g & \text{if } \|g\|_2 \le \tau\\
\tau \frac{g}{\|g\|_2} & \text{otherwise}
\end{cases}
\]

**Why it’s used**  
- **RNNs/LSTMs**: Long sequences amplify gradient magnitude, making training unstable.  
- **Very deep CNNs or Transformers**: Large learning rates combined with many layers can produce spikes.  
- **Reinforcement learning**: Policy gradients often have high variance; clipping stabilizes updates.  

**Practical tips**  
- Choose τ between 1.0 and 5.0 for most tasks; tune empirically.  
- Clip by norm (most common) or by value (element‑wise).  
- Integrate with optimizers via a hook or wrapper; many frameworks provide built‑in support.

**Example (PyTorch)**

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.LSTM(input_size=128, hidden_size=256, num_layers=2)
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=1e-3)

for xb, yb in dataloader:
    optimizer.zero_grad()
    output, _ = model(xb)
    loss = criterion(output.view(-1, output.size(-1)), yb.view(-1))
    loss.backward()
    # Clip gradients globally to
