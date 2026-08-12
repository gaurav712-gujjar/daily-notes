# Reward Shaping Technique

**Category:** Agentic AI  
**Date:** 2026-08-12 (morning)

---

# Reward Shaping in Agentic AI
Reward shaping is a technique used in agentic AI to modify the reward function of an agent to guide its learning process. The goal is to provide additional rewards or penalties to encourage the agent to take specific actions or reach particular states. This can be particularly useful when the original reward function is sparse or difficult to optimize.

In practice, reward shaping is used in various applications, such as robotics, game playing, and autonomous driving. For example, in a robotic arm task, a reward shaping function can be designed to reward the arm for reaching a certain position or for avoiding obstacles.

Here's a simple example of reward shaping in Python:
```python
def reward_shaping(state, action):
    if state == 'goal' and action == 'reach':
        return 10  # reward for reaching the goal
    elif state == 'obstacle' and action == 'avoid':
        return 5  # reward for avoiding the obstacle
    else:
        return 0  # no reward otherwise
```
This function can be used to modify the original reward function and provide additional guidance to the agent.
