# Neural Ordinary Differential Equations

**Category:** AI/ML Concepts  
**Date:** 2026-09-16 (afternoon)

---

# Neural Ordinary Differential Equations

Neural Ordinary Differential Equations (Neural ODEs) reinterpret the forward pass of a deep network as solving an initial‑value problem of an ordinary differential equation. Instead of stacking discrete layers, a continuous dynamics function **f(·,θ)** parameterized by neural weights **θ** defines the derivative of the hidden state **h(t)**:

\[
\frac{dh(t)}{dt}=f\bigl(h(t),t;\theta\bigr),\qquad h(0)=h_0
\]

The output is obtained by integrating this ODE from time 0 to a final time **T** using a numerical solver (e.g., Runge‑Kutta). This formulation yields memory‑efficient training via the adjoint sensitivity method, which back‑propagates gradients by solving a reverse‑time ODE instead of storing intermediate activations.

### When to use Neural ODEs
- **Irregularly sampled time‑series** where observations arrive at non‑uniform intervals.  
- **Continuous‑time generative modeling** (e.g., continuous normalizing flows).  
- **Parameter‑efficient models**: a single ODE block can replace dozens of conventional layers, reducing the number of learnable parameters.  
- **Physics‑informed learning** where known differential equations guide the network’s dynamics.

### Minimal PyTorch example

```python
import torch
from torchdiffeq import odeint

class ODEFunc(torch.nn.Module):
    def __init__(self, dim):
        super().__init__()
        self.net = torch.nn.Sequential(
            torch.nn.Linear(dim, 64),
            torch.nn.Tanh(),
            torch.nn.Linear(64, dim)
        )
    def forward(self, t, h):
        return self.net(h)

# initial hidden state
h0 = torch.randn(1, 5)
t = torch.linspace(0., 1., 100)          # integration times
func = ODEFunc(dim=5)

# forward pass = solve ODE
h_T = odeint(func, h0, t)[-1]            # state at final time
print(h_T.shape)                         # -> torch.Size([1, 5])
```

In this snippet, `odeint` integrates the learned dynamics from `t=0` to `t=1`. The adjoint method automatically computes gradients for `func` during training.

---
