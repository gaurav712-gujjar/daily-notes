# Elastic Net Regularization

**Category:** Machine Learning  
**Date:** 2026-09-08 (afternoon)

---

# Elastic Net Regularization

Elastic Net combines L1 (Lasso) and L2 (Ridge) penalties into a single regularizer:

\[
\Omega(\mathbf w)=\alpha \left[ \lambda_1 \|\mathbf w\|_1 + (1-\lambda_1)\|\mathbf w\|_2^2 \right]
\]

where α controls overall strength and λ₁∈[0,1] balances the two norms.  
The L1 part encourages sparsity (feature selection), while the L2 part stabilizes coefficients when predictors are highly correlated. This hybrid behaves like Lasso when λ₁≈1 and like Ridge when λ₁≈0, offering a flexible compromise.

**Why use it?**  
- **Correlated features:** Pure Lasso may arbitrarily keep one variable and discard others; Elastic Net tends to keep groups of correlated variables together.  
- **High‑dimensional data:** In genomics or text mining, where p≫n, the combined penalty yields more reliable models than either penalty alone.  
- **Model interpretability + robustness:** You retain a sparse model without sacrificing predictive performance.

**Practical example (scikit‑learn):**

```python
from sklearn.linear_model import ElasticNet
from sklearn.datasets import make_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

X, y = make_regression(n_samples=200, n_features=100, noise=0.5, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# α = 0.1 controls overall regularization, l1_ratio = 0.7 => 70% L1, 30% L2
model = ElasticNet(alpha=0.1, l1_ratio=0.7, random_state=0)
model.fit(X_train, y_train)

pred = model.predict(X_test)
print("MSE:", mean_squared_error(y_test, pred))
print("Non‑zero coefficients:", (model.coef_ != 0).sum())
```

The output shows a reduced number of active features while maintaining low error, illustrating Elastic Net’s balance between sparsity and stability.
