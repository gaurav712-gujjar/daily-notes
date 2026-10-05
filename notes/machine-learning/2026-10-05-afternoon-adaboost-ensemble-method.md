# AdaBoost Ensemble Method

**Category:** Machine Learning  
**Date:** 2026-10-05 (afternoon)

---

# AdaBoost Ensemble Method

AdaBoost (Adaptive Boosting) is a boosting algorithm that combines many weak learners—typically shallow decision trees—into a strong classifier. It works by iteratively training a new weak learner on the training data, but it re‑weights the instances: mis‑classified samples receive higher weights so the next learner focuses on the harder cases. After each round, the learner’s error determines its weight in the final vote, giving more influence to accurate models.

**Why it’s used**  
- **Improved accuracy**: By concentrating on difficult examples, AdaBoost often outperforms a single strong model.  
- **Robustness to over‑fitting**: When using simple weak learners (e.g., decision stumps), the ensemble remains interpretable and less prone to memorizing noise.  
- **Versatility**: Works for binary, multiclass, and even regression tasks (AdaBoost.R2). It is widely applied in text classification, face detection, and fraud detection where modest models need to be combined quickly.

**Quick example (scikit‑learn)**  

```python
from sklearn.ensemble import AdaBoostClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Weak learner: decision stump (max_depth=1)
stump = DecisionTreeClassifier(max_depth=1, random_state=42)

ada = AdaBoostClassifier(
    estimator=stump,
    n_estimators=100,
    learning_rate=0.5,
    random_state=42
)

ada.fit(X_train, y_train)
pred = ada.predict(X_test)
print("Test accuracy:", accuracy_score(y_test, pred))
```

The snippet builds an AdaBoost ensemble of 100 decision stumps, achieving high accuracy on a medical diagnosis dataset.

---
