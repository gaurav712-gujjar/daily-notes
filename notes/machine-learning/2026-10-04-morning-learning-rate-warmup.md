# Learning Rate Warmup

**Category:** Machine Learning  
**Date:** 2026-10-04 (morning)

---

# Learning Rate Warmup

Learning rate warmup is a training technique that gradually increases the optimizer’s learning rate from a small value to the target learning rate over the first few training iterations or epochs. Instead of starting with the full learning rate, which can cause unstable updates—especially in large‑batch or transformer‑based models—the warmup phase smooths the early optimization steps, allowing the model to settle into a reasonable region of the loss landscape before aggressive learning begins.

**Why use it?**  
- **Stability with large batches:** Large‑batch training often suffers from divergence at the start; warmup mitigates this.  
- **Transformer models:** Architectures like BERT and GPT rely on warmup to handle the high variance of gradients early on.  
- **Preventing sharp minima:** A gradual ramp‑up can guide optimization toward flatter minima, improving generalization.

**Typical schedule**  
A common schedule is linear warmup:  
\[
\eta_t = \eta_{\text{base}} \times \frac{t}{T_{\text{warmup}}}
\]  
where \( \eta_t \) is the learning rate at step \( t \), \( \eta_{\text{base}} \) the target learning rate, and \( T_{\text{warmup}} \) the number of warmup steps.

**Code example (PyTorch)**

```python
import torch
from torch.optim import AdamW
from torch.optim.lr_scheduler import LambdaLR

model = ...  # your neural net
optimizer = AdamW(model.parameters(), lr=1e-3)

warmup_steps = 500
total_steps = 10000

# Lambda function defines the LR multiplier at each step
lr_lambda = lambda step: min((step + 1) / warmup_steps, 1.0)

scheduler = LambdaLR(optimizer, lr_lambda)

for step in range(total_steps):
    loss = compute_loss(model, batch)
    loss.backward()
    optimizer.step()
    scheduler.step()          # updates LR according to warmup schedule
    optimizer.zero_grad()
```

In this snippet, the learning rate linearly rises for the first 500 steps, then stays at the base value for the remaining training.

**When to apply**  
- Training large language models or vision transformers.  
- Using very high batch sizes (e.g., > 1024).  
- When initial loss spikes indicate instability.

Warmup is a lightweight addition that often yields noticeable gains in convergence speed and final model quality.
