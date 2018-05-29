from map import Warmap
import random
RED_ARMY = 10
GRAY_ARMY = 10

class RL(object):
    def __init__(self,action_space, learning_rate=0.01,reward_decay=0.9,e_greedy=0.9):
        self.actions = action_space
        self.lr = learning_rate
        self.gamma = reward_decay
        self.epsilon = e_greedy

def update():
    for turn in range(600):
        env.reload()
        for agentid in range(RED_ARMY):
            num = random.randint(0,3)
            action=['u','d','l','r']
            env.step(action[num], 0, agentid)
            env.step(action[num], 1, agentid)

if __name__ == "__main__":
    env = Warmap()
    #env.step('d', 9)
    update()
    env.mainloop()