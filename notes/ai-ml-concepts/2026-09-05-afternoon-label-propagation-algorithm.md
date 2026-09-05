# Label Propagation Algorithm

**Category:** AI/ML Concepts  
**Date:** 2026-09-05 (afternoon)

---

# Label Propagation Algorithm

Label Propagation is a simple, graph‑based semi‑supervised learning technique that spreads label information from a small set of labeled nodes to the unlabeled ones through the structure of a similarity graph. Each node starts with a probability distribution over classes; at every iteration, a node adopts the weighted average of its neighbors’ distributions. The process converges when distributions stop changing significantly.

**Why it’s useful**  
- **Scalability**: Only requires matrix multiplications; works well on large, sparse graphs.  
- **No explicit model training**: No gradient descent or hyper‑parameter tuning, making it fast to prototype.  
- **Natural fit for relational data**: Ideal for community detection, document classification with citation networks, or image segmentation where adjacency is known.

**Typical workflow**  
1. Construct a k‑nearest‑neighbors or similarity graph from feature vectors.  
2. Initialize label distributions for the few labeled nodes (one‑hot vectors).  
3. Iteratively update unlabeled nodes by averaging neighbor distributions, optionally applying a “clamping” factor to keep labeled nodes fixed.  
4. Assign each node the class with highest probability after convergence.

```python
import numpy as np
from sklearn.semi_supervised import LabelPropagation

# X: feature matrix, y: labels (-1 for unlabeled)
X = np.load('features.npy')
y = np.array([0, 1, -1, -1, 2, -1])   # example with 3 labeled points

lp = LabelPropagation(kernel='knn', n_neighbors=5, max_iter=1000)
lp.fit(X, y)

print("Predicted labels:", lp.transduction_)
```

The `LabelPropagation` class in scikit‑learn implements the algorithm with a choice of kernels (`knn`, `rbf`). After fitting, `transduction_` holds the final label assignment for every sample.

*When you have abundant unlabeled data but only a few annotated examples, label propagation offers an efficient way to leverage the underlying data manifold without heavy model training.*
