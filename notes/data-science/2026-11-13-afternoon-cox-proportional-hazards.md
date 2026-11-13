# Cox Proportional Hazards

**Category:** Data Science  
**Date:** 2026-11-13 (afternoon)

---

# Cox Proportional Hazards Model

The Cox proportional hazards (PH) model is a semi‑parametric regression technique used to study the relationship between a set of covariates and the time until an event occurs (e.g., failure, death). Unlike fully parametric survival models, the Cox model does not assume a specific baseline hazard function; instead, it estimates hazard ratios that are assumed constant over time (the *proportional hazards* assumption).

**Why it’s used**  
- **Medical research**: Quantify how risk factors (age, treatment, biomarkers) affect patient survival.  
- **Reliability engineering**: Model failure times of components under varying operating conditions.  
- **Customer churn**: Predict the time until a user cancels a subscription based on usage metrics.  

The model yields interpretable coefficients: a positive coefficient indicates a higher hazard (shorter expected survival), while a negative coefficient suggests a protective effect.

```python
# Example: fitting a Cox PH model with lifelines
import pandas as pd
from lifelines import CoxPHFitter

# Load a sample dataset (duration, event observed, covariates)
df = pd.read_csv('https://raw.githubusercontent.com/CamDavidsonPilon/ML-'
                 'Data-Science/master/medical/heart_failure_clinical_records_dataset.csv')
df.rename(columns={'DEATH_EVENT': 'event', 'time': 'duration'}, inplace=True)

cph = CoxPHFitter()
cph.fit(df, duration_col='duration', event_col='event')
cph.print_summary()          # shows hazard ratios and p‑values
cph.plot()                   # visualizes coefficients
```

The output includes hazard ratios (exp(coef)) and statistical tests to assess each covariate’s significance, enabling data‑driven decision making in time‑to‑event problems.  

---
