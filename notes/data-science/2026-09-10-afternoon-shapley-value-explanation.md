# Shapley Value Explanation

**Category:** Data Science  
**Date:** 2026-09-10 (afternoon)

---

# Shapley Value Feature Importance

**What it is**  
Shapley values come from cooperative game theory and assign each feature a fair contribution to a model’s prediction. For a given instance, the Shapley value of a feature is the average marginal gain in prediction when that feature is added to every possible subset of the remaining features.  

**Why/where it’s used**  
- **Model‑agnostic interpretability** – works with trees, linear models, neural nets, etc.  
- **Global insight** – aggregating Shapley values over many rows reveals which features drive overall performance.  
- **Regulatory compliance** – provides a mathematically sound justification for automated decisions (e.g., credit scoring).  
- **Debugging** – highlights unexpected feature influence, helping to detect data leakage or bias.

**Quick example with the `shap` library**

```python
import shap, xgboost, pandas as pd
X, y = shap.datasets.boston()
model = xgboost.XGBRegressor().fit(X, y)

# Explain the model on the training data
explainer = shap.Explainer(model, X)
shap_values = explainer(X.iloc[:5])   # first 5 rows

# Visualize contributions for the first instance
shap.plots.waterfall(shap_values[0])
```

The waterfall plot shows each feature’s Shapley value, indicating how it pushes the prediction higher or lower relative to the model’s base value (the average prediction). By averaging `shap_values` across rows, you obtain a global feature importance ranking that is consistent, additive, and theoretically grounded.

---
