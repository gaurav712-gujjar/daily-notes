# Neural Tangent Kernel

**Category:** Machine Learning  
**Date:** 2026-11-17 (afternoon)

---

# Neural Tangent Kernel (NTK)

**Concept**  
The Neural Tangent Kernel describes the limiting behavior of infinitely wide neural networks trained with gradient descent. As the width of each layer → ∞, the network’s output evolves linearly in function space, and its training dynamics can be expressed analytically by a kernel matrix computed from the network’s architecture and initialization. NTK bridges deep learning and kernel methods, allowing us to predict generalization and convergence without explicit training.

**Practical Use‑Cases**  
- **Theoretical analysis**: Researchers use NTK to prove convergence rates, study over‑parameterization, and compare architectures analytically.  
- **Fast prototyping**: For small datasets, training the NTK directly (via kernel ridge regression) can achieve performance comparable to a full deep net with far less compute.  
- **Architecture search**: By inspecting the NTK spectrum, practitioners can gauge a model’s expressive power before expensive training.

**Simple PyTorch Example**  
```python
import torch
from torch import nn
from torch.nn import functional as F
from neural_tangents import stax, predict

# Define a shallow fully‑connected network
init_fn, apply_fn, kernel_fn = stax.serial(
    stax.Dense(128), stax.Relu(),
    stax.Dense(1)
)

# Random inputs
x_train = torch.randn(100, 20)
y_train = torch.randn(100, 1)

# Compute the NTK matrix on training data
ntk_train = kernel_fn(x_train, None, 'ntk')

# Perform kernel ridge regression (λ = 1e-3)
alpha = torch.linalg.solve(ntk_train + 1e-3 * torch.eye(len(x_train)), y_train)

# Predict on new points
x_test = torch.randn(10, 20)
ntk_test = kernel_fn(x_test, x_train, 'ntk')
y_pred = ntk_test @ alpha
print(y_pred.squeeze())
```
*The `neural_tangents` library (JAX‑based) provides a concise interface; the same idea can be reproduced in pure PyTorch by manually constructing the Jacobian.*

---
