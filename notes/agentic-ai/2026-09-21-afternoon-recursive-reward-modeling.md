# Recursive Reward Modeling

**Category:** Agentic AI  
**Date:** 2026-09-21 (afternoon)

---

# Recursive Reward Modeling

Recursive Reward Modeling (RRM) is a training paradigm for agentic AI where a hierarchy of language models or policies iteratively learns to evaluate increasingly complex tasks. A base model first learns a simple reward function from human feedback. Higher‑level models then use the lower‑level reward model as a *proxy evaluator* to train on more abstract objectives, recursively building up capability without requiring exhaustive human labeling for every nuance.

**Why it’s used**  
- **Scalability**: Direct human annotation becomes infeasible for sophisticated tasks (e.g., long‑term planning, ethical judgments). RRM lets a small set of human‑rated examples bootstrap a cascade of learned evaluators.  
- **Alignment**: By grounding higher‑level rewards in lower‑level models that were explicitly aligned, the system inherits alignment properties, reducing the risk of reward hacking.  
- **Generalization**: Each recursion abstracts away details, enabling the agent to handle novel situations that were never explicitly labeled.

**Typical workflow**

```python
# Pseudocode for a two‑level RRM loop
reward_model_0 = train_reward_model(human_labeled_data)

for level in range(1, N):
    # Generate queries for the next level
    queries = policy[level-1].sample_trajectories()
    # Use previous reward model to score them
    scores = reward_model_{level-1}.predict(queries)
    # Train next reward model on (queries, scores) pairs
    reward_model_{level} = train_reward_model(queries, scores)
    # Update policy to maximize the new reward
    policy[level] = reinforce(policy[level-1], reward_model_{level})
```

RRM is especially promising for safe AI assistants, autonomous scientific discovery agents, and any system that must reason about abstract goals while remaining anchored to human values.
