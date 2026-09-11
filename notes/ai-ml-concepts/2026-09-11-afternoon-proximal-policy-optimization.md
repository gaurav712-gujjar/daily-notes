# Proximal Policy Optimization

**Category:** AI/ML Concepts  
**Date:** 2026-09-11 (afternoon)

---

# Proximal Policy Optimization (PPO)

Proximal Policy Optimization is a policy‑gradient reinforcement‑learning algorithm that strikes a balance between sample efficiency and implementation simplicity. PPO optimizes a surrogate objective that clips the probability ratio between the new and old policies, preventing large, destabilizing policy updates. This “proximal” constraint keeps each update within a trust region without the heavy computation of methods like TRPO.

**Why it’s used:**  
- **Stability:** The clipping mechanism reduces the chance of catastrophic performance drops.  
- **Scalability:** PPO works well with parallel environments and can be applied to both discrete and continuous action spaces.  
- **Popularity:** It underpins many OpenAI Gym benchmarks and is the default in libraries such as Stable‑Baselines3.

**Typical workflow:**  
1. Collect trajectories using the current policy.  
2. Compute advantage estimates (e.g., GAE).  
3. Perform several epochs of minibatch SGD on the clipped surrogate loss.  
4. Update the policy and repeat.

```python
import gym
from stable_baselines3 import PPO

env = gym.make("CartPole-v1")
model = PPO("MlpPolicy", env, verbose=0)
model.learn(total_timesteps=100_000)

obs, _ = env.reset()
for _ in range(200):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, done, _, _ = env.step(action)
    env.render()
    if done:
        obs, _ = env.reset()
env.close()
```

PPO’s blend of reliability and ease‑of‑use makes it a go‑to choice for many RL projects, from game AI to robotic control.
