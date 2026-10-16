# Partial Least Squares Regression

**Category:** Data Science  
**Date:** 2026-10-16 (morning)

---

# Partial Least Squares Regression (PLS)

Partial Least Squares Regression (PLS) is a linear modeling technique that finds latent components explaining both predictor (X) and response (Y) variance simultaneously. Unlike ordinary least squares, which may suffer when predictors are highly collinear or when p ≫ n, PLS projects X and Y onto a lower‑dimensional space, then performs regression on these components. The algorithm maximizes the covariance between the projected X‑scores and Y‑scores, yielding directions that are most predictive of the outcome.

**When to use PLS**

- **High‑dimensional data**: spectroscopy, genomics, or chemometrics where the number of variables far exceeds observations.  
- **Multicollinearity**: when predictors are strongly correlated, PLS stabilizes coefficient estimates.  
- **Interpretability**: latent components can be examined to understand which groups of variables drive the response.  

**Quick example with scikit‑learn**

```python
import numpy as np
from sklearn.cross_decomposition import PLSRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

# Simulated data: 100 samples, 50 highly correlated features
np.random.seed(0)
X = np.random.randn(100, 50)
X = X @ np.random.randn(50, 5)  # induce collinearity
y = X[:, 0] * 2.5 + np.random.randn(100) * 0.5   # continuous target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pls = PLSRegression(n_components=5)
pls.fit(X_train, y_train)
y_pred = pls.predict(X_test)

print("R² on test set:", r2_score(y_test, y_pred))
```

The `n_components` parameter controls the number of latent variables; cross‑validation helps select an optimal value. PLS bridges the gap between dimensionality reduction (like PCA) and predictive modeling, making it a go‑to method for many scientific and engineering regression problems.
