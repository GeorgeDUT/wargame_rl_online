'''this is without q learning'''
import pandas as pd
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

mpl.rcParams['legend.fontsize'] = 10

def softmax(x):
    return np.exp(x) / np.sum(np.exp(x), axis=0)


class RLSoftmax(object):
    def __init__(self,action_space, learning_rate=0.1,reward_decay=0.9,e_greedy=0.9):
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

            self.q_table.loc[state,'u']=self.init_u
            self.q_table.loc[state,'d']=self.init_d
            self.q_table.loc[state,'l']=self.init_l
            self.q_table.loc[state, 'r'] = self.init_r


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
        else:
            action=self.actions[3]
        return action

    def learn(self, *arg):
        pass


class QLearningSoftmax(RLSoftmax):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9,init_u=5,init_d=0,init_l=0,init_r=0):
        super(QLearningSoftmax, self).__init__(actions, learning_rate, reward_decay, e_greedy)
        self.init_u = init_u
        self.init_d = init_d
        self.init_l = init_l
        self.init_r = init_r

    def learn(self, s, a, r, s_,time):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r
        self.q_table.loc[s, a] += (self.lr/(time*0.0001+1)) * (q_target - q_predict)


def train_softmax(episode,u_gailv,d_gailv,l_gailv,u_o,d_o,l_o):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL.choose_action(str(obs_a))
        #action_o=np.random.choice(['j','s','b'])
        action_o=RL_O.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='u' and action_o=='u':
            reward_a=0
            reward_b=10
        elif action_a=='u' and action_o=='d':
            reward_a = 0
            reward_b = 0
        elif action_a=='u' and action_o=='l':
            reward_a = 0
            reward_b = 8
        elif action_a=='u' and action_o=='r':
            reward_a = 0
            reward_b = 0
        # 2
        if action_a=='d' and action_o=='u':
            reward_a=8
            reward_b=10
        elif action_a=='d' and action_o=='d':
            reward_a = 8
            reward_b = 0
        elif action_a=='d' and action_o=='l':
            reward_a = 7
            reward_b = 1
        elif action_a=='d' and action_o=='r':
            reward_a = 8
            reward_b = 0
        # 3
        if action_a=='l' and action_o=='u':
            reward_a=0
            reward_b=10
        elif action_a=='l' and action_o=='d':
            reward_a = 0
            reward_b = 0
        elif action_a=='l' and action_o=='l':
            reward_a = 0
            reward_b = 8
        elif action_a=='l' and action_o=='r':
            reward_a = 0
            reward_b = 0
        # 4
        if action_a=='r' and action_o=='u':
            reward_a=9
            reward_b=1
        elif action_a=='r' and action_o=='d':
            reward_a = 10
            reward_b = 0
        elif action_a=='r' and action_o=='l':
            reward_a = 10
            reward_b = 8
        elif action_a=='r' and action_o=='r':
            reward_a = 10
            reward_b = 0

        obs_a_next=1
        obs_o_next=1
        action_a_next=RL.choose_action(str(obs_a_next))
        action_o_next=RL_O.choose_action(str(obs_o_next))
        # action_o=np.random.choice(['s'])
        RL.learn(str(obs_a), action_a, reward_a,str(obs_a_next),episode)
        RL_O.learn(str(obs_o),action_o, reward_b,str(obs_o_next),episode)
        action_a=action_a_next
        action_o=action_o_next
        obs_a=obs_a_next
        obs_o=obs_o_next
        gailv=softmax(RL.q_table.loc[str(obs_a),:])
        gailv_o=softmax(RL_O.q_table.loc[str(obs_o),:])
        # print(gailv[0],gailv[1],gailv[2],gailv[3],gailv[0]+gailv[1]+gailv[2]+gailv[3])
        u_gailv.append(gailv[0])
        d_gailv.append(gailv[1])
        l_gailv.append(gailv[2])
        u_o.append(gailv_o[0])
        d_o.append(gailv_o[1])
        l_o.append(gailv_o[2])
        print(gailv_o[0], gailv_o[1], gailv_o[2], gailv_o[3],gailv_o[0] + gailv_o[1] + gailv_o[2]+gailv_o[3])
        break


