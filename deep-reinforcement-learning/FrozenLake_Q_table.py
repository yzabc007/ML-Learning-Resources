import gym
import numpy as np
import argparse
import itertools

import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt


def str2bool(string):
    return string.lower() in ['yes', 'true', 't', 1]


def main():
    parser = argparse.ArgumentParser(description="Collecting Data")
    parser.register('type', 'bool', str2bool)
    parser.add_argument('-g', '--GAMMA', type=float, default=0.95, help='gamma for bellman function')
    parser.add_argument('-l', '--LR', type=float, default=0.8, help='learning rate')
    parser.add_argument('-e', '--EPOCHS', type=int, default=3000, help='number of epochs')

    args = parser.parse_args()
    print 'args: ', args

    env = gym.make('FrozenLake-v0')
    num_states = env.observation_space.n
    num_actions = env.action_space.n

    # define a two-dimensional table: states-actions
    Q_table = np.zeros([num_states, num_actions])
    # learning rate
    lr = args.LR
    # discount parameter
    gamma = args.GAMMA
    num_epochs = args.EPOCHS
    reward_list = []
    end_list = []
    scatter_0 = []
    scatter_1 = []
    scatter_2 = []

    for i in range(num_epochs):
        # initial state
        cur_state = env.reset()
        total_reward = 0
        count = 0
        end = False
        # begin exploring the space
        # while count < 99:
        while not end:
            count += 1
            # greedily select a best action
            # cur_action = np.argmax(Q_table[cur_state, :])
            cur_action = np.argmax(Q_table[cur_state, :] + np.random.randn(1, num_actions) * (1./(i + 1)))
            # run the environment, move to next state, get reward to the transition, decide whether to stop
            new_state, new_reward, end, _ = env.step(cur_action)
            # calculate the new Q value for current state and action based on the bellman equation
            Q_table[cur_state, cur_action] = (1 - lr) * Q_table[cur_state, cur_action] + \
                lr * (new_reward + gamma * np.max(Q_table[new_state, :]))
            total_reward += new_reward
            cur_state = new_state
            # if end:
            #     break

        if new_reward:
            scatter_1.append([i, count])
        elif count == 100:
            scatter_2.append([i, count])
        else:
            scatter_0.append([i, count])

        reward_list.append(total_reward)
        end_list.append(count)

    ratio_success = sum(reward_list) / float(num_epochs)
    print 'Percent of succesful episodes', ratio_success
    print 'Success ration for last 100 epochs: ', sum(reward_list[-1000:]) / 1000.

    # plt.figure(figsize=(12, 5))
    # plt.plot(range(len(end_list)), end_list, 'b.')
    # plt.savefig('end_list_table')
    #
    # plt.figure(figsize=(12, 5))
    # plt.plot(range(len(reward_list)), reward_list, 'b.')
    # plt.savefig('reward_list_table')

    plt.figure(figsize=(12, 5))
    if scatter_0:
        scatter_0 = np.array(scatter_0)
        plt.scatter(scatter_0[:, 0], scatter_0[:, 1], c='b', marker='.')
    if scatter_1:
        scatter_1 = np.array(scatter_1)
        plt.scatter(scatter_1[:, 0], scatter_1[:, 1], c='r', marker='.')
    if scatter_2:
        scatter_2 = np.array(scatter_2)
        plt.scatter(scatter_2[:, 0], scatter_2[:, 1], c='g', marker='.')
    plt.xlabel('Iterations')
    plt.ylabel('Number of steps to finish')
    plt.title('Plotting ending points (success ratio:%0.4f, lr=%0.2f, gamma=%0.2f' % (ratio_success, lr, gamma))
    plt.savefig('new_reward_count_plot')

    # plot Q table
    # Q_table = Q_table.transpose()
    # plt.figure(figsize=(12, 5))
    # plt.imshow(Q_table, interpolation='nearest', cmap=plt.cm.Blues)
    # plt.title('Plotting of Q table')
    # plt.colorbar()
    # plt.yticks(np.arange(num_actions), ['LEFT', 'DOWN', 'RIGHT', 'UP'], rotation=45)
    # plt.xticks(np.arange(num_states), range(num_states))
    #
    # thresh = Q_table.max() / 2
    # for i, j in itertools.product(range(num_actions), range(num_states)):
    #     plt.text(j, i, format(Q_table[i, j], '4.2f'),
    #              horizontalalignment="center",
    #              color="white" if Q_table[i, j] > thresh else 'black')
    # plt.tight_layout()
    # plt.ylabel('Action')
    # plt.xlabel('State')
    # plt.savefig('Q_table')
    return


if __name__ == '__main__':
    main()
