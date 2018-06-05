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
        print(self.q_table)

class Sarsa(RL):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(Sarsa, self).__init__(actions, learning_rate, reward_decay, e_greedy)
    def learn(self, s, a, r, s_, a_):
        pass


def update():
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

if __name__ == "__main__":
    env = Warmap()
    update()
    test = Sarsa(actions=['u','d','l','r'])
    env.mainloop()
    a = [1, 2, 3]
    b = [4, 5]
    c = []
    c.append(a)
    c.append(b)
    a[0]=9
    c[0][0]=99
    print(a)
    print(b)
    print(c)