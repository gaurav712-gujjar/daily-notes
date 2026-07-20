# Markov Chain Monte Carlo

**Category:** AI/ML Concepts  
**Date:** 2026-07-20 (afternoon)

---

# Markov Chain Monte Carlo
Markov Chain Monte Carlo (MCMC) is a computational method used for approximating the distribution of a target variable. It works by generating a sequence of samples from a proposal distribution and accepting or rejecting them based on a probability calculated from the target distribution. This process creates a Markov chain that converges to the target distribution.

MCMC is widely used in practice for Bayesian inference, where it's used to estimate the posterior distribution of model parameters given observed data. It's particularly useful when the posterior distribution is complex or high-dimensional, making it difficult to compute analytically.

For example, in Python, the `scipy` library provides an implementation of MCMC for sampling from a target distribution:
```python
from scipy.stats import norm
import numpy as np

# Target distribution
def target_distribution(x):
    return norm.pdf(x, loc=0, scale=1)

# Proposal distribution
def proposal_distribution(x, sigma):
    return norm.rvs(loc=x, scale=sigma)
```
MCMC is used in various fields, including machine learning, statistics, and physics, for tasks such as parameter estimation, model selection, and uncertainty quantification.
