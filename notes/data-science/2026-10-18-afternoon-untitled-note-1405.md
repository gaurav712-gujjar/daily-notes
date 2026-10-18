# Untitled Note - 1405

**Category:** Data Science  
**Date:** 2026-10-18 (afternoon)

---

# Cox Proportional Hazards Model

The Cox proportional hazards (Cox PH) model is a semi‑parametric regression technique used to study the relationship between survival time (or time‑to‑event) and one or more covariates. Unlike fully parametric models, it does **not** assume a specific baseline hazard function; instead, it models the hazard ratio as an exponential function of the covariates:

\[
h(t|X) = h_0(t) \exp(\beta_1 X_1 + \beta_2 X_2 + \dots)
\]

where \(h_0(t)\) is the unknown baseline hazard and \(\beta\) are coefficients estimated from data.

### When to use it
- **Medical research**: estimating how risk factors (age, treatment, biomarkers) affect patient survival.
- **Customer churn**: predicting time until a user cancels a subscription.
- **Reliability engineering**: modeling failure times of components under varying operating conditions.

Key assumptions:
1. **Proportional hazards** – the hazard ratios between groups remain constant over time.
2. **Independence of censoring** – censored observations are unrelated to the hazard.

### Quick Python example (using `lifelines`)

```python
import pandas as pd
from lifelines import CoxPHFitter

# Example dataset: columns = ['duration', 'event', 'age', 'treatment']
df =
