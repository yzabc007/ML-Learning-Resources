# 4. Cart Pole with Policy Gradient

> [https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-2-ded33892c724](https://medium.com/@awjuliani/super-simple-reinforcement-learning-tutorial-part-2-ded33892c724)

---

##### Background

Reviewing three characteristics of traditional RL:

> 1. Different actions yield different rewards.
> 2. Rewards are delayed over time
> 3. Reward for an action is conditional on the state of the environment.
>
> MDP
>
> * At any time in an MDP, an agent is given a state`s`, takes action`a`, and receives new state`s’`and reward`r`.

The [Cart Pole](https://gym.openai.com/envs/CartPole-v0/) game aims to hold the balance of a Pole as long as possible.

Environment:

> A reward of +1 is provided for every timestep that the pole remains upright.
>
> The episode ends when the pole is more than 15 degrees from vertical, or the cart moves more than 2.4 units from the center.

> CartPole-v0 defines "solving" as getting average reward of 195.0 over 100 consecutive trials.



---

![](https://morvanzhou.github.io/static/results/reinforcement-learning/5-1-1.png)

