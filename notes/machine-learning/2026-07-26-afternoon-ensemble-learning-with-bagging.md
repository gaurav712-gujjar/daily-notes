# Ensemble Learning with Bagging

**Category:** Machine Learning  
**Date:** 2026-07-26 (afternoon)

---

# Ensemble Learning with Bagging
Ensemble learning with bagging is a technique used in machine learning where multiple instances of a model are trained on different subsets of the training data. This approach helps to reduce overfitting and improves the overall performance of the model. Each model in the ensemble is trained on a bootstrap sample of the training data, which is a random subset of the data with replacement. The predictions from each model are then combined to produce the final prediction.

Bagging is particularly useful when working with noisy or complex data, as it helps to reduce the variance of the model and improves its robustness. It's commonly used in practice for classification and regression tasks, especially when working with decision trees or other models that are prone to overfitting.

Here's an example of how bagging can be implemented using scikit-learn in Python:
```python
from sklearn.ensemble import BaggingClassifier
from sklearn.tree import DecisionTreeClassifier

bagging_model = BaggingClassifier(base_estimator=DecisionTreeClassifier(), n_estimators=10)
```
In this example, we're creating a bagging model with 10 decision trees as the base estimators. The `n_estimators` parameter controls the number of models in the ensemble.
