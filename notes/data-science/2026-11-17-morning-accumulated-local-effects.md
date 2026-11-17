# Accumulated Local Effects

**Category:** Data Science  
**Date:** 2026-11-17 (morning)

---

# Accumulated Local Effects (ALE) Plots  

**What it is**  
Accumulated Local Effects (ALE) plots are a model‑agnostic tool for visualizing the marginal effect of a feature on a prediction while accounting for feature interactions. Unlike Partial Dependence Plots, ALE estimates the effect by integrating *local* differences of the model predictions over the distribution of the feature, which avoids extrapolation into regions with little or no data.

**Why / Where it’s used**  
- Interpreting complex black‑box models (e.g., gradient boosting, random forests, deep nets).  
- Detecting non‑linear relationships and interaction‑driven shifts without the bias of PD plots.  
- Situations with correlated features where PD plots become unreliable.  

**Quick example (Python, scikit‑learn + pyALE)**  

```python
import pandas as pd
from sklearn.datasets import fetch_california_housing
from sklearn.ensemble import GradientBoostingRegressor
from pyale import ale_plot

# Load data and train a model
X, y = fetch_california_housing(return_X_y=True, as_frame=True)
model = GradientBoostingRegressor(random_state=0).fit(X, y)

# Plot ALE for the feature "MedInc" (median income)
ale_plot(
    model,                     # fitted estimator
    X,                         # original data
    feature="MedInc",          # feature to explain
    bins=20,                   # number of intervals
    plot_kwargs=dict(figsize=(6,4))
)
```

The resulting curve shows how changes in *MedInc* locally shift the predicted house price, accumulated across the data distribution. ALE plots are especially helpful when you need trustworthy, interaction‑aware explanations for high‑dimensional, correlated datasets.  

---
