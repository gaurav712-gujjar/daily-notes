# MICE Imputation

**Category:** Data Science  
**Date:** 2026-10-26 (afternoon)

---

# MICE (Multiple Imputation by Chained Equations)

Multiple Imputation by Chained Equations (MICE) is a statistical technique for handling missing data. Instead of discarding incomplete rows or filling all gaps with a single estimate, MICE creates several complete datasets by iteratively modeling each variable with missing values as a function of the others. After running the analysis on each imputed dataset, results are pooled, reflecting the uncertainty introduced by the missingness.

**Why use MICE?**  
- **Preserves data variability:** By generating multiple plausible values, it avoids the overly optimistic variance reduction of single imputation.  
- **Flexibility:** Each column can be imputed with a model suited to its type (linear regression for continuous, logistic for binary, etc.).  
- **Compatibility with downstream pipelines:** The imputed datasets can be fed directly into scikit‑learn models, preserving the original feature engineering steps.

**Typical workflow**  
1. Identify columns with missing values.  
2. Choose appropriate models for each column.  
3. Run the chained equations for a fixed number of iterations (default 10).  
4. Produce *m* imputed datasets (commonly 5).  
5. Fit the predictive model on each dataset and combine coefficients using Rubin’s rules.

**Python example (scikit‑learn IterativeImputer)**

```python
import pandas as pd
from sklearn.experimental import enable_iterative_imputer  # noqa
from sklearn.impute import IterativeImputer
from sklearn.linear_model import BayesianRidge

# Sample data with missing values
df = pd.read_csv('housing.csv')
X = df.drop('price', axis=1)

# MICE imputer: BayesianRidge as default estimator
mice = IterativeImputer(
    estimator=BayesianRidge(),
    max_iter=10,
    random_state=42
)

X_imputed = mice.fit_transform(X)
X_imputed = pd.DataFrame(X_imputed, columns=X.columns)
```

In practice, MICE is widely adopted in epidemiology, social sciences, and any domain where missingness is non‑random and preserving statistical inference is critical.
