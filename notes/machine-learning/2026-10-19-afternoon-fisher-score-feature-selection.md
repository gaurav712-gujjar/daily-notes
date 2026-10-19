# Fisher Score Feature Selection

**Category:** Machine Learning  
**Date:** 2026-10-19 (afternoon)

---

# Fisher Score Feature Selection

The **Fisher Score** evaluates each feature independently by measuring how well it separates classes. For a given feature \(x\), the score is  

\[
S(x)=\frac{\sum_{c=1}^{C} n_c(\mu_{c}-\mu)^2}{\sum_{c=1}^{C} n_c\sigma_{c}^{2}}
\]

where \(n_c\) is the number of samples in class \(c\), \(\mu_c\) and \(\sigma_c^2\) are the mean and variance of the feature within that class, and \(\mu\) is the overall mean. A high Fisher score means the feature’s values are tightly clustered within each class but far apart between classes, making it a strong discriminative attribute.

### When to use it
- **High‑dimensional data** (e.g., text, genomics) where a quick, model‑agnostic filter is needed.  
- **Pre‑processing step** before training linear models, k‑NN, or tree‑based learners to reduce overfitting and improve speed.  
- Situations where **interpretability** matters, because the score ranks individual features directly.

### Quick Python example
```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.feature_selection import SelectKBest
from sklearn.feature_selection import f_classif   # Fisher score = ANOVA F‑value

X, y = load_iris(return_X_y=True)

# Keep the 2 most discriminative features
selector = SelectKBest(score_func=f_classif, k=2)
X_new = selector.fit_transform(X, y)

print("Selected feature indices:", selector.get_support(indices=True))
print("Fisher scores:", selector.scores_)
```
The `f_classif` function computes exactly the Fisher (ANOVA F) score for each column, allowing you to pick the top‑k features effortlessly.

**Key take‑away:** Fisher Score offers a fast, statistically grounded way to prune irrelevant dimensions, often boosting downstream model performance with minimal overhead.
