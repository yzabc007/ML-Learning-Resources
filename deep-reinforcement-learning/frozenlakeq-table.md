# 1. Q Learning with table

> [https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)

---

#### Introduction of the environment

The environment is a simple game from [OpenAI](https://gym.openai.com/docs/) named [Frozen Lake](https://gym.openai.com/envs/FrozenLake-v0/).

It's a 4\*4 grid as follows:

> SFFF       \(S: starting point, safe\)
>
> FHFH       \(F: frozen surface, safe\)
>
> FFFH       \(H: hole, fall to your doom\)
>
> HFFG       \(G: goal, where the frisbee is located\)

The purpose of the task is walking from the starting point to the goal point and trying not to fall into the hole.

The tricky part is that on the frozen surface, there could be some wind to push you in the direction that you don't want to go. That's how the uncertain factor in the environment, otherwise, a simple search algorithm would successfully finish the task all the time.

---

#### Basic elements of RL

State: one of the 16 position on the grid

Action: four actions, up, down, left, right \(not consider the boundary, the agent will automatically learn it\)

Reward: whether you can successfully reach the goal point or not; that's a delayed reward. In the process of walking, there is no intermediate reward for each step.

---

#### Understanding of discounted future reward and the Q learning with table

The meaning of the bellman function is explained well in the following blog:

> [https://ai.intel.com/demystifying-deep-reinforcement-learning/](https://ai.intel.com/demystifying-deep-reinforcement-learning/)

The reward of future is discounted by an exponential factor in the following equation and is transformed into the second equation, which is **the summation of current reward and a discounted reward of next state**.

> ![](/assets/bellman_1.png)
>
> ![](/assets/bellman_2.png)
>
> γ is the discount factor between 0 and 1 – the more into the future the reward is, the less we take it into consideration.
>
> A good strategy for an agent would be to **always choose an action that maximizes the \(discounted\) future reward.**
>
> ![](/assets/bellman_3.png)

R\_{t+1} is discounted future reward for all possible actions.

Multiple understandings of values stored in Q table:

1. The value stored in Q table could be considered as the **maximum discounted future reward** for choosing current action in current state.
2. > the best possible score at the end of the game after performing current action on current state.

> **It is called Q-function, because it represents the “quality” of a certain action in a given state.**
>
> Then the bellman function comes up to estimate the Q function, aka., the maximum future reward for current state is the sum of current reward \(immediate reward\) and the maximum future reward for the next state.
>
> ![](/assets/bellman_4.png)

---

#### Algorithm for Q table learning

##### My algorithm

![](/assets/algo_q_table.png)

##### Tambet Matiisen's algorithm

> ![](/assets/algo_q_table_2.png)

There are many tricky parts in the real algorithm and keep the following sentence from **la la land** in mind:

> a bit of madness is key, to give us new colors to see ...

If we strictly follow the above algorithm process, we would confine ourselves in some kind of local optimal points. As a result, we need to add some randomness/uncertainty in the process.

For example:

1. By using a learning rate, we decide not to fully update the Q value by bellman function but to change the value based on its previous value
2. When greedily choosing the best action based on current Q table, it's not necessary to choose the best one all the time.

---

#### Evaluation

##### Irrelevant thoughts

After implementing the simple algorithm, the last question may be how do we evaluate the algorithm.

A bad news is that there may not be deterministic metrics, such as accuracy, loss, etc to tell you how good or bad of the algorithm.

The question we should ask is that how could we evaluate a learning algorithm when the algorithm is still learning.

A simple answer would be how fast the algorithm successfully learn something or does it learn something.

##### Simple Metrics for this task

In this simple Q table experiments,  we use two metrics to evaluation the algorithm and tune the parameters.

1. The number of steps each trial takes to end \(whether it fails to reach the goal or successfully make it\)
2. The percentage of successful trails among all trails

For the first metric, at the beginning, the agent may fall into the hole easily because of the underestimate of the environment, thus it would take very few steps to finish one trial; after the learning, the agent is supposed to take longer time to stay on the frozen surface and the percentage of success will increase.

\(Note the maximum number of steps is 100 and when your agent takes 100 steps, the end flag will be True set by the environment and it's actually not good because we expect the agent take as less as possible steps to reach the goal.\)

For the second metric, it's easily to understand that the higher the percentage, the better the agent is.

##### Visualizing the results

All in all, because of the simplicity of this task, we can plot the following figure to show the progress of learning.  
![](/assets/frozenlake_res_1.png)
<img src="/assets/frozenlake_res_1.png" width="100">
The blue points are the failing trails, the red points are the successful trails, and the green points are the unfinished trails within 100 steps. \(of course, we couldn't take the unfinished trails as failure, but we still want the agent to reach a failing or success point ASAP considering such a simple task.\)

As we can see, at the beginning, the agent fails very often, while after about 200 iterations, it learns how to reach the goal successfully and the success ratio is pretty high. But note the success ratio is very unstable but the tendency of the progress of learning should be similar.

##### Parameters tuning

There are two main parameters to tune: learning rate and the discount factor.

1. The larger the learning rate is, the more you consider new value calculated by the bellman function, the less you consider old value from current Q table.
2. The larger the discount factor, gamma, is, the more you consider the future reward, the less you consider the current/intermediate reward.
   > If we set the discount factor _γ_=0, then our strategy will be short-sighted and we rely only on the immediate rewards. If we want to balance between immediate and future rewards, we should set discount factor to something like _γ=0.9. If our environment is deterministic and the same actions always result in same rewards, then we can set discount factor _γ=1.

##### Some interesting results





