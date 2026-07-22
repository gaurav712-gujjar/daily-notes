# Information Gain Calculation

**Category:** Data Science  
**Date:** 2026-07-22 (morning)

---

# Information Gain in Decision Trees
Information gain is a measure used in decision trees to determine the best split for a node. It calculates the reduction in impurity or uncertainty in the target variable after splitting the data based on a particular feature. This concept is crucial in building efficient decision trees, as it helps in selecting the most informative features that contribute to accurate predictions.

In practice, information gain is used in various machine learning algorithms, including decision trees, random forests, and gradient boosting machines. It is particularly useful when dealing with large datasets and multiple features, as it helps to identify the most relevant features that contribute to the target variable.

For example, in a decision tree, information gain can be calculated using the following formula:
```python
import math

def information_gain(parent_entropy, child_entropies):
    ig = parent_entropy
    for child_entropy in child_entropies:
        ig -= (child_entropy * (len(child_entropies) / len(parent_entropies)))
    return ig
```
This code snippet demonstrates a basic calculation of information gain, which can be used to determine the best split for a node in a decision tree.
