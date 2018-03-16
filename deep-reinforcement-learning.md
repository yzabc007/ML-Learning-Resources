# Deep Reinforcement Learning

---

Main referred learning resources:

> [https://medium.com/emergent-future](https://medium.com/emergent-future)
>
> [https://ai.intel.com/demystifying-deep-reinforcement-learning/](https://ai.intel.com/demystifying-deep-reinforcement-learning/)

---

The differences between Q-learning and policy gradient:

| Policy gradient |  |
| :--- | :--- |
| Q -learning |  |

Characteristics of RL problem:

1. Different actions yield different rewards.
2. Rewards are delayed over time.
3. Reward for an action is conditional on the state of the environment. 

![](/assets/comparisons_bandit_full_RL.png)

FULL RL:

Environments which pose the full problem to an agent are referred to as Markov Decision Processes \(MDPs\).

An MDP consists of a set of all possible states S from which our agent at any time will experience s. A set of all possible actions A from which our agent at any time will take action a. Given a state action pair \(s, a\), the transition probability to a new state s’ is defined by T\(s, a\), and the reward r is given by R\(s, a\). As such, at any time in an MDP, an agent is given a state s, takes action a, and receives new state s’ and reward r.

**credit assignment problem**– i.e., which of the preceding actions was responsible for getting the reward and to what extent.

— 不确定之前到底是哪一个动作导致了现在的reward

核心思想是：找出在那些state下采取哪些action能够导致更大的reward

**explore-exploit dilemma** – should you exploit the known working strategy or explore other, possibly better strategies.

1. 是否应该在当前已知的策略中选择最好的；还是要继续探索未知的策略
2. Exploration
   ：探索未知（**ε-greedy exploration**）
3. Exploitation

Discounted Future Reward

![](/assets/bellman_1.png)

![](/assets/bellman_2.png)

γ is the discount factor between 0 and 1 – the more into the future the reward is, the less we take it into consideration.

function Q\(s, a\) representing **themaximum discounted future rewardwhen we perform action **a** in state **s**, and continue optimally from that point on.**

![](/assets/bellman_3.png)

![](/assets/bellman_4.png)

the best possible score at the end of the gameafter performing action a** in state **s

**It is called Q-function, because it represents the “quality” of a certain action in a given state.**

maximum future reward for \(this state and action\) is the immediate reward plus **maximum future reward for the next state**.

------



