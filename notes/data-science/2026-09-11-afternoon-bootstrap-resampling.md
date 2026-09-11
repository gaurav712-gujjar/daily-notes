# Bootstrap Resampling

**Category:** Data Science  
**Date:** 2026-09-11 (afternoon)

---

# Bootstrap Resampling

Bootstrap is a non‑parametric statistical technique that creates many “new” datasets by sampling **with replacement** from the original data. Each resample has the same size as the original, but because of replacement, some observations appear multiple times while others may be omitted. By computing a statistic (e.g., mean, regression coefficient, model accuracy) on each bootstrap replicate, we obtain an empirical distribution that approximates the sampling distribution of that statistic.  

**Why use it?**  
- **Uncertainty estimation** when analytic formulas are unavailable or unreliable.  
- **Confidence intervals** for complex estimators (e.g., median, quantiles).  
- **Model validation** for small or imbalanced datasets where traditional splits would waste data.  
- **Feature importance stability** by repeatedly fitting models on bootstrapped samples.  

**Practical example** – estimating a 95 % confidence interval for the mean of a numeric column:

```python
import numpy as np

def bootstrap_ci(data, n_boot=1000, alpha=0.05):
    rng = np.random.default_rng()
    boots = rng.choice(data, size=(n_boot, len(data)), replace=True)
    means = boots.mean(axis=1)
    lower = np.percentile(means, 100 * (alpha/2))
    upper = np.percentile(means, 100 * (1 - alpha/2))
    return lower, upper

# usage
x = np.array([5.1, 4.9, 5.0, 5.2, 5.3])
ci_low, ci_high = bootstrap_ci(x)
print(f"95% CI for the mean: ({ci_low:.2f}, {ci_high:.2f})")
```

The function draws 1,000 bootstrap samples, computes their means, and reports the percentile‑based confidence interval. This simple tool scales to any statistic, making bootstrap a versatile workhorse in modern data science.
