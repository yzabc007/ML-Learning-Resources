# 3. Two armed bandit with Policy Gradient

> [https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-1-fd544fab149)

---

##### Notes:

Characteristics of traditional RL:

> 1. Different actions yield different rewards.
> 2. Rewards are delayed over time
> 3. Reward for an action is conditional on the state of the environment.

Differences between Policy-based and Value-based:

> 1. Policy-based learns a policy for picking optimal actions in a given state directly, while Value-based learns to predict how good a given state or action will be for the agent to be in.

Well, it may sound like it's the same algorithm for both of them after real understanding the sentence, because the Policy-based still needs to choose the best action based on some values. So what's the real difference between two of them? There are some explanations as follows:

1. The action chosen by Policy-based could be continuous, while the action chosen by Value-based can only be discrete.

---

### Two armed bandit



