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

            self.q_table.loc[state,'j']=self.init_j
            self.q_table.loc[state,'s']=self.init_s
            self.q_table.loc[state,'b']=self.init_b

            '''
            # prisoner
            self.q_table.loc[state, 'j'] = self.init_j
            self.q_table.loc[state, 's'] = self.init_s
            # prisoner
            '''

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

        '''
        # prisoner
        if choose >= 0 and choose < softmax_q[0]:
            action = self.actions[0]
        else:
            action = self.actions[1]
        # prisoner
        '''

        return action

    def learn(self, *arg):
        pass


class QLearningSoftmax(RLSoftmax):
    def __init__(self, actions, learning_rate=0.01, reward_decay=0.9, e_greedy=0.9,init_j=5,init_s=0,init_b=0):
        super(QLearningSoftmax, self).__init__(actions, learning_rate, reward_decay, e_greedy)
        self.init_j = init_j
        self.init_s = init_s
        self.init_b = init_b

    def learn(self, s, a, r, s_,time):
        self.check_state_exist(s_)
        q_predict = self.q_table.loc[s, a]
        if s_ != 'terminal':
            q_target = r + self.gamma * self.q_table.loc[s_, :].max()
        else:
            q_target = r
        self.q_table.loc[s, a] += (self.lr/(time*0.0001+1)) * (q_target - q_predict)


def train_softmax(episode,j_gailv,s_gailv,j_o,s_o):
    obs_a=1
    obs_o=1

    while(1):
        action_a=RL.choose_action(str(obs_a))
        #action_o=np.random.choice(['j','s','b'])
        action_o=RL_O.choose_action(str(obs_a))
        # action_o=np.random.choice(['s'])
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
        obs_o_next=1
        action_a_next=RL.choose_action(str(obs_a_next))
        action_o_next=RL_O.choose_action(str(obs_o_next))
        # action_o=np.random.choice(['s'])
        RL.learn(str(obs_a), action_a, reward,str(obs_a_next),episode)
        RL_O.learn(str(obs_o),action_o, -reward,str(obs_o_next),episode)
        action_a=action_a_next
        action_o=action_o_next
        obs_a=obs_a_next
        obs_o=obs_o_next
        gailv=softmax(RL.q_table.loc[str(obs_a),:])
        gailv_o=softmax(RL_O.q_table.loc[str(obs_o),:])
        print(gailv[0],gailv[1],gailv[2],gailv[0]+gailv[1]+gailv[2])
        j_gailv.append(gailv[0])
        s_gailv.append(gailv[1])
        j_o.append(gailv_o[0])
        s_o.append(gailv_o[1])
        #print(gailv_o[0], gailv_o[1], gailv_o[2], gailv_o[0] + gailv_o[1] + gailv_o[2])
        break

    '''
    # prisoner
    while (1):
        action_a = RL.choose_action(str(obs_a))
        action_o = RL_O.choose_action(str(obs_a))
        action_o=np.random.choice(['s'])
        if action_a=='j' and action_o=='j':
            reward_a=-8
            reward_o=-8
        elif action_a=='j' and action_o=='s':
            reward_a=0
            reward_o=-10
        elif action_a=='s' and action_o=='j':
            reward_a=-10
            reward_o=0
        elif action_a=='s' and action_o=='s':
            reward_a=-1
            reward_o=-1
        obs_a_next = 1
        obs_o_next = 1
        action_a_next = RL.choose_action(str(obs_a_next))
        action_o_next = RL_O.choose_action(str(obs_o_next))
        action_o_next = np.random.choice(['s'])
        RL.learn(str(obs_a), action_a, reward_a, str(obs_a_next), episode)
        RL_O.learn(str(obs_o), action_o, reward_o, str(obs_o_next), episode)
        action_a = action_a_next
        action_o = action_o_next
        obs_a = obs_a_next
        obs_o = obs_o_next
        gailv = softmax(RL.q_table.loc[str(obs_a), :])
        gailv_o = softmax(RL_O.q_table.loc[str(obs_o), :])
        j_gailv.append(gailv[0])
        s_gailv.append(gailv[1])
        j_o.append(gailv_o[0])
        s_o.append(gailv_o[1])
        print(episode,gailv[0], gailv[1], gailv[0] + gailv[1] )
        break
    # prisoner
    '''



def update():
    j_gailv=[]
    s_gailv=[]
    j_o=[]
    s_o=[]
    b_o=[]
    for episode in range(6000):
        train_softmax(episode,j_gailv,s_gailv,j_o,s_o)
        b_o.append(1-j_o[episode]-s_o[episode])
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
    b_gailv_1=[]
    b_gailv_2 = []
    b_gailv_3 = []
    b_gailv_4 = []
    b_gailv_5 = []
    b_gailv_6 = []
    for i in range(6000):
        if i<1000:
            j_gailv_1.append(j_gailv[i])
            s_gailv_1.append(s_gailv[i])
            b_gailv_1.append(1-j_gailv[i]-s_gailv[i])
        elif i<2000 and i>=1000:
            j_gailv_2.append(j_gailv[i])
            s_gailv_2.append(s_gailv[i])
            b_gailv_2.append(1 - j_gailv[i] - s_gailv[i])
        elif i<3000 and i>=2000:
            j_gailv_3.append(j_gailv[i])
            s_gailv_3.append(s_gailv[i])
            b_gailv_3.append(1 - j_gailv[i] - s_gailv[i])
        elif i<4000 and i>=3000:
            j_gailv_4.append(j_gailv[i])
            s_gailv_4.append(s_gailv[i])
            b_gailv_4.append(1 - j_gailv[i] - s_gailv[i])
        elif i<5000 and i>=4000:
            j_gailv_5.append(j_gailv[i])
            s_gailv_5.append(s_gailv[i])
            b_gailv_5.append(1 - j_gailv[i] - s_gailv[i])
        elif i<6000 and i>=5000:
            j_gailv_6.append(j_gailv[i])
            s_gailv_6.append(s_gailv[i])
            b_gailv_6.append(1 - j_gailv[i] - s_gailv[i])

    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.plot(j_gailv_1, s_gailv_1, b_gailv_1,color='lightskyblue')
    ax.plot(j_gailv_2, s_gailv_2, b_gailv_2,color='deepskyblue')
    ax.plot(j_gailv_3, s_gailv_3, b_gailv_3,color='dodgerblue')
    ax.plot(j_gailv_4, s_gailv_4, b_gailv_4,color='blue')
    ax.plot(j_gailv_5, s_gailv_5, b_gailv_5,color='darkblue')
    ax.plot(j_gailv_6, s_gailv_6, b_gailv_6,color='black')
    ax.legend()

    '''
    # prisoner
    plt.plot(j_gailv,color='red')
    plt.plot(j_o,color='black')
    # prisoner
    '''

    plt.plot(j_o, s_o,b_o, color='red')
    plt.show()

RL =QLearningSoftmax(actions=list(['j','s','b']),init_j=5,init_s=0,init_b=0)
RL_O=QLearningSoftmax(actions=list(['j','s','b']),init_j=0,init_s=5,init_b=0)
update()
print ('ok')

