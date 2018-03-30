# Deep Reinforcement Learning

---

Main referred learning resources:

###### Blogs

> [https://medium.com/emergent-future](https://medium.com/emergent-future)
>
> [https://ai.intel.com/demystifying-deep-reinforcement-learning/](https://ai.intel.com/demystifying-deep-reinforcement-learning/)

##### Slides

> [http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html](http://www0.cs.ucl.ac.uk/staff/d.silver/web/Teaching.html)

##### Online Videos

> [http://videolectures.net/rldm2015\_silver\_reinforcement\_learning/](http://videolectures.net/rldm2015_silver_reinforcement_learning/)
>
> [http://videolectures.net/deeplearning2017\_pineau\_reinforcement\_learning/](http://videolectures.net/deeplearning2017_pineau_reinforcement_learning/)

---

The differences between Q-learning and policy gradient:

| Policy gradient | Attempts to learn functions which directly map on observation to an action |
| :--- | :--- |
| Q -learning | Attempts to learn the value of being in a given state, and taking a specific action there |

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

function Q\(s, a\) representing **the maximum discounted future rewardwhen we perform action **a** in state **s**, and continue optimally from that point on.**

![](/assets/bellman_3.png)

![](/assets/bellman_4.png)

the best possible score at the end of the gameafter performing action a** in state **s

**It is called Q-function, because it represents the “quality” of a certain action in a given state.**

maximum future reward for \(this state and action\) is the immediate reward plus **maximum future reward for the next state**.

---

DQN

![](/assets/dqn_loss.png)

Algorithm:

Given a transition &lt; s, a, r, s’ &gt;, the Q-table update rule in the previous algorithm must be replaced with the following:

1. Do a feedforward pass for the current state s to get predicted Q-values for all actions.
2. Do a feedforward pass for the next state s’ and calculate maximum overall network outputs max a’ Q\(s’, a’\).
3. Set Q-value target for action to r + γmax a’ Q\(s’, a’\) \(use the max calculated in step 2\). For all other actions, set the Q-value target to the same as originally returned from step 1, making the error 0 for those outputs.
4. Update the weights using backpropagation.

**Experience Replay:**

1. This breaks the similarity of subsequent training samples, which otherwise might drive the network into a local minimum.
2. Also experience replay makes the training task more similar to usual supervised learning, which simplifies debugging and testing the algorithm.
3. One could actually collect all those experiences from human gameplay and then train network on these.



