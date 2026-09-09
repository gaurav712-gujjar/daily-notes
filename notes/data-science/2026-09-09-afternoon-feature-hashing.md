# Feature Hashing

**Category:** Data Science  
**Date:** 2026-09-09 (afternoon)

---

# Feature Hashing (The Hashing Trick)

Feature hashing is a dimensionality‑reduction technique that maps high‑cardinality categorical or textual features into a fixed‑size vector space using a hash function. Instead of building a dictionary of every unique token (which can be memory‑intensive), each token’s hash determines both the index of the vector to increment and a sign (+1 or –1) to mitigate collisions. The resulting sparse vector can be fed directly to linear models or neural networks.

**Why use it?**  
- **Scalability:** Handles millions of distinct tokens with a constant memory budget.  
- **Speed:** No need for costly vocabulary construction or look‑ups.  
- **Online learning:** Works well when data arrives incrementally, as the hash space is predefined.  
- **Regularization effect:** Controlled collisions act like a form of feature mixing, sometimes improving generalization.

**Typical applications** include text classification, click‑through‑rate prediction, and any pipeline that must ingest large categorical fields (e.g., user IDs, product codes) without exploding the feature matrix.

```python
import numpy as np
from sklearn.feature_extraction import FeatureHasher

# Sample records with mixed categorical fields
records = [
    {'user_id': 'U123', 'product': 'A', 'action': 'click'},
    {'user_id': 'U456', 'product': 'B', 'action': 'view'},
    {'user_id': 'U123', 'product': 'C', 'action': 'purchase'},
]

hasher = FeatureHasher(n_features=2**10, input_type='dict')
X = hasher.transform(records)          # returns a scipy CSR matrix
print(X.toarray()[:2])                 # view first two hashed vectors
```

The hash size (`n_features`) trades off between collision probability and memory usage; a power‑of‑two size is common. Feature hashing is especially valuable in production pipelines where feature vocabularies evolve rapidly and memory constraints are tight.
