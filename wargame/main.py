from map import Warmap
import random
import numpy as np
import pandas as pd
import time
import sys
import matplotlib.pyplot as plt
RED_ARMY = 4
GRAY_ARMY = 1
T = 4
# gate =1 gray army random go gate =0 gray army do not go
gate = 1
# if RUN=1, gray army will escape from red army
RUN = 1

class RL(object):
    def __init__(self, action_space, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9, agent_num = 1):
        self.actions = action_space
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy
        self.q_table=[]
        for i in range(agent_num):
            a = pd.DataFrame(columns=self.actions, dtype=np.float64)
            self.q_table.append(a)
        #print(self.q_table.index)

    def check_state_exist(self, state,agent_id):
        if state not in self.q_table[agent_id].index:
            # append new state to q table
            self.q_table[agent_id] = self.q_table[agent_id].append(
                pd.Series(
                    [0] * len(self.actions),
                    index=self.q_table[agent_id].columns,
                    name=state,
                )
            )

    def choose_action(self, observation, agent_id):
        self.check_state_exist(observation,agent_id)
        # action selection
        if np.random.rand() < self.epsilon:
            # choose best action
            state_action = self.q_table[agent_id].loc[observation, :]
            state_action = state_action.reindex(
                np.random.permutation(state_action.index))  # some actions have same value
            action = state_action.idxmax()
        else:
            # choose random action
            action = np.random.choice(self.actions)
        #action = np.random.choice(self.actions)
        return action

    def learn(self, *args):
        pass

class SarsaTable(RL):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9,agent_num = 1):
        super(SarsaTable, self).__init__(actions, learning_rate, reward_decay, e_greedy, agent_num)

    def learn(self, s, a, r, s_, a_, agent_id):
        self.check_state_exist(s_,agent_id)
        q_predict = self.q_table[agent_id].loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table[agent_id].loc[s_, a_]  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table[agent_id].loc[s, a] += self.lr * (q_target - q_predict)  # update

class Qlearning(RL):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9, agent_num = 1):
        super(Qlearning, self).__init__(actions, learning_rate, reward_decay, e_greedy, agent_num)
    def learn(self, s, a, r, s_, a_, agent_id):
        self.check_state_exist(s_, agent_id)
        q_predict = self.q_table[agent_id].loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table[agent_id].loc[s_, :].max()  # next state is not terminal
        else:
            q_target = r  # next state is terminal
        self.q_table[agent_id].loc[s, a] += self.lr * (q_target - q_predict)  # update

class Contorl(object):
    def __init__(self):
        self.red_num=RED_ARMY
        self.gray_num=GRAY_ARMY
        self.red_loc=[]
        self.gray_loc=[]

    def get_env_inf(self, action, teamid):
        for i in range(self.red_num):
            env.step(action[i],teamid,i)
        state=[]
        for i in range(self.red_num):
            state.append(env.army_loc[0][i])
        self.red_loc =state

def Contorl_update():
    our_contorl=Contorl()
    ac=['d','l','d','r']
    for turn in range(10):
        our_contorl.get_env_inf(ac,0)
        env.reload(turn)
        #this is contorl move function
        for i in range(RED_ARMY):
            for j in range(GRAY_ARMY):
                x = abs(env.army_loc[0][i][0] - env.army_loc[1][j][0])
                y = abs(env.army_loc[0][i][1] - env.army_loc[1][j][1])
    pass



def update():
    aver_step = 0
    point = []
    for turn in range(355):
        # reset all agent
        obs=[]
        action=[]
        for agentid in range(T):
            obs.append(env.reset(0, agentid))
        for agentid in range(T):
            action.append(RL.choose_action(str(obs[agentid]),agentid))
        all_step = 0
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
            for agentid in range(T):
                action_.append(RL.choose_action(str(obs_[agentid]),agentid))

            for agentid in range(T):
                RL.learn(str(obs[agentid]), action[agentid], reward[agentid], str(obs_[agentid]), action_[agentid],agentid)
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
                    env.rand_step(ac[num], 1, agentid, RUN)
            all_step=all_step+1
            # end while

        if gate == 1:
            for agentid in range(GRAY_ARMY):
                env.reset(1, agentid)
        aver_step = aver_step+all_step
        #print(turn,all_step,aver_step/(turn+1))
        print(turn, all_step)
        point.append(all_step)

    for i in range(2):
        print(env.army_loc[i])
    plt.plot(point)
    plt.show()
    #env.destroy()


if __name__ == "__main__":

    env = Warmap()
    RL = SarsaTable(actions=['u','d','l','r'],agent_num=RED_ARMY)
    #RL = Qlearning(actions=['u', 'd', 'l', 'r'])
    env.after(400, update)
    env.mainloop()

    #env=Warmap()
    #env.mainloop()
    #my_control=Contorl()
