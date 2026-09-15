# Permutation Test

**Category:** Data Science  
**Date:** 2026-09-15 (afternoon)

---

# Permutation Test (Randomization Test)

A permutation test is a non‑parametric statistical method that evaluates the null hypothesis by repeatedly shuffling (permuting) the labels of the data and recomputing the test statistic each time. The proportion of permuted statistics that are at least as extreme as the observed statistic estimates the p‑value. Because it makes no distributional assumptions (e.g., normality), the permutation test is robust to outliers and skewed data.

**When to use it**  
- Comparing means, medians, or any custom statistic between two (or more) groups when classical assumptions are doubtful.  
- Assessing feature importance in a model by permuting a feature’s values and measuring the drop in performance (a form of model‑agnostic interpretation).  
- Small‑sample experiments where analytical p‑values are unreliable.

**Key steps**  
1. Compute the statistic of interest on the original data (e.g., difference of means).  
2. Randomly permute the group labels and recompute the statistic; repeat many times (≥ 1,000).  
3. The p‑value = #(permuted ≥ observed) / #permutations.

```python
import numpy as np
from itertools import repeat

def permutation_test(x, y, n_perm=5000, stat=np.mean):
    obs = stat(x) - stat(y)
    combined = np.concatenate([x, y])
    count = 0
    for _ in range(n_perm):
        np.random.shuffle(combined)
        new_x, new_y = combined[:len(x)], combined[len(x):]
        if (stat(new_x) - stat(new_y)) >= obs:
            count += 1
    return count / n_perm

# Example
group_a = np.array([5.1, 4.9, 5.0, 5.2])
group_b = np.array([4.6, 4.8, 4.7, 4.5])
p = permutation_test(group_a, group_b)
print(f"P‑value ≈ {p:.3f}")
```

The permutation test provides an intuitive, distribution‑free way to quantify statistical significance, making it a valuable tool in exploratory data analysis and rigorous scientific reporting.
