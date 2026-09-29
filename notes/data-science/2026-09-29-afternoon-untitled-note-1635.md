# Untitled Note - 1635

**Category:** Data Science  
**Date:** 2026-09-29 (afternoon)

---

# Bayesian Optimization for Hyperparameter Tuning

Bayesian Optimization (BO) treats hyperparameter search as a black‑box optimization problem. Instead of exhaustively trying combinations (grid search) or randomly sampling (random search), BO builds a probabilistic surrogate model—typically a Gaussian Process (GP)—that predicts the performance of unseen hyperparameter settings. An acquisition function (e.g., Expected Improvement) uses this surrogate to decide where to sample next, balancing exploration of uncertain regions and exploitation of promising ones.  

**Why use it?**  
- **Sample efficiency:** BO often finds near‑optimal hyperparameters with far fewer evaluations than grid/random search, which is crucial when training models is expensive.  
- **Automatic trade‑off:** The acquisition function automatically balances trying new areas versus refining known good regions.  
- **Flexibility:** Works with continuous, discrete, and conditional hyperparameters, and can incorporate prior knowledge via the GP kernel.

**Typical workflow**  
1. Define the search space (e.g., learning rate ∈ [1e‑5, 1e‑1], max depth ∈ {3,5,7}).  
2. Choose a surrogate (GP) and acquisition (EI, UCB).  
3. Iteratively propose a new configuration, evaluate it (train/validate the model), and update the surrogate.  

```python
from skopt import BayesSearchCV
from sklearn.ensemble import RandomForestRegressor

search_spaces = {
    "n_estimators": (50, 300),          # int range
    "max_depth": (3, 15
