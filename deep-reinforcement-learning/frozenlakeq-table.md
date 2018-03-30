# 1. Q Learning with table

> https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0

---

The environment is a simple game from [OpenAI](https://gym.openai.com/docs/) named [Frozen Lake](https://gym.openai.com/envs/FrozenLake-v0/). 

It's a 4*4 grid as follows:

SFFF       (S: starting point, safe)
FHFH       (F: frozen surface, safe)
FFFH       (H: hole, fall to your doom)
HFFG       (G: goal, where the frisbee is located)

The purpose of the task is 