# Goal‑Conditioned Policy Networks

**Category:** Agentic AI  
**Date:** 2026-10-30 (afternoon)

---

# Goal‑Conditioned Policy Networks (GCPN)

Goal‑Conditioned Policy Networks are neural policies that take **both the current state and a desired goal** as inputs and output an action distribution. Unlike standard policies that learn to maximize a fixed reward, GCPNs learn a **generalizable mapping** from any reachable goal to the actions needed to achieve it. During training, the agent samples random goals from the environment’s state space and receives a binary reward (1 if the goal is reached, 0 otherwise). This encourages the network to discover **trajectory‑level behaviors** that can be reused for new objectives at inference time.

**Practical use‑cases**  
- **Robotic manipulation:** a single policy can pick, place, or assemble objects simply by feeding the target pose as a goal vector.  
- **Navigation:** autonomous vehicles can be directed to arbitrary waypoints without retraining.  
- **Game AI:** NPCs can pursue dynamic objectives (e.g., “collect 3 health packs”) using the same model.

**Minimal PyTorch example**

```python
import torch
import torch.nn as nn
import torch.nn.functional as F

class GCPN(nn.Module):
    def __init__(self, state_dim, goal_dim, act_dim):
        super().__init__()
        self.fc = nn.Sequential(
            nn.Linear(state_dim + goal_dim, 256),
            nn.ReLU(),
            nn.Linear(256, act_dim)
        )

    def forward(self, state, goal):
        x = torch.cat([state, goal], dim=-1)
        logits = self.fc(x)
        return F.softmax(logits, dim=-1)

# dummy dimensions
state = torch.randn(1, 10)   # e.g., robot joint angles
goal  = torch.randn(1, 5)    # target end‑effector pose
policy = GCPN(state_dim=10, goal_dim=5, act_dim=4)

action_prob = policy(state, goal)
print(action_prob)
```

The network learns a **single, reusable policy** that can be queried with new goals, dramatically reducing the need for multiple task‑specific models.
