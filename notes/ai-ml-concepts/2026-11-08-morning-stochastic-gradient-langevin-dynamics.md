# Stochastic Gradient Langevin Dynamics

**Category:** AI/ML Concepts  
**Date:** 2026-11-08 (morning)

---

# Stochastic Gradient Langevin Dynamics (SGLD)

Stochastic Gradient Langevin Dynamics blends stochastic gradient descent (SGD) with a controlled amount of injected Gaussian noise, turning the optimizer into a sampler from the Bayesian posterior of a model’s parameters. At each iteration the update rule is  

\[
\theta_{t+1}= \theta_t - \frac{\epsilon}{2}\nabla_{\theta}\mathcal{L}(\theta_t) + \sqrt{\epsilon}\,\xi_t,
\]

where ε is the learning‑rate and ξₜ ∼ 𝒩(0, I) is random noise. The noise term prevents the optimizer from collapsing to a single point estimate, allowing exploration of multiple high‑probability regions in weight space.

**Why use SGLD?**  
- **Bayesian deep learning**: Provides a cheap way to approximate posterior predictive distributions without expensive MCMC.  
- **Uncertainty estimation**: The sampled weight trajectories yield predictive variance, useful for safety‑critical applications.  
- **Regularization**: The stochastic perturbations act as an implicit regularizer, often improving generalization on small datasets.

**Typical use‑cases**  
- Posterior predictive checks in computer vision or NLP models.  
- Model‑based reinforcement learning where calibrated uncertainty guides exploration.  
- Small‑scale problems where full variational inference is overkill.

**Simple PyTorch example**

```python
import torch
import torch.nn as nn
import torch.optim as optim

model = nn.Linear(10, 1)
criterion = nn.MSELoss()
optimizer = optim.SGD(model.parameters(), lr=1e-3)

def sgld_step():
    optimizer.zero_grad()
    outputs = model(x_batch)
    loss = criterion(outputs, y_batch)
    loss.backward()
    # SGD step
    optimizer.step()
    # Add Gaussian noise to each parameter
    with torch.no_grad():
        for p in model.parameters():
            p.add_(torch.randn_like(p) * (optimizer.param_groups[0]['lr'] ** 0.5))

# training loop
for epoch in range(epochs):
    for x_batch, y_batch in loader:
        sgld_step()
```

The code performs a standard SGD update then perturbs each weight with scaled Gaussian noise, turning the optimizer into an SGLD sampler.
