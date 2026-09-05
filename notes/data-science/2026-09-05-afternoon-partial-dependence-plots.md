# Partial Dependence Plots

**Category:** Data Science  
**Date:** 2026-09-05 (afternoon)

---

# Partial Dependence Plots (PDP)

Partial Dependence Plots visualize the average effect of one or two features on a model’s prediction, marginalizing over all other variables. Formally, for a feature *xₖ*, the partial dependence function is  

\[
\hat{f}_{PD}(x_k) = \frac{1}{n}\sum_{i=1}^{n} \hat{f}(x_k, \mathbf{x}_{i}^{\setminus k}),
\]

where \(\mathbf{x}_{i}^{\setminus k}\) are the remaining features of the *i*‑th observation. By plotting \(\hat{f}_{PD}(x_k)\) against \(x_k\), we see how the model responds to changes in that feature, independent of interactions with others.

**Why use PDP?**  
- **Interpretability:** Provides a global, model‑agnostic view of feature influence, useful for stakeholders without deep ML expertise.  
- **Feature engineering:** Reveals non‑linear relationships or saturation points, guiding transformations.  
- **Model debugging:** Detects unexpected monotonicity or artifacts caused by data leakage.

**When to apply:**  
PDPs work best with moderately sized datasets and models that are not highly sensitive to feature interactions; for strong interactions, consider Individual Conditional Expectation (ICE) plots.

```python
import matplotlib.pyplot as plt
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.inspection import partial_dependence, PartialDependenceDisplay
from sklearn.datasets import fetch_california_housing

X, y = fetch_california_housing(return_X_y=True)
model = GradientBoostingRegressor().fit(X, y)

features = [0, 5]          # MedianIncome and Latitude
PartialDependenceDisplay.from_estimator(
    model, X, features, kind='average')
plt.suptitle('Partial Dependence of Median Income & Latitude')
plt.show()
```

The code fits a Gradient Boosting model on the California housing data and draws PDPs for *MedianIncome* and *Latitude*, illustrating their average impact on predicted house prices.
