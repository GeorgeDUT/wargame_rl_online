"""
this file use to test the function of other model.
"""
import time
import pandas as pd
import numpy as np
from hq import *
import sys
import platform
from A_algorithm import *
import matplotlib.pyplot as plt
from rl_algorithm import *

if sys.version_info.major == 2:
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter import *
    import tkinter as tk


def loss_agent_test(my_map,turn):
    cnt_robot = 0
    cnt_nato = 0
    for i in range(my_map.map_h):
        for j in range(my_map.map_w - my_map.map_start_x):
            if my_map.env_map[i][j] == 'robot':
                cnt_robot = cnt_robot + 1
            elif my_map.env_map[i][j] == 'nato':
                cnt_nato = cnt_nato + 1
    if cnt_robot != my_map.robot_num:
        print(turn, 'lost robot')
        print(cnt_robot)
        print(my_map.env_map)
        print(my_map.robot_loc)
        print(my_map.nato_loc)
        time.sleep(1)
    if cnt_nato != my_map.nato_num:
        print(turn, 'lost nato')
        print(cnt_nato)
        print(my_map.env_map)
        print(my_map.robot_loc)
        print(my_map.nato_loc)


def test_var(new_map):
    new_map.env_map[0][0]='ok'
    #return new_map


def test_index():
    actions = ['a','b','c']
    a = pd.DataFrame(columns=actions,dtype=np.float64)
    a = a.append(pd.Series([0]*len(actions),index = a.columns,name = 'ok'))
    state = 'ok'
    if state not in a.index:
        print('not in a.index')
    else:
        print('in a.index')


def test_rand_function():
    for i in range(100):
        print(np.random.rand())


def test_robot_map(robot, nato, my_map):
    for i in range(my_map.robot_num):
        if robot[i].x == my_map.robot_loc[i][0] and robot[i].y == my_map.robot_loc[i][1]:
            pass
        else:
            print('no loc')
    for i in range(my_map.nato_num):
        if nato[i].x == my_map.nato_loc[i][0] and nato[i].y == my_map.nato_loc[i][1]:
            pass
        else:
            print('no loc')


def test_observation_str(my_map):
    observation = []
    for i in range(my_map.robot_num):
        observation.append(get_state(my_map, 'robot', i))


# this function use to clear the list
def test_list_clear(alist):
    if sys.version_info.major == 3:
        alist.clear()
    else:
        while len(alist) > 0:
            alist.pop()


def test_if_is_not_else():
    b = None
    #b.append(1)
    a = 0 if b is not None else 1
    print('a',a)


def test_os():
    while 1:
        os = platform.version()
        print(os.find('Ubuntu'))
        print(os)


def test_list_to_str():
    l = [[1,2],[1,5],[1,0]]
    r = ''.join(l)
    print (r)


def test_list_newaxis():
    x = np.array([0,1,0,4])
    y = (np.array(x[:2]))
    y2 = (np.array(x[:2]))- (np.array(x[2:4]))
    print(np.array(x[2:4]))
    print(y)
    print(y2)


def test_key_input():
    action = input()
    if action == 'w':
        print('shang')


def test_mouse():
    root = Tk()
    def key(event):
        print ("pressed", repr(event.char))

    def callback(event):
        print ("clicked at", event.x, event.y)

    frame = Frame(root, width=100, height=100)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    frame.pack()
    root.mainloop()


'''jiandan shitou bu'''


def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


class RLSoftmax(object):
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

            self.q_table.loc[state,'j']=1
            self.q_table.loc[state,'s']=0
            self.q_table.loc[state,'b']=0

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # choose action use e_greedy method
        # TODO: softmax method
        softmax_q=softmax(self.q_table.loc[observation,:])
        choose=np.random.rand()
        if choose>=0 and choose<softmax_q[0]:
            action=self.actions[0]
        elif choose>=softmax_q[0] and choose<(softmax_q[0]+softmax_q[1]):
            action=self.actions[1]
        elif choose>=(softmax_q[0]+softmax_q[1]) and choose<(softmax_q[0]+softmax_q[1]+softmax_q[2]):
            action=self.actions[2]
        return action

    def learn(self, *arg):
        pass


class QLearningSoftmax(RLSoftmax):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9):
        super(QLearningSoftmax, self).__init__(actions, learning_rate, reward_decay, e_greedy)

    def learn(self, s, a, r, s_):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r
        self.q_table.loc[s, a] += self.lr * (q_target - q_predict)


def train_softmax(episode,j_gailv,s_gailv):
    obs_a=1
    while(1):
        action_a=RL.choose_action(str(obs_a))
        action_o=np.random.choice(['j','s','b'])
        #action_o='j'
        if action_a==action_o:
            reward=0
        elif action_a=='j' and action_o=='s':
            reward=-1
        elif action_a=='j' and action_o=='b':
            reward=1
        elif action_a=='s' and action_o=='j':
            reward=1
        elif action_a=='s' and action_o=='b':
            reward=-1
        elif action_a=='b' and action_o=='j':
            reward=-1
        elif action_a=='b' and action_o=='s':
            reward=1
        obs_a_next=1
        action_a_next=RL.choose_action(str(obs_a_next))
        RL.learn(str(obs_a), action_a, reward,str(obs_a_next))
        action_a=action_a_next
        obs_a=obs_a_next
        gailv=softmax(RL.q_table.loc[str(obs_a),:])
        print(gailv[0],gailv[1],gailv[2],gailv[0]+gailv[1]+gailv[2])
        j_gailv.append(gailv[0])
        s_gailv.append(gailv[1])
        break


def update():
    j_gailv=[]
    s_gailv=[]
    for episode in range(6000):
        train_softmax(episode,j_gailv,s_gailv)
    j_gailv_1=[]
    s_gailv_1=[]
    j_gailv_2=[]
    s_gailv_2=[]
    j_gailv_3 = []
    s_gailv_3 = []
    j_gailv_4 = []
    s_gailv_4 = []
    j_gailv_5 = []
    s_gailv_5 = []
    j_gailv_6 = []
    s_gailv_6 = []
    for i in range(6000):
        if i<1000:
            j_gailv_1.append(j_gailv[i])
            s_gailv_1.append(s_gailv[i])
        elif i<2000 and i>=1000:
            j_gailv_2.append(j_gailv[i])
            s_gailv_2.append(s_gailv[i])
        elif i<3000 and i>=2000:
            j_gailv_3.append(j_gailv[i])
            s_gailv_3.append(s_gailv[i])
        elif i<4000 and i>=3000:
            j_gailv_4.append(j_gailv[i])
            s_gailv_4.append(s_gailv[i])
        elif i<5000 and i>=4000:
            j_gailv_5.append(j_gailv[i])
            s_gailv_5.append(s_gailv[i])
        elif i<6000 and i>=5000:
            j_gailv_6.append(j_gailv[i])
            s_gailv_6.append(s_gailv[i])
    plt.plot(j_gailv_1, s_gailv_1, color='blue')
    plt.plot(j_gailv_2, s_gailv_2, color='mediumblue')
    plt.plot(j_gailv_3, s_gailv_3, color='darkblue')
    plt.plot(j_gailv_4, s_gailv_4, color='navy')
    plt.plot(j_gailv_5, s_gailv_5, color='midnightblue')
    plt.plot(j_gailv_6, s_gailv_6, color='black')
    plt.show()

RL =QLearningSoftmax(actions=list(['j','s','b']))
update()
print ('ok')





