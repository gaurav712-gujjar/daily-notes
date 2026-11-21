# Dynamic Time Warping

**Category:** Data Science  
**Date:** 2026-11-21 (morning)

---

# Dynamic Time Warping (DTW)

Dynamic Time Warping is an algorithm for measuring similarity between two temporal sequences that may vary in speed or length. Unlike simple Euclidean distance, DTW aligns points by “warping” the time axis, allowing for local accelerations and decelerations. The optimal alignment is found via dynamic programming, constructing a cost matrix where each cell contains the cumulative distance of the best path to that point.

**Why it matters:**  
- **Time‑series classification** – DTW is a go‑to distance metric for nearest‑neighbor classifiers when patterns are shifted or stretched.  
- **Sensor fusion** – Aligning signals from devices with different sampling rates.  
- **Speech & handwriting recognition** – Matching spoken words or pen strokes despite varying speeds.  

**Basic Python example (tslearn):**

```python
import numpy as np
from tslearn.metrics import dtw
from tslearn.datasets import CachedDatasets

# Load two simple series
X_train, y_train = CachedDatasets().load_dataset("Trace")
s1, s2 = X_train[0].ravel(), X_train[1].ravel()

# Compute DTW distance
dist = dtw(s1, s2)
print(f"DTW distance: {dist:.2f}")

# Visualize optimal warping path
from tslearn.metrics import dtw_path
path, _ = dtw_path(s1, s2)

import matplotlib.pyplot as plt
plt.plot(s1, label='Series 1')
plt.plot(s2, label='Series 2')
for (i, j) in path[::10]:  # plot a subset of alignment lines
    plt.plot([i, j], [s1[i], s2[j]], 'k-', alpha=0.3)
plt.legend()
plt.title('DTW Alignment')
plt.show()
```

DTW runs in O(N × M) time for series of lengths N and M, but fast approximations (e.g., Sakoe‑Chiba band) make it practical for large datasets.
