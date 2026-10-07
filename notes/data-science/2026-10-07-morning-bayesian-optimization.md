# Bayesian Optimization

**Category:** Data Science  
**Date:** 2026-10-07 (morning)

---

# Bayesian Optimization for Hyperparameter Tuning  

Bayesian Optimization (BO) is a sequential model‑based strategy that treats hyperparameter tuning as a black‑box optimization problem. Instead of exhaustively trying combinations (grid search) or randomly sampling (random search), BO builds a probabilistic surrogate model—usually a Gaussian Process (GP)—that predicts the performance of unseen hyperparameter settings. An acquisition function (e.g., Expected Improvement, Upper Confidence Bound) then balances exploration of uncertain regions with exploitation of promising ones, selecting the next configuration to evaluate.

**Why use it?**  
- **Sample efficiency:** BO often finds near‑optimal settings with far fewer model trainings than grid or random search, which is crucial when each training run is costly.  
- **Automatic handling of continuous, discrete, and conditional spaces:** The surrogate can model mixed‑type variables and respect constraints.  
- **Applicability:** Widely adopted in deep learning (learning rate, dropout), gradient‑boosted trees (max depth, regularization), and even pipeline hyper‑parameters (feature selection thresholds).

**Typical workflow (using `scikit‑optimize`):**

```python
from skopt import BayesSearchCV
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split

X, y = load_boston(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define search space
param_space = {
    "n_estimators": (50, 300),          # integer range
    "max_depth": (3, 15),               # integer range
    "min_samples_split": (2, 20),       # integer range
    "max_features": ["auto", "sqrt", "log2"]  # categorical
}

opt = BayesSearchCV(
    estimator=RandomForestRegressor(random_state=42),
    search_spaces=param_space,
    n_iter=30,               # number of BO iterations
    cv=3,
    scoring="neg_mean_squared_error",
    random_state=42
)

opt.fit(X_train, y_train)
print("Best params:", opt.best_params_)
print("Best CV score:", -opt.best_score_)
```

In practice, after identifying the optimal hyperparameters, you retrain the model on the full training data and evaluate on a held‑out test set. Bayesian Optimization thus accelerates model development while preserving performance quality.
