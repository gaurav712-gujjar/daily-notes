# SMOTE for Imbalanced Data

**Category:** Data Science  
**Date:** 2026-09-09 (afternoon)

---

# SMOTE for Imbalanced Data

SMOTE (Synthetic Minority Over‑sampling Technique) generates new minority‑class examples by interpolating between existing ones. Instead of simply duplicating minority samples, SMOTE creates synthetic points along the line segments joining a minority instance and its *k* nearest minority neighbors. This reduces over‑fitting that can occur with naive oversampling while balancing class distributions.

**Why use SMOTE?**  
Imbalanced datasets—common in fraud detection, medical diagnosis, and churn prediction—bias classifiers toward the majority class, leading to poor recall on the minority. SMOTE improves model sensitivity and overall metrics (e.g., F1‑score, AUC) by providing the learner with a richer representation of the minority decision space.

**Practical considerations**  
- Apply SMOTE *only* to the training split to avoid data leakage.  
- Combine with under‑sampling of the majority class for extreme imbalance.  
- Beware of generating noisy samples near class boundaries; variants like Borderline‑SMOTE or ADASYN can mitigate this.

```python
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X, y = load_data()                         # your feature matrix and labels
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, stratify=y, random_state=42)

sm = SMOTE(k_neighbors=5, random_state=42)
X_res, y_res = sm.fit_resample(X_train, y_train)

clf = RandomForestClassifier(n_estimators=200, random_state=1)
clf.fit(X_res, y_res)
print(classification_report(y_test, clf.predict(X_test)))
```

The snippet demonstrates a typical workflow: split, oversample the training data with SMOTE, train a model, and evaluate on the untouched test set.
