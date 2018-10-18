"""

"""

from robot_carry import *
import numpy as np
import tensorflow as tf

'''if DRAW_PIC is False, program will not use tkinter'''
DRAW_PIC = True
robot_NUM = 4
nato_NUM = 1


def get_state_full(my_map):
    s = np.zeros((my_map.map_h-my_map.map_start_y,my_map.map_w-my_map.map_start_x))
    for i in range(my_map.map_h-my_map.map_start_y):
        for j in range(my_map.map_w-my_map.map_start_x):
            if my_map.env_map[i][j]=='null':
                s[i][j]=0
            elif my_map.env_map[i][j]=='robot':
                s[i][j]=1
            elif my_map.env_map[i][j]=='nato':
                s[i][j]=2
    return s

def move_all_agent(my_map,action):



def train_dqn(episode,point,ponit2):
    observation_robot = []
    action_robot = []
    action_nato = []
    for i in range(my_map.robot_num):
        observation_robot.append(get_dqn_state(my_map,'robot',i))
    sum_reward=0
    for step in range(99999):
        test_list_clear(action_robot)
        test_list_clear(action_nato)
        for i in range(my_map.robot_num):
            action_robot.append(RL.choose_action(observation_robot[i]))
            action_nato.append(brain_of_nato(my_map))
        observation_robot_next = []
        test_list_clear(observation_robot_next)
        action_robot_num = []
        action_nato_num = []
        # get obs and reward
        for i in range(my_map.robot_num):
            single_action, single_observation_robot_next = feedback_dqn_from_env(my_map, robot,i, action_robot[i])
            observation_robot_next.append(single_observation_robot_next)
            action_robot_num.append(single_action)
        for i in range(my_map.nato_num):
            single_action2, single_observation_nato_next = feedback_from_env(my_map, nato, i, action_nato[i])
            action_nato_num.append(single_action2)
        # draw robot and nato on map
        my_map.flash(my_map.robot_num,action_robot_num,robot)
        my_map.flash(my_map.nato_num,action_nato_num,nato)

        # get reward
        reward, done = get_reward_from_env(my_map,robot,nato)
        sum_reward=sum_reward+reward
        # store
        #for i in range(my_map.robot_num):
            #RL.store_transition(observation_robot[i],action_robot[i],reward,observation_robot_next[i])
        aver_step=0
        for i in range(episode):
            aver_step=point[i]/episode+aver_step
        # this method has no use, will change.todo find another method
        for i in range(my_map.robot_num):
            RL.store_transition(observation_robot[i],action_robot[i],reward,observation_robot_next[i])

        if (step <999999) and (step%5 == 0):
            RL.learn()

        for i in range(my_map.robot_num):
            observation_robot[i]=observation_robot_next[i]

        if done:
            print(episode,step,'surround')
            point.append(step)
            ponit2.append(sum_reward)
            my_map.restart(robot, nato)
            break


def update():
    point=[]
    point2=[]
    point3=[]
    for episode in range(5):
        # every robot choose a action on observation
        # train_q_tale(episode,point,point2,point3)
        train_dqn(episode,point,point2)
        # naive_a_algorithm(my_map,robot,nato,episode,point)
        # rand_no_train(episode,point)
    print('end')

    plt.plot(point,color ='red')
    plt.plot(point2, color='black')
    #plt.plot(point3, color='green')
    plt.show()


if __name__ == "__main__":
    my_map = ROBOT_MAP(ROBOT_NUM=robot_NUM, NATO_NUM=nato_NUM,draw_pic=DRAW_PIC)
    robot = []
    nato = []
    for i in range(my_map.robot_num):
        robot.append(ROBOT(x_loc=i, y_loc=0, id=i, blood=10.0, dirction=(0,1)))
    for i in range(my_map.nato_num):
        nato.append(NATO(x_loc=i, y_loc=2, id=i, blood=10.0, dirction=(0,-1)))
    # RL = QLearningTable(actions=list(['u','d','l','r','s']))

    RL=DQN(my_map.action_num,2,
           learning_rate=0.01,
           reward_decay=0.9,
           e_greedy=0.9,
           replace_target_iter=200,
           memory_size=2000,
           )

    my_map.init_robot(robot,my_map.robot_num)
    my_map.init_nato(nato,my_map.nato_num)




