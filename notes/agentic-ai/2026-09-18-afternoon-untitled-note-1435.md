# Untitled Note - 1435

**Category:** Agentic AI  
**Date:** 2026-09-18 (afternoon)

---

# Options Framework for Hierarchical Agentic Planning

The **options framework** extends primitive actions with *temporally extended* macro‑actions called *options*. An option consists of three parts: an initiation set (states where it can start), an intra‑option policy (how to act while the option is active), and a termination condition. In agentic AI, options let a single agent reason at multiple time‑scales, turning a complex task into a hierarchy of sub‑tasks that can be planned and learned separately.

**Why it matters**  
- **Scalability** – Long‑horizon problems (e.g., robot navigation, game playing) become tractable when high‑level goals are decomposed into reusable skills.  
- **Transferability** – Learned options can be reused across environments, accelerating adaptation.  
- **Interpretability** – High‑level options correspond to human‑readable behaviors (“pick‑up‑object”, “navigate‑to‑room”), making the agent’s plan easier to audit.

**Typical usage**  
1. **Skill discovery** – Use unsupervised methods (e.g., clustering of trajectories) to define candidate options.  
2. **Learning** – Train intra‑option policies with RL or imitation learning while learning a high‑level policy over options.  
3. **Planning** – Employ model‑based planners that treat options as actions, reducing the depth of the search tree.

**Python sketch (using `gym` and `stable-baselines3`)**

```python
import gym, numpy as np
from stable_baselines3 import PPO

# ---- Define a simple option ----
class MoveToGoalOption:
    def __init__(self, goal):
        self.goal = np.array(goal)

    def initiation(self, state):
        # can start anywhere
        return True

    def termination(self, state):
        # stop when within 0.1 of goal
        return np.linalg.norm(state[:2] - self.goal) < 0.1

    def
