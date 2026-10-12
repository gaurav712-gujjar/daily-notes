# Kaplan Meier Survival Estimator

**Category:** Data Science  
**Date:** 2026-10-12 (morning)

---

# Kaplan Meier Survival Estimator  

The Kaplan‑Meier estimator is a non‑parametric statistic that estimates the survival function \(S(t)\) – the probability that an event of interest (e.g., failure, churn, death) has **not** occurred by time \(t\). It handles right‑censored data, where the exact event time is unknown because the observation ended early (e.g., a customer is still active at study end). The estimator updates the survival probability at each observed event time \(t_i\) as  

\[
\hat{S}(t) = \prod_{t_i \le t} \left(1 - \frac{d_i}{n_i}\right)
\]

where \(d_i\) is the number of events at \(t_i\) and \(n_i\) is the number of subjects at risk just before \(t_i\).

### Practical uses  
* **Medical research** – estimating patient survival after treatment.  
* **Customer analytics** – predicting churn or product lifetime.  
* **Reliability engineering** – modeling time‑to‑failure of components.  

### Quick Python example (using `lifelines`)  

```python
import pandas as pd
from lifelines import KaplanMeierFitter
import matplotlib.pyplot as plt

# Sample data: duration (days) and event observed flag (1=event, 0=censored)
df = pd.DataFrame({
    'duration': [5, 12, 9, 30, 45, 22, 18, 50],
    'event':    [1, 0, 1, 1, 0, 1, 1, 0]
})

kmf = KaplanMeierFitter()
kmf.fit(durations=df['duration'], event_observed=df['event'])

kmf.plot_survival_function()
plt.title('Kaplan‑Meier Survival Curve')
plt.xlabel('Time (days)')
plt.ylabel('Survival probability')
plt.show()
```

The plotted curve shows the step‑wise decline of survival probability, automatically accounting for censored observations.  

---
