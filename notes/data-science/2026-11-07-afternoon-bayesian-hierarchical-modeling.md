# Bayesian Hierarchical Modeling

**Category:** Data Science  
**Date:** 2026-11-07 (afternoon)

---

# Bayesian Hierarchical Modeling

Bayesian hierarchical (or multilevel) models capture data that naturally group into clusters—such as students within schools or patients within hospitals—by sharing statistical strength across groups. Instead of fitting separate models for each group, a hierarchical model introduces group‑level parameters that are themselves drawn from a common prior. This structure lets low‑sample groups “borrow information” from richer groups, reducing over‑fitting while preserving genuine heterogeneity.

**When to use:**  
- **Partial pooling:** When you suspect group effects but have varying amounts of data per group.  
- **Complex surveys:** Accounting for design effects like stratification and clustering.  
- **Meta‑analysis:** Combining results from multiple studies with differing sample sizes.  
- **Missing data imputation:** Leveraging group‑level patterns to fill gaps.

**Simple example with PyMC**

```python
import pymc as pm
import arviz as az
import numpy as np

# Simulated data: test scores for students in 5 schools
schools = np.repeat(np.arange(5), 20)
y = np.random.normal(loc=70 + 5*schools, scale=10)

with pm.Model() as hierarchical:
    # Hyperpriors for group means and variance
    mu_mu = pm.Normal('mu_mu', mu=70, sigma=10)
    sigma_mu = pm.HalfNormal('sigma_mu', sigma=5)

    # School‑specific means
    mu = pm.Normal('mu', mu=mu_mu, sigma=sigma_mu, shape=5)

    # Observation model
    sigma = pm.HalfNormal('sigma', sigma=10)
    obs = pm.Normal('obs', mu=mu[schools], sigma=sigma, observed=y)

    trace = pm.sample(1000, tune=1000, target_accept=0.95, cores=2)

az.plot_forest(trace, var_names=['mu'])
```

The model learns a common distribution for school means (`mu_mu`, `sigma_mu`) while allowing each school its own deviation (`mu`). Posterior draws reveal both overall performance and school‑specific effects, automatically regularized by the hierarchy.

---
