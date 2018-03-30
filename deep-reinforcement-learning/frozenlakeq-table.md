# 1. Q Learning with table

> https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0

---
#### Introduction of the environment

The environment is a simple game from [OpenAI](https://gym.openai.com/docs/) named [Frozen Lake](https://gym.openai.com/envs/FrozenLake-v0/). 

It's a 4*4 grid as follows:

SFFF       (S: starting point, safe)
FHFH       (F: frozen surface, safe)
FFFH       (H: hole, fall to your doom)
HFFG       (G: goal, where the frisbee is located)

The purpose of the task is walking from the starting point to the goal point and trying not to fall into the hole.

The tricky part is that on the frozen surface, there could be some wind to push you in the direction that you don't want to go. That's how the uncertain factor in the environment, otherwise, a simple search algorithm would successfully finish the task all the time.

---
#### Basic elements of RL

state: one of the 16 position on the grid
action: four actions, up, down, left, right (not consider the boundary)