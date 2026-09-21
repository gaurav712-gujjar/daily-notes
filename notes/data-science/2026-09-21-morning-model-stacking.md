# Model Stacking

**Category:** Data Science  
**Date:** 2026-09-21 (morning)

---

# Model Stacking Ensemble

Model stacking (or stacked generalization) is an ensemble technique that combines multiple “base” learners by training a higher‑level **meta‑model** on their predictions. Unlike bagging or boosting, which aggregate predictions directly, stacking treats the outputs of the base models as features for the meta‑learner. This allows the meta‑model to learn how to weight or correct the individual predictions, often yielding better generalization.

**Why use stacking?**  
- **Heterogeneous strengths:** Different algorithms capture distinct patterns (e.g., tree‑based models excel on categorical interactions, linear models capture additive effects).  
- **Reduced over‑fitting:** The meta‑model sees out‑of‑fold predictions, mitigating leakage.  
- **Performance boost:** In Kaggle competitions, stacking frequently pushes scores past the ceiling of any single model.

**Typical workflow**  
1. Split the training data into *K* folds.  
2. For each base model, train on *K‑1* folds and generate predictions for the held‑out fold (out‑of‑fold predictions).  
3. Concatenate these predictions to form a new feature matrix.  
4. Train the meta‑model on this matrix.  
5. At inference, train each base model on the full data, predict on the test set, and feed those predictions to the meta‑model.

```python
from sklearn.model_selection import KFold
from sklearn.linear_model import Ridge
from sklearn.ensemble import RandomForestRegressor, GradientBoostingRegressor
import numpy as np

X, y = load_data()
base_models = [RandomForestRegressor(n_estimators=200, random_state=0),
               GradientBoostingRegressor(n_estimators=300, random_state=0)]

kf = KFold(n_splits=5, shuffle=True, random_state=42)
S_train = np.zeros((X.shape[0], len(base_models)))

for i, model in enumerate(base_models):
    for train_idx, val_idx in kf.split(X):
        model.fit(X[train_idx], y[train_idx])
        S_train[val_idx, i] = model.predict(X[val_idx])

meta = Ridge(alpha=1.0)
meta.fit(S_train, y)

# test predictions
S_test = np.column_stack([m.predict(X_test) for m in base_models])
final_pred = meta.predict(S_test)
```

Stacking is especially valuable when you have diverse models and enough data to avoid over‑fitting the meta‑learner.
