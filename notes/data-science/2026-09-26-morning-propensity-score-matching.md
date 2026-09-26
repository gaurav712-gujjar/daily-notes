# Propensity Score Matching

**Category:** Data Science  
**Date:** 2026-09-26 (morning)

---

# Propensity Score Matching

Propensity Score Matching (PSM) is a statistical technique used to reduce selection bias in observational studies when estimating causal effects. It involves estimating the probability (the propensity score) that each unit receives a treatment given its observed covariates, typically via logistic regression. Units from the treatment and control groups are then paired (or weighted) based on similar scores, creating a pseudo‑randomized sample where the distribution of covariates is balanced.

**Why it matters:**  
- **Causal inference**: Enables more credible estimation of treatment effects without a randomized experiment.  
- **Policy evaluation & healthcare**: Frequently applied to assess the impact of interventions (e.g., a new drug, marketing campaign).  
- **Data‑driven decision making**: Provides a transparent, reproducible way to control for confounders when randomization isn’t feasible.

**Typical workflow**
1. Choose covariates that influence both treatment assignment and outcome.  
2. Fit a propensity model (often logistic regression).  
3. Match each treated unit to one or more control units with similar scores (nearest‑neighbor, caliper, or kernel matching).  
4. Check covariate balance (e.g., standardized mean differences).  
5. Estimate the average treatment effect on the matched sample.

**Python example (using `pymatch`):**

```python
import pandas as pd
from pymatch.Matcher import Matcher

# Load data with treatment column 'promo' and covariates
df = pd.read_csv('marketing.csv')

# Fit propensity model
m = Matcher(df, yvar='promo', exclude=['outcome'])
m.fit_scores(balance=True, nmodels=5)

# Perform 1‑to‑1 nearest neighbor matching with caliper 0.05
m.match(method='nearest', nmatches=1, caliper=0.05)

# Check balance
print(m.balance())
# Estimate treatment effect
ate = m.est_att()
print(f'Estimated ATT: {ate:.3f}')
```

This snippet demonstrates building propensity scores, matching, and evaluating balance before estimating the average treatment effect on the treated (ATT).
