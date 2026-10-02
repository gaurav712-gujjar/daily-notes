# CatBoost Gradient Boosting

**Category:** Machine Learning  
**Date:** 2026-10-02 (afternoon)

---

# CatBoost Gradient Boosting

CatBoost (Categorical Boosting) is a gradient‑boosted decision‑tree library that natively handles categorical features without extensive preprocessing. It builds ensembles by sequentially adding trees that correct the residuals of previous ones, using ordered boosting to reduce target leakage and a symmetric tree structure for faster inference.  

**Why it’s useful**  
- **Categorical data:** Directly accepts string or integer categorical columns, applying optimal target encoding internally.  
- **Robustness:** Ordered boosting mitigates over‑fitting on small datasets, often outperforming XGBoost or LightGBM when categories are prevalent.  
- **Speed & deployment:** Supports GPU training, CPU parallelism, and model export to C++/ONNX for low‑latency serving.  

**Typical applications**  
- Click‑through‑rate prediction in online advertising.  
- Credit risk scoring where many features are categorical (e.g., occupation, zip code).  
- Recommender systems that combine user/item IDs with numeric signals.  

**Quick example (Python)**  

```python
from catboost import CatBoostClassifier, Pool
import pandas as pd

# Sample data
df = pd.DataFrame({
    'city': ['NY', 'LA', 'NY', 'SF', 'LA'],
    'device': ['mobile', 'desktop', 'mobile', 'tablet', 'desktop'],
    'age': [25, 32, 19, 45, 28],
    'clicked': [1, 0, 0, 1, 0]
})

X = df.drop('clicked', axis=1)
y = df['clicked']

cat_features = ['city', 'device']          # columns with categorical data
train_pool = Pool(X, y, cat_features=cat_features)

model = CatBoostClassifier(iterations=200,
                           depth=6,
                           learning_rate=0.1,
                           loss_function='Logloss',
                           verbose=False)
model.fit(train_pool)

# Predict probability of click
print(model.predict_proba(X)[:, 1])
```

The model automatically encodes *city* and *device*, trains an ensemble of decision trees, and outputs click‑through probabilities ready for downstream ranking or thresholding.
