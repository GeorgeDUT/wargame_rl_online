from map import Warmap
import random
import numpy as np
import pandas as pd
RED_ARMY = 10
GRAY_ARMY = 10

class RL(object):
    def __init__(self, action_space, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
        self.actions = action_space
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        print(self.q_table.index)

    def check_state_exist(self, state):
        if state not in self.q_table.index:
            # append new state to q table
            self.q_table = self.q_table.append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table.columns,
                    name=state,
                )
            )

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # action selection
        if np.random.rand() < self.epsilon:
            # choose best action
            state_action = self.q_table.loc[observation, :]
            state_action = state_action.reindex(
                np.random.permutation(state_action.index))  # some actions have same value
            action = state_action.idxmax()
        else:
            # choose random action
            action = np.random.choice(self.actions)
        return action

    def learn(self, *args):
        pass

class SarsaTable(RL):

    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(SarsaTable, self).__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_, a_):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, a_]  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)  # update


def update():
    '''
    for turn in range(5):
        env.reload()
        for agentid in range(RED_ARMY):
            num = random.randint(0,3)
            action=['u','d','l','r']
            env.step(action[num], 0, agentid)
            env.step(action[num], 1, agentid)
    for teamid in range(2):
        for agentid in range(RED_ARMY):
            env.reset(teamid, int(agentid/2))
    for turn in range(5):
        env.reload()
        for agentid in range(RED_ARMY):
            num = random.randint(0,3)
            action=['u','d','l','r']
            env.step(action[num], 0, agentid)
            env.step(action[num], 1, agentid)
    '''
    for turn in range(500):
        pass

if __name__ == "__main__":
    env = Warmap()
    update()
    test = SarsaTable(actions=['u','d','l','r'])
    env.mainloop()