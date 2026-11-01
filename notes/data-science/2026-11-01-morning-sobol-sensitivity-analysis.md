# Sobol Sensitivity Analysis

**Category:** Data Science  
**Date:** 2026-11-01 (morning)

---

# Sobol Sensitivity Analysis

Sobol sensitivity analysis is a variance‑based global method that quantifies how each input variable (and their interactions) contributes to the output variance of a model. It decomposes the total variance **V(Y)** into first‑order effects **S_i** (the portion caused by a single factor) and higher‑order effects **S_{i,j,...}** (joint contributions). The sum of all Sobol indices equals 1, giving a clear picture of which features dominate the model’s behavior.

**Why use it?**  
- **Model‑agnostic:** Works with any deterministic or stochastic model (e.g., simulation, neural network).  
- **Interaction insight:** Reveals not only the importance of individual variables but also how they interact.  
- **Robustness:** Unlike local methods (e.g., gradient‑based), Sobol indices remain reliable across the entire input space, making them ideal for risk assessment, calibration, and feature selection in engineering, finance, and environmental modeling.

**Quick Python example (using SALib):**

```python
from SALib.sample import saltelli
from SALib.analyze import sobol
import numpy as np

# Define the problem
problem = {
    'num_vars': 3,
    'names': ['x1', 'x2', 'x3'],
    'bounds': [[-1, 1], [0, 5], [10, 20]]
}

# Generate samples
param_values = saltelli.sample(problem, 1000, calc_second_order=True)

# Model: simple nonlinear function
def model(X):
    return X[:,0]**2 + np.sin(X[:,1]) + np.log(X[:,2])

Y = model(param_values)

# Perform Sobol analysis
Si = sobol.analyze(problem, Y, calc_second_order=True)

print('First‑order indices:', Si['S1'])
print('Total‑order indices:', Si['ST'])
```

The output shows each variable’s first‑order and total contribution, guiding decisions such as reducing model complexity or focusing data collection on influential parameters.

---
