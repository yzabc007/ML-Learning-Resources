# 2. Frozen Lake with Q network

> [https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0](https://medium.com/emergent-future/simple-reinforcement-learning-with-tensorflow-part-0-q-learning-with-tables-and-neural-networks-d195264329d0)
>
> [https://github.com/yzabc007/ml\_learning\_resources/blob/master/deep-reinforcement-learning/FrozenLake\_Q\_table.py](https://github.com/yzabc007/ml_learning_resources/blob/master/deep-reinforcement-learning/FrozenLake_Q_table.py)

---

##### Design of neural network

Instead of storing Q values in a table, in this note, we would like to use a simple neural network to approximate a function with the input of one of states and the output of Q values for each action.

In the Frozen Lake game, the input is one of 16 states, the outputs are 4 Q values for each action. The neural network would be a simple FC network.

Specifically, the input would be a one hot vector for 16 states, the output would be a 4-dimension vector representing predicted Q value for each action, the ground-truth is the real Q value for current action calculated by the bellman function. The loss function is the square loss between predicted Q value vector and the golden Q value vector with an 

There are some tricks for building the network:

1. The predicted Q values are positive, so the initialization of weights should be positive
2. The 

---

##### Results:

It turns out a simple single FC layer performs worse than Q table algorithm.

![](/assets/frozenlake_q_tf_1.png)

The Q network needs more iterations to learn and the final performance is not as good as Q table.

