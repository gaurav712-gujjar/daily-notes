# Permutation Feature Importance

**Category:** Data Science  
**Date:** 2026-08-31 (afternoon)

---

# Permutation Feature Importance

Permutation Feature Importance (PFI) measures how much a model’s predictive performance degrades when a single feature’s values are randomly shuffled. By breaking the relationship between that feature and the target, the increase in error directly reflects the feature’s contribution to the model. Unlike built‑in importance scores (e.g., tree‑based Gini importance), PFI is model‑agnostic and works with any estimator that can produce a scoring metric.

**Why use it?**  
- **Model‑agnostic:** Works for linear models, ensembles, neural nets, etc.  
- **Interpretability:** Provides an intuitive “drop in performance” metric that stakeholders can easily understand.  
- **Detects leakage:** If shuffling a feature does not change performance, the feature may be redundant or leaking information already captured elsewhere.

**Typical workflow**  
1. Train the model on the original data.  
2. Compute baseline metric (e.g., accuracy, RMSE).  
3. For each feature, shuffle its column, predict, and recompute the metric.  
4. Importance = shuffled metric – baseline metric (higher = more important).

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
from sklearn.inspection import permutation_importance
import pandas as pd

X, y = pd.read_csv('house_prices.csv').drop('price', axis=1), pd.read_csv('house_prices.csv')['price']
model = RandomForestRegressor(random_state=42).fit(X, y)

baseline = mean_squared_error(y, model.predict(X), squared=False)
result = permutation_importance(model, X, y,
                                scoring='neg_root_mean_squared_error',
                                n_repeats=5, random_state=0)

# Display sorted importances
importances = pd.Series(result.importances_mean, index=X.columns).sort_values(ascending=False)
print(importances)
```

The output ranks features by how much the model’s RMSE increases when each column is permuted, giving a clear, data‑driven view of feature relevance.
