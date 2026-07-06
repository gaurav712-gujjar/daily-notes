# K Nearest Neighbors

**Category:** AI/ML Concepts  
**Date:** 2026-07-06 (afternoon)

---

# K-Nearest Neighbors Algorithm
The K-Nearest Neighbors (KNN) algorithm is a supervised learning technique used for classification and regression tasks. It works by finding the 'k' most similar data points, known as neighbors, to a new input data point, and using their labels or values to make predictions. This algorithm is simple to implement and can be effective for datasets with a small number of features.

KNN is used in practice for a variety of applications, including customer segmentation, image classification, and recommender systems. It's particularly useful when the relationship between the features and target variable is complex and non-linear. For instance, in a movie recommender system, KNN can be used to suggest movies to a user based on the movies they've already watched and liked.

Here's an example code snippet in Python using scikit-learn library:
```python
from sklearn.neighbors import KNeighborsClassifier
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split

iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, test_size=0.2)
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
```
