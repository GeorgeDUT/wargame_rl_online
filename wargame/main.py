from map import Warmap
import random
import numpy as np
import pandas as pd
RED_ARMY = 10
GRAY_ARMY = 10
T = 10
gate = 1

class RL(object):
    def __init__(self, action_space, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
        self.actions = action_space
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table = pd.DataFrame(columns=self.actions, dtype=np.float64)
        #print(self.q_table.index)

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

    for turn in range(200):
        # reset all agent
        obs=[]
        action=[]
        for agentid in range(T):
            obs.append(env.reset(0, agentid))
        for agentid in range(T):
            action.append(RL.choose_action(str(obs[agentid])))
        while True:
            env.reload(turn)
            obs_=[]
            reward = []
            action_ = []
            done = []
            for i in range(T):
                obs_.append(0)
                reward.append(0)
                done.append(False)
            for agentid in range(T):
                obs_[agentid], reward[agentid], done[agentid] = env.step(action[agentid],0,agentid)
            for agenteid in range(T):
                action_.append(RL.choose_action(str(obs_[agenteid])))

            for agentid in range(T):
                RL.learn(str(obs[agenteid]), action[agentid], reward[agentid], str(obs_[agentid]), action_[agentid])
            for agentid in range(T):
                obs[agentid]=obs_[agentid]
                action[agentid]= action_[agentid]
            flag = 0
            for agentid in range(T):
                if done[agentid]:
                    flag = 1
            if flag == 1:
                break

            if gate ==1:
                for agentid in range(GRAY_ARMY):
                    num = random.randint(0, 3)
                    ac = ['u', 'd', 'l', 'r']
                    env.rand_step(ac[num], 1, agentid)
            # end while

        if gate == 1:
            for agentid in range(GRAY_ARMY):
                env.reset(1, agentid)
        print(turn)
    #env.destroy()



if __name__ == "__main__":
    env = Warmap()
    RL = SarsaTable(actions=['u','d','l','r'])
    env.after(400,update)
    env.mainloop()