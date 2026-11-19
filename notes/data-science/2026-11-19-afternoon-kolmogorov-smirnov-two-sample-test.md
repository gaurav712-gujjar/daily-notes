# Kolmogorov Smirnov Two‑Sample Test

**Category:** Data Science  
**Date:** 2026-11-19 (afternoon)

---

# Kolmogorov‑Smirnov Two‑Sample Test

The Kolmogorov‑Smirnov (KS) two‑sample test is a non‑parametric hypothesis test that compares the empirical distribution functions of two independent samples. It quantifies the maximum absolute difference **D** between the cumulative distributions. The null hypothesis states that both samples are drawn from the same continuous distribution; a large **D** (and small p‑value) leads to rejection.

**Why it matters**  
- **Distribution validation**: Verify that a training set and a hold‑out set share the same underlying distribution before model building.  
- **Feature drift detection**: In production, compare current feature values against a baseline to spot covariate shift.  
- **A/B testing**: Assess whether two user groups exhibit similar behavior distributions (e.g., session lengths).

**Python example (SciPy)**

```python
import numpy as np
from scipy.stats import ks_2samp

# Simulated data
np.random.seed(0)
control = np.random.normal(loc=0, scale=1, size=500)
variant = np.random.normal(loc=0.2, scale=1, size=500)

# KS two‑sample test
stat, p_value = ks_2samp(control, variant)

print(f"KS statistic = {stat:.4f}")
print(f"P‑value      = {p_value:.4f}")
```

If `p_value < 0.05`, we conclude the two samples likely come from different distributions, prompting further investigation or model retraining.

---
