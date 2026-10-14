# M-Estimators for Robust Regression

**Category:** Data Science  
**Date:** 2026-10-14 (afternoon)

---

# M‑Estimators for Robust Regression

M‑estimators are a generalization of maximum‑likelihood estimators that replace the squared‑error loss with a less‑sensitive ρ‑function. By down‑weighting large residuals, they reduce the influence of outliers on the fitted model, offering a robust alternative to ordinary least squares (OLS). Common ρ‑functions include Huber, Tukey’s biweight, and Cauchy. The corresponding influence function ψ = ∂ρ/∂r determines how each residual r contributes to the parameter update.

**Why use it?**  
- Datasets with mislabeled points, sensor glitches, or heavy‑tailed error distributions.  
- Situations where OLS coefficients become unstable or misleading due to a few extreme values.  
- Pre‑processing step before more complex models; a robust linear baseline can reveal true trends.

**Typical workflow**  
1. Choose a robust loss (e.g., Huber with tuning parameter δ).  
2. Fit the model by iteratively re‑weighted least squares (IRLS): each iteration computes weights w_i = ψ(r_i)/r_i and solves a weighted least‑squares problem.  
3. Evaluate residual diagnostics; adjust δ if necessary.

**Python example (statsmodels)**

```python
import numpy as np
import statsmodels.api as sm

# synthetic data with outliers
np.random.seed(0)
X = np.random.randn(100, 1)
y = 3 * X.squeeze() + np.random.randn(100) * 0.5
y[::10] += 10  # inject outliers

X = sm.add_constant(X)          # add intercept term
model = sm.RLM(y, X, M=sm.robust.norms.HuberT(t=1.35))
results = model.fit()
print(results.params)  # robust intercept & slope
```

The `RLM` class implements IRLS automatically, yielding coefficients that are far less affected by the injected outliers than OLS would be.
