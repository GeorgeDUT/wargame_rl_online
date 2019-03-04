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

            self.q_table.loc[state,'c']=self.init_c
            self.q_table.loc[state,'d']=self.init_d

    def choose_action(self, observation):
        self.check_state_exist(observation)
        # choose action use e_greedy method
        # TODO: softmax method
        softmax_q=softmax(self.q_table.loc[observation,:])
        choose=np.random.rand()

        if choose>=0 and choose<softmax_q[0]:
            action=self.actions[0]
        else:
            action=self.actions[1]
        return action

    def learn(self, *arg):
        pass


class QLearningSoftmax(RLSoftmax):
    def __init__(self, actions, learning_rate=0.1, reward_decay=0.9, e_greedy=1,init_c=5,init_d=0):
        super(QLearningSoftmax, self).__init__(actions, learning_rate, reward_decay, e_greedy)
        self.init_c = init_c
        self.init_d = init_d

    def learn(self, s, a, r, s_,time):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r
        # self.q_table.loc[s, a] += (self.lr/(time*0.0001+1)) * (q_target - q_predict)
        self.q_table.loc[s, a] += (self.lr) * (q_target - q_predict)


def train_softmax(episode,c_gailv,c_O):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL.choose_action(str(obs_a))
        #action_o=np.random.choice(['j','s','b'])
        action_o=RL_O.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='c' and action_o=='c':
            reward_a=-8
            reward_b=-8
        elif action_a=='c' and action_o=='d':
            reward_a = 0
            reward_b = -10
        elif action_a=='d' and action_o=='c':
            reward_a = -10
            reward_b = 0
        elif action_a=='d' and action_o=='d':
            reward_a = -1
            reward_b = -1

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
        c_gailv.append(gailv[0])
        c_O.append(gailv_o[0])
        print(gailv_o[0])
        break


def train_softmax2(episode,c_gailv,c_O):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL2.choose_action(str(obs_a))
        #action_o=np.random.choice(['j','s','b'])
        action_o=RL_O2.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='c' and action_o=='c':
            reward_a=-8
            reward_b=-8
        elif action_a=='c' and action_o=='d':
            reward_a = 0
            reward_b = -10
        elif action_a=='d' and action_o=='c':
            reward_a = -10
            reward_b = 0
        elif action_a=='d' and action_o=='d':
            reward_a = -1
            reward_b = -1

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
        c_gailv.append(gailv[0])
        c_O.append(gailv_o[0])
        print(gailv_o[0])
        break


def train_softmax3(episode,c_gailv,c_O):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL3.choose_action(str(obs_a))
        #action_o=np.random.choice(['j','s','b'])
        action_o=RL_O3.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='c' and action_o=='c':
            reward_a=-8
            reward_b=-8
        elif action_a=='c' and action_o=='d':
            reward_a = 0
            reward_b = -10
        elif action_a=='d' and action_o=='c':
            reward_a = -10
            reward_b = 0
        elif action_a=='d' and action_o=='d':
            reward_a = -1
            reward_b = -1

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
        c_gailv.append(gailv[0])
        c_O.append(gailv_o[0])
        print(gailv_o[0])
        break


def train_softmax4(episode,c_gailv,c_O):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL4.choose_action(str(obs_a))
        #action_o=np.random.choice(['j','s','b'])
        action_o=RL_O4.choose_action(str(obs_o))
        # action_o=np.random.choice(['s'])
        # 1
        if action_a=='c' and action_o=='c':
            reward_a=-8
            reward_b=-8
        elif action_a=='c' and action_o=='d':
            reward_a = 0
            reward_b = -10
        elif action_a=='d' and action_o=='c':
            reward_a = -10
            reward_b = 0
        elif action_a=='d' and action_o=='d':
            reward_a = -1
            reward_b = -1

        obs_a_next=1
        obs_o_next=1
        action_a_next=RL4.choose_action(str(obs_a_next))
        action_o_next=RL_O4.choose_action(str(obs_o_next))
        RL4.learn(str(obs_a), action_a, reward_a,str(obs_a_next),episode)
        # RL_O4.learn(str(obs_o),action_o, reward_b,str(obs_o_next),episode)
        action_a=action_a_next
        action_o=action_o_next
        obs_a=obs_a_next
        obs_o=obs_o_next
        gailv=softmax(RL4.q_table.loc[str(obs_a),:])
        gailv_o=softmax(RL_O4.q_table.loc[str(obs_o),:])
        c_gailv.append(gailv[0])
        c_O.append(gailv_o[0])
        print(gailv_o[0])
        break





def update():
    c_gailv=[]
    c_o=[]
    # for episode in range(15):
    #     train_softmax(episode,c_gailv,c_o)
    #
    # c_gailv2 = []
    # c_o2 = []
    # for episode in range(15):
    #     train_softmax2(episode, c_gailv2, c_o2)
    #
    # c_gailv3 = []
    # c_o3 = []
    # for episode in range(15):
    #     train_softmax3(episode, c_gailv3, c_o3)

    c_gailv4 = []
    c_o4 = []
    for episode in range(1500):
        train_softmax4(episode, c_gailv4, c_o4)

    fig = plt.figure()

    # plt.plot(c_gailv,'--', color='red')
    # plt.plot(c_o, color='red')
    #
    # plt.plot(c_gailv2, '--', color='blue')
    # plt.plot(c_o2,color='blue')
    # #
    # plt.plot(c_gailv3, '--', color='black')
    # plt.plot(c_o3, color='black')

    plt.plot(c_gailv4, '--', color='green')
    plt.plot(c_o4, color='green')

    plt.show()


RL = QLearningSoftmax(actions=list(['c','d']),init_c=0,init_d=0)
RL_O = QLearningSoftmax(actions=list(['c','d']),init_c=0,init_d=0)

RL2 = QLearningSoftmax(actions=list(['c','d']),init_c=2,init_d=0)
RL_O2 = QLearningSoftmax(actions=list(['c','d']),init_c=2,init_d=0)

RL3 = QLearningSoftmax(actions=list(['c','d']),init_c=2,init_d=0)
RL_O3 = QLearningSoftmax(actions=list(['c','d']),init_c=0,init_d=2)

RL4 = QLearningSoftmax(actions=list(['c','d']),init_c=0,init_d=0)
RL_O4 = QLearningSoftmax(actions=list(['c','d']),init_c=0,init_d=4)


update()
print ('ok')

