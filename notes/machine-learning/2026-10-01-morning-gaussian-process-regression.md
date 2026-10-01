# Gaussian Process Regression

**Category:** Machine Learning  
**Date:** 2026-10-01 (morning)

---

# Gaussian Process Regression

Gaussian Process Regression (GPR) is a non‑parametric Bayesian approach to regression that defines a distribution over functions. Instead of learning a fixed set of parameters, GPR places a **Gaussian process** prior on the latent function \(f(x)\). Any finite collection of function values follows a multivariate normal distribution described by a mean function \(m(x)\) (often set to zero) and a covariance (kernel) function \(k(x, x')\) that encodes similarity between inputs.  

**Why use it?**  
- **Uncertainty quantification:** GPR returns a predictive mean **and** a variance, giving confidence intervals for each prediction.  
- **Flexibility:** By choosing different kernels (RBF, Matern, periodic, etc.) the model can capture smooth, rough, or repeating patterns without changing the model architecture.  
- **Data‑efficient:** Works well on small‑to‑medium datasets where deep nets would overfit.  

**Typical applications** include surrogate modeling for expensive simulations, Bayesian optimization, time‑series forecasting with irregular sampling, and spatial interpolation (kriging) in geostatistics.

### Quick example with scikit‑learn
```python
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, WhiteKernel

# synthetic data
X = np.linspace(0, 5, 20).reshape(-1, 1)
y = np.sin(X).ravel() + 0.1 * np.random.randn(20)

# kernel = RBF (smoothness) + WhiteKernel (noise)
kernel = RBF(length_scale=1.0) + WhiteKernel(noise_level=0.1)
gpr = GaussianProcessRegressor(kernel=kernel, n_restarts_optimizer=10)

gpr.fit(X, y)

# prediction with uncertainty
X_test = np.linspace(-1, 6, 100).reshape(-1, 1)
y_pred, sigma = gpr.predict(X_test, return_std=True)
```
The `y_pred` array gives the mean prediction, while `sigma` provides the standard deviation, useful for plotting confidence bands.

**Takeaway:** GPR offers a principled way to model complex functions with built‑in uncertainty estimates, making it valuable wherever understanding prediction confidence is crucial.
