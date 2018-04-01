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

The basic principle is that when receiving a reward by tanking an action given a state, we want to increase the probability according to the reward for taking this action when encounter a similar context \(maybe not the same state?\).

---

### Multi-armed bandits

https://cdn-images-1.medium.com/max/742/1*Tt8A6mP98ibBlrlFD5UJxg.png

> Two slot machines, each with a different fixed payout probability.
>
> The goal is to discover the machine with the best payout, and maximize the returned reward by always choosing it.

In the game of four armed bandit, each bandit has a probability to get the reward, and the goal of the agent is to choose the most likely one to get reward.

This simple game only satisfies the 1 first characteristic for traditional RL and could **be confused with supervised learning**.

* The environment of the bandit problem is uncertain, that is, when pulling the bandit \(take an action\), the reward is not guaranteed. In supervised learning, the label/reward is obtained certainly for the input.

In our policy network, we define 4 weights for 4 bandits to direct the probability of pulling this bandit to get a reward. Then we choose the largest one as the action currently.

The input of the policy network is the actual selected action, the output is the positive/negative reward. The loss function is the policy loss equation:

> Loss = -log\(π\)\*A
>
> `A`is advantage, and is an essential aspect of all reinforcement learning algorithms.
>
> * Intuitively it corresponds to how much better an action was than some baseline.
>
> `π`is the policy. In this case, it corresponds to the chosen action’s weight.
>
> Intuitively, this loss function allows us to increase the weight for actions that yielded a positive reward, and decrease them for actions that yielded a negative reward. In this way the agent will be more or less likely to pick that action in the future.

---

#### Contextual Bandits