def train_softmax2(episode,u_gailv,d_gailv,l_gailv,u_o,d_o,l_o):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL2.choose_action(str(obs_a))
        action_o=RL_O2.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='u' and action_o=='u':
            reward_a=0
            reward_b=10
        elif action_a=='u' and action_o=='d':
            reward_a = 0
            reward_b = 0
        elif action_a=='u' and action_o=='l':
            reward_a = 0
            reward_b = 8
        elif action_a=='u' and action_o=='r':
            reward_a = 0
            reward_b = 0
        # 2
        if action_a=='d' and action_o=='u':
            reward_a=8
            reward_b=10
        elif action_a=='d' and action_o=='d':
            reward_a = 8
            reward_b = 0
        elif action_a=='d' and action_o=='l':
            reward_a = 7
            reward_b = 1
        elif action_a=='d' and action_o=='r':
            reward_a = 8
            reward_b = 0
        # 3
        if action_a=='l' and action_o=='u':
            reward_a=0
            reward_b=10
        elif action_a=='l' and action_o=='d':
            reward_a = 0
            reward_b = 0
        elif action_a=='l' and action_o=='l':
            reward_a = 0
            reward_b = 8
        elif action_a=='l' and action_o=='r':
            reward_a = 0
            reward_b = 0
        # 4
        if action_a=='r' and action_o=='u':
            reward_a=9
            reward_b=1
        elif action_a=='r' and action_o=='d':
            reward_a = 10
            reward_b = 0
        elif action_a=='r' and action_o=='l':
            reward_a = 10
            reward_b = 8
        elif action_a=='r' and action_o=='r':
            reward_a = 10
            reward_b = 0

        obs_a_next=1
        obs_o_next=1
        action_a_next=RL2.choose_action(str(obs_a_next))
        action_o_next=RL_O2.choose_action(str(obs_o_next))
        # action_o=np.random.choice(['s'])
        RL2.learn(str(obs_a), action_a, reward_a,str(obs_a_next),episode)
        RL_O2.learn(str(obs_o),action_o, reward_b,str(obs_o_next),episode)
        action_a=action_a_next
        action_o=action_o_next
        obs_a=obs_a_next
        obs_o=obs_o_next
        gailv=softmax(RL2.q_table.loc[str(obs_a),:])
        gailv_o=softmax(RL_O2.q_table.loc[str(obs_o),:])
        # print(gailv[0],gailv[1],gailv[2],gailv[3],gailv[0]+gailv[1]+gailv[2]+gailv[3])
        u_gailv.append(gailv[0])
        d_gailv.append(gailv[1])
        l_gailv.append(gailv[2])
        u_o.append(gailv_o[0])
        d_o.append(gailv_o[1])
        l_o.append(gailv_o[2])
        print('2',gailv_o[0], gailv_o[1], gailv_o[2], gailv_o[3],gailv_o[0] + gailv_o[1] + gailv_o[2]+gailv_o[3])
        break

def train_softmax3(episode,u_gailv,d_gailv,l_gailv,u_o,d_o,l_o):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL3.choose_action(str(obs_a))
        action_o=RL_O3.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='u' and action_o=='u':
            reward_a=0
            reward_b=10
        elif action_a=='u' and action_o=='d':
            reward_a = 0
            reward_b = 0
        elif action_a=='u' and action_o=='l':
            reward_a = 0
            reward_b = 8
        elif action_a=='u' and action_o=='r':
            reward_a = 0
            reward_b = 0
        # 2
        if action_a=='d' and action_o=='u':
            reward_a=8
            reward_b=10
        elif action_a=='d' and action_o=='d':
            reward_a = 8
            reward_b = 0
        elif action_a=='d' and action_o=='l':
            reward_a = 7
            reward_b = 1
        elif action_a=='d' and action_o=='r':
            reward_a = 8
            reward_b = 0
        # 3
        if action_a=='l' and action_o=='u':
            reward_a=0
            reward_b=10
        elif action_a=='l' and action_o=='d':
            reward_a = 0
            reward_b = 0
        elif action_a=='l' and action_o=='l':
            reward_a = 0
            reward_b = 8
        elif action_a=='l' and action_o=='r':
            reward_a = 0
            reward_b = 0
        # 4
        if action_a=='r' and action_o=='u':
            reward_a=9
            reward_b=1
        elif action_a=='r' and action_o=='d':
            reward_a = 10
            reward_b = 0
        elif action_a=='r' and action_o=='l':
            reward_a = 10
            reward_b = 8
        elif action_a=='r' and action_o=='r':
            reward_a = 10
            reward_b = 0

        obs_a_next=1
        obs_o_next=1
        action_a_next=RL3.choose_action(str(obs_a_next))
        action_o_next=RL_O3.choose_action(str(obs_o_next))
        # action_o=np.random.choice(['s'])
        RL3.learn(str(obs_a), action_a, reward_a,str(obs_a_next),episode)
        RL_O3.learn(str(obs_o),action_o, reward_b,str(obs_o_next),episode)
        action_a=action_a_next
        action_o=action_o_next
        obs_a=obs_a_next
        obs_o=obs_o_next
        gailv=softmax(RL3.q_table.loc[str(obs_a),:])
        gailv_o=softmax(RL_O3.q_table.loc[str(obs_o),:])
        # print(gailv[0],gailv[1],gailv[2],gailv[3],gailv[0]+gailv[1]+gailv[2]+gailv[3])
        u_gailv.append(gailv[0])
        d_gailv.append(gailv[1])
        l_gailv.append(gailv[2])
        u_o.append(gailv_o[0])
        d_o.append(gailv_o[1])
        l_o.append(gailv_o[2])
        print('2',gailv_o[0], gailv_o[1], gailv_o[2], gailv_o[3],gailv_o[0] + gailv_o[1] + gailv_o[2]+gailv_o[3])
        break

def update():
    u_gailv=[]
    d_gailv=[]
    l_gailv=[]
    r_gailv=[]
    u_o=[]
    d_o=[]
    l_o=[]
    r_o=[]
    for episode in range(1500):
        train_softmax(episode,u_gailv,d_gailv,l_gailv,u_o,d_o,l_o)
        r_gailv.append(1-u_gailv[episode]-d_gailv[episode]-l_gailv[episode])
        r_o.append(1-u_o[episode]-d_o[episode]-l_o[episode])

    u_gailv2 = []
    d_gailv2 = []
    l_gailv2 = []
    r_gailv2 = []
    u_o2 = []
    d_o2 = []
    l_o2 = []
    r_o2 = []
    for episode in range(1500):
        train_softmax2(episode, u_gailv2, d_gailv2, l_gailv2, u_o2, d_o2, l_o2)
        r_gailv2.append(1 - u_gailv2[episode] - d_gailv2[episode] - l_gailv2[episode])
        r_o2.append(1 - u_o2[episode] - d_o2[episode] - l_o2[episode])

    u_gailv3 = []
    d_gailv3 = []
    l_gailv3 = []
    r_gailv3 = []
    u_o3 = []
    d_o3 = []
    l_o3 = []
    r_o3 = []
    for episode in range(1500):
        train_softmax3(episode, u_gailv3, d_gailv3, l_gailv3, u_o3, d_o3, l_o3)
        r_gailv3.append(1 - u_gailv3[episode] - d_gailv3[episode] - l_gailv3[episode])
        r_o3.append(1 - u_o3[episode] - d_o3[episode] - l_o3[episode])

    fig = plt.figure()
    # ax = fig.gca(projection='3d')
    # ax.plot(u_gailv, d_gailv,color='blue')
    # ax.legend()

    plt.plot(r_gailv, d_gailv,'--', color='red')
    plt.plot(u_o, l_o, color='red')

    plt.plot(r_gailv2,d_gailv2, '--',color='blue')
    plt.plot(u_o2,l_o2, color='blue')

    plt.plot(r_gailv3, d_gailv3,'--', color='black')
    plt.plot(u_o3, l_o3, color='black')


    plt.show()


RL = QLearningSoftmax(actions=list(['u','d','l','r']),init_u=0,init_d=0,init_l=0,init_r=-0.1)
RL_O = QLearningSoftmax(actions=list(['u','d','l','r']),init_u=-1,init_d=0,init_l=-1,init_r=0)

RL2 = QLearningSoftmax(actions=list(['u','d','l','r']),init_u=3,init_d=0,init_l=2,init_r=0)
RL_O2 = QLearningSoftmax(actions=list(['u','d','l','r']),init_u=0,init_d=0,init_l=0,init_r=8)

RL3 = QLearningSoftmax(actions=list(['u','d','l','r']),init_u=0,init_d=0,init_l=0,init_r=0)
RL_O3 = QLearningSoftmax(actions=list(['u','d','l','r']),init_u=0,init_d=0,init_l=0,init_r=0)


update()
print ('ok')

