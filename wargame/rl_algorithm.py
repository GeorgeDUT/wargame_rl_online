"""
this file is reinforcement learning algorithm model
"""
import random
import numpy as np
import pandas as pd


class RL(object):
    def __init__(self,action_space, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
        self.actions = action_space
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = []
        self.q_table = pd.DataFrame(columns=self.actions,dtype=np.float64)

    def check_state_exist(self,state):
        if state not in self.q_table.index:
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # choose action use e_greedy method
        if np.random.rand() < self.epsilon:
            state_action = self.q_table.loc[observation,:]
            state_action = state_action.reindex(np.random.permutation(state_action.index))
            action = state_action.idxmax()
        else:
            action = np.random.choice(self.actions)
        # TODO: softmax method

        return action

    def learn(self, *arg):
        pass


class Q_learning_table(RL):
        def __init__(self,actions, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
            super(Q_learning_table,self).__init__(actions, learning_rate, reward_decay, e_greedy)

        def learn(self, s,a,r,s_):
            self.check_state_exist(s_)
            q_predict = self.q_table.loc[s,a]
            if s_ != 'terminal':
                q_target = r+self.gamma*self.q_table.loc[s_,:].max()
            else:
                q_target = r
            self.q_table.loc[s,a]+=self.lr*(q_target-q_predict)


class Sarsa_table(RL):
    pass


def brain_of_rboto(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    return action


def brain_of_nato(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    #action = 's'
    return action
