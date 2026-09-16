# Quantile Regression

**Category:** Data Science  
**Date:** 2026-09-16 (morning)

---

# Quantile Regression

Quantile regression estimates the conditional quantiles (e.g., median, 90th percentile) of a response variable instead of its mean. Unlike ordinary least‑squares, which minimizes the sum of squared residuals, quantile regression minimizes an asymmetric loss called the **pinball loss**, giving different penalties for over‑ and under‑predictions. This yields a more complete picture of the distribution, especially when the data are heteroscedastic or contain outliers.

**When to use it**

- Modeling risk‑sensitive targets (e.g., Value‑at‑Risk in finance).  
- Understanding how predictors affect the tails of a distribution (e.g., extreme house prices).  
- Building prediction intervals without assuming normality.  

**Python example (sklearn GradientBoostingRegressor)**

```python
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.model_selection import train_test_split

X, y = np.loadtxt('housing.csv', delimiter=',', unpack=True)  # placeholder
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 0.5 quantile = median, 0.9 quantile = 90th percentile
median_reg = GradientBoostingRegressor(loss='quantile', alpha=0.5, n_estimators=200)
p90_reg    = GradientBoostingRegressor(loss='quantile', alpha=0.9, n_estimators=200)

median_reg.fit(X_train, y_train)
p90_reg.fit(X_train, y_train)

median_pred = median_reg.predict(X_test)
p90_pred    = p90_reg.predict(X_test)
```

The two models give point estimates for the 50 % and 90 % conditional quantiles, allowing you to construct asymmetric prediction intervals or examine how features shift the distribution’s shape.  

---
