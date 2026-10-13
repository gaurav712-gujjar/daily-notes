# Isotonic Regression

**Category:** Data Science  
**Date:** 2026-10-13 (morning)

---

# Isotonic Regression for Probability Calibration

Isotonic regression is a non‑parametric, monotonic regression technique that fits a piecewise‑constant (or linear) function constrained to be **non‑decreasing** (or non‑increasing). In machine learning it is most often employed to **calibrate** the raw scores of a classifier so that they better reflect true probabilities. Unlike parametric methods such as Platt scaling (logistic regression), isotonic regression makes no assumption about the shape of the mapping, allowing it to adapt to irregular score‑to‑probability relationships.

**When to use it**

- After training a binary classifier (e.g., Random Forest, Gradient Boosting) whose predicted scores are poorly calibrated.
- When you have enough validation data (typically > 1000 instances) to avoid over‑fitting the monotonic fit.
- In risk‑sensitive domains like medical diagnosis or credit scoring where accurate probability estimates are crucial.

**How it works**

The algorithm sorts the validation instances by their raw scores, then pools adjacent groups whose average observed label violates monotonicity, merging them until the entire sequence is monotonic. The resulting step‑function maps each raw score to a calibrated probability.

**Python example (scikit‑learn)**

```python
from sklearn.isotonic import IsotonicRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import brier_score_loss

# Train a classifier
X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.3, random_state=42)
clf = GradientBoostingClassifier().fit(X_train, y_train)

# Raw scores (probability estimates)
raw_prob = clf.predict_proba(X_val)[:, 1]

# Fit isotonic regression on validation set
iso = IsotonicRegression(out_of_bounds='clip')
iso.fit(raw_prob, y_val)

# Calibrated probabilities
calibrated_prob = iso.predict(raw_prob)

print("Brier score before:", brier_score_loss(y_val, raw_prob))
print("Brier score after :", brier_score_loss(y_val, calibrated_prob))
```

The drop in Brier score demonstrates improved calibration.

---
