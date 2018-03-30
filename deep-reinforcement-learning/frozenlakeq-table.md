# 1. Q Learning with table

> [https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)

---

#### Introduction of the environment

The environment is a simple game from [OpenAI](https://gym.openai.com/docs/) named [Frozen Lake](https://gym.openai.com/envs/FrozenLake-v0/).

It's a 4\*4 grid as follows:

SFFF       \(S: starting point, safe\)

FHFH       \(F: frozen surface, safe\)

FFFH       \(H: hole, fall to your doom\)

HFFG       \(G: goal, where the frisbee is located\)

The purpose of the task is walking from the starting point to the goal point and trying not to fall into the hole.

The tricky part is that on the frozen surface, there could be some wind to push you in the direction that you don't want to go. That's how the uncertain factor in the environment, otherwise, a simple search algorithm would successfully finish the task all the time.

---

#### Basic elements of RL

State: one of the 16 position on the grid

Action: four actions, up, down, left, right \(not consider the boundary, the agent will automatically learn it\)

Reward: whether you can successfully reach the goal point or not; that's a delayed reward. In the process of walking, there is no intermediate reward for each step.

---

#### Algorithm

The meaning of the bellman function is explained well as follows:

> [https://ai.intel.com/demystifying-deep-reinforcement-learning/](https://ai.intel.com/demystifying-deep-reinforcement-learning/)

The reward of future is discounted by a exponential factor in the following equation and is transformed into the second equation, which is **the summation of current reward and a discounted reward of next state**.

![](/assets/bellman_1.png)

![](/assets/bellman_2.png)

γ is the discount factor between 0 and 1 – the more into the future the reward is, the less we take it into consideration.

A good strategy for an agent would be to **always choose an action that maximizes the \(discounted\) future reward **as follows:

![](/assets/bellman_3.png)

Multiple understanding Q table:

1. The value stored in Q table could be considered as the future reward for choosing current action on current state. 
2. the best possible score at the end of the game after performing current action on current state.

**It is called Q-function, because it represents the “quality” of a certain action in a given state.**

![](/assets/bellman_4.png)

![](/assets/algo_q_table.png)![](/assets/algo_q_table_2.png)



