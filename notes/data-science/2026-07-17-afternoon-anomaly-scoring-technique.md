# Anomaly Scoring Technique

**Category:** Data Science  
**Date:** 2026-07-17 (afternoon)

---

# Anomaly Scoring
Anomaly scoring is a technique used in data science to identify unusual patterns or outliers in a dataset. It assigns a score to each data point based on its likelihood of being an anomaly. This score can be used to rank data points by their anomaly likelihood, allowing for further investigation or action.

Anomaly scoring is used in practice in various applications, such as fraud detection, network intrusion detection, and quality control. For instance, in credit card transactions, anomaly scoring can help identify potentially fraudulent transactions that deviate from a user's normal spending behavior.

Here's an example of how anomaly scoring can be implemented using the Local Outlier Factor (LOF) algorithm in Python:
```python
from sklearn.svm import OneClassSVM
import numpy as np

# Generate sample data
np.random.seed(0)
data = np.random.randn(100, 2)

# Create an OneClassSVM model
model = OneClassSVM(kernel='rbf', gamma=0.1, nu=0.1)

# Fit the model to the data
model.fit(data)

# Predict anomaly scores
anomaly_scores = model.decision_function(data)

# Print anomaly scores
print(anomaly_scores)
```
This code snippet demonstrates how to use the OneClassSVM algorithm to assign anomaly scores to data points.
