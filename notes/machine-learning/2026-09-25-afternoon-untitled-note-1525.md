# Untitled Note - 1525

**Category:** Machine Learning  
**Date:** 2026-09-25 (afternoon)

---

# Stratified K-Fold Cross Validation

Stratified K-Fold is a variation of the standard K‑Fold cross‑validation that preserves the class distribution of the target variable in each fold. Instead of randomly splitting the data, it groups samples so that every fold has roughly the same proportion of each class as the whole dataset. This is crucial when dealing with imbalanced classification problems where a naïve split could produce folds that are dominated by the majority class, leading to misleading performance estimates.

**When to use it**

- **Imbalanced datasets** (e.g., fraud detection, medical diagnosis) where minority classes must be represented in every validation set.  
- **Model selection & hyper‑parameter tuning** for classification tasks to obtain reliable, unbiased estimates of generalisation performance.  
- **Comparing multiple models** where fairness across folds matters.

**Quick example (scikit‑learn)**

```python
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import numpy as np

X = np.load('features.npy')          # shape (n_samples, n_features)
y = np.load('labels.npy')            # binary or multiclass target

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = []

for train_idx, val_idx in skf.split(X, y):
    X_train, X_val = X[train_idx], X[val_idx]
    y_train, y_val = y[train_idx], y[val_idx]

    clf = RandomForestClassifier(n_estimators=200, random_state=0)
    clf.fit(X_train, y_train)
    preds = clf.predict(X_val)
    scores.append(f1_score(y_val, preds, average='weighted'))

print(f"Mean weighted F1 across folds: {np.mean(scores):.4f
