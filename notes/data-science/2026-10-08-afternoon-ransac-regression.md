# RANSAC Regression

**Category:** Data Science  
**Date:** 2026-10-08 (afternoon)

---

# RANSAC Regression  

**Concept**  
RANSAC (Random Sample Consensus) is an iterative algorithm for fitting a model to data that may contain a large proportion of outliers. At each iteration, it randomly selects a minimal subset of observations, fits the model, and then determines how many data points fit this model within a tolerance (the “inliers”). The model with the largest consensus set is retained as the final estimate.

**Why / Where Used**  
- **Robust regression** when measurements are corrupted by gross errors (e.g., sensor glitches).  
- **Computer vision** for estimating geometric transforms (homographies, fundamental matrix).  
- **Geospatial analysis** where GPS readings include occasional large deviations.  
RANSAC trades a deterministic solution for resilience; it does not assume a particular outlier distribution and works well when outliers dominate.

**Quick Example (scikit‑learn)**  

```python
import numpy as np
from sklearn.linear_model import RANSACRegressor, LinearRegression
import matplotlib.pyplot as plt

# synthetic data: line + outliers
rng = np.random.RandomState(0)
X = np.linspace(0, 10, 100)[:, None]
y = 2.5 * X.squeeze() + 1.0 + rng.normal(scale=0.5, size=100)
y[::10] += rng.normal(scale=10, size=10)          # inject outliers

# RANSAC fitting
ransac = RANSACRegressor(base_estimator=LinearRegression(),
                         residual_threshold=2.0,
                         random_state=0)
ransac.fit(X, y)

inlier_mask = ransac.inlier_mask_
outlier_mask = ~inlier_mask

# plot
plt.scatter(X[inlier_mask], y[inlier_mask], color='green', label='Inliers')
plt.scatter(X[outlier_mask], y[outlier_mask], color='red',   label='Outliers')
line_X = np.arange(0, 10, 0.1)[:, None]
plt.plot(line_X, ransac.predict(line_X), color='blue', linewidth=2,
         label='RANSAC fit')
plt.legend()
plt.show()
```

The plot shows the algorithm discarding the red outliers and fitting a reliable line to the green inliers.  

---
