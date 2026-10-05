# Recursive Feature Elimination

**Category:** Data Science  
**Date:** 2026-10-05 (morning)

---

# Recursive Feature Elimination (RFE)

Recursive Feature Elimination (RFE) is a wrapper‑style feature‑selection technique that repeatedly fits a model and removes the least important features until a desired number of features remains. At each iteration, the model’s feature‑importance scores (e.g., coefficients for linear models or impurity reduction for tree‑based models) are computed, and the lowest‑ranking features are pruned. The process is “recursive” because the model is refit on the reduced set after each pruning step.

**Why use RFE?**  
- **Model‑agnostic:** Works with any estimator that provides a `coef_` or `feature_importances_` attribute.  
- **Performance‑driven:** By directly tying feature removal to model performance, RFE often yields a compact subset that preserves (or even improves) predictive power.  
- **Interpretability:** A smaller, well‑ranked feature set makes downstream analysis and explanations easier.

**Typical use cases**  
- High‑dimensional datasets (e.g., genomics, text) where many variables are noisy.  
- Situations where domain experts need a short, ranked list of predictors.  
- Pre‑processing step before deploying models on resource‑constrained devices.

**Example (scikit‑learn)**

```python
from sklearn.datasets import load_breast_cancer
from sklearn.svm import SVC
from sklearn.feature_selection import RFE
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify=y, random_state=42)

svc = SVC(kernel='linear', C=1)
rfe = RFE(estimator=svc, n_features_to_select=10, step=1)
rfe.fit(X_train, y_train)

print("Selected features:", rfe.support_.sum())
print("Feature ranking:", rfe.ranking_)
y_pred = rfe.predict(X_test)
print("Test accuracy:", accuracy_score(y_test, y_pred))
```

The code trains a linear SVM, recursively eliminates features, and retains the ten most informative ones, reporting the resulting test accuracy.

---
