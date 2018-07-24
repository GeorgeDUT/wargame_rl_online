"""
this file is main function of all the model
hello ubuntu
"""
import time
import matplotlib.pyplot as plt
from robot_carry import *
from hq import *
from test_function import *
from rl_algorithm import *
import matplotlib.pyplot as plt


robot_NUM = 2
nato_NUM = 1


def train_q_tale(episode, point,point2,point3):
    observation_robot = []
    observation_nato = []
    action_robot = []
    action_nato = []
    for i in range(my_map.robot_num):
        observation_robot.append(get_state(my_map, 'robot', i))
        action_robot.append(RL.choose_action(str(observation_robot[i])))
    for i in range(my_map.nato_num):
        observation_nato.append(get_state(my_map, 'nato', i))
        action_nato.append(brain_of_nato(my_map))

    # one episode start
    for step in range(500000):
        observation_robot_next = []
        test_list_clear(observation_robot_next)
        # this action_num use to tell map to flash, format [addx,addy]
        action_robot_num = []
        action_nato_num = []
        # get observation_next and reward
        for i in range(my_map.robot_num):
            single_action, single_observation_robot_next = feedback_from_env(my_map, robot, i, action_robot[i])
            observation_robot_next.append(single_observation_robot_next)
            action_robot_num.append(single_action)
        for i in range(my_map.nato_num):
            single_action2, single_observation_nato_next = feedback_from_env(my_map, nato, i, action_nato[i])
            action_nato_num.append(single_action2)
        # draw robot and nato on may
        my_map.flash(my_map.robot_num, action_robot_num, robot)
        my_map.flash(my_map.nato_num, action_nato_num, nato)

        # get reward
        reward, done = get_reward_from_env(my_map)

        action_robot_next = []
        # action_robot_next.clear()
        for i in range(my_map.robot_num):
            action_robot_next.append(RL.choose_action(str(observation_robot_next[i])))
        for i in range(my_map.robot_num):
            RL.learn(str(observation_robot[i]), action_robot[i], reward,
                     str(observation_robot_next[i]))
        for i in range(my_map.robot_num):
            observation_robot[i] = observation_robot_next[i]
            action_robot[i] = action_robot_next[i]

        if reward == 100:
            my_map.restart(robot, nato)
            print(episode, step, 'surround')
            point.append(step)
            # watch move
            if episode > 1500:
                time.sleep(0.1)
            # watch move
            break
        # watch move
        if episode > 1500:
            time.sleep(0.5)
        # watch move

        # nato random run
        test_list_clear(observation_nato)
        test_list_clear(action_nato)
        for i in range(my_map.nato_num):
            observation_nato.append(get_state(my_map, 'nato', i))
            action_nato.append(brain_of_nato(my_map))


def rand_no_train(episode,point):
    for step in range(50000):
        action_robot_num = []
        action_nato_num = []
        for i in range(my_map.robot_num):
            choice = brain_of_rboto(my_map)
            single_action, s_ = feedback_from_env(my_map, robot, i, choice)
            action_robot_num.append(single_action)
        for i in range(my_map.nato_num):
            choice2 = brain_of_nato(my_map)
            single_action2, s_2 = feedback_from_env(my_map, nato, i, choice2)
            action_nato_num.append(single_action2)
        my_map.flash(my_map.robot_num, action_robot_num, robot)
        my_map.flash(my_map.nato_num, action_nato_num, nato)
        reward = get_reward_from_env(my_map)
        if reward == 10:
            my_map.restart(robot, nato)
            print(step, 'surround')
            break
            time.sleep(1)
    # loss_agent_test(my_map,step)
    # test_robot_map(robot,nato, my_map)


def update():
    point=[]
    point2=[]
    point3=[]
    for episode in range(800):
        # every robot choose a action on observation
        train_q_tale(episode,point,point2,point3)
        time.sleep(0)
    print('end')
    plt.plot(point,color ='red')
    #plt.plot(point2, color='black')
    #plt.plot(point3, color='green')
    plt.show()


if __name__ == "__main__":

    my_map = ROBOT_MAP(ROBOT_NUM=robot_NUM, NATO_NUM=nato_NUM)
    robot = []
    nato = []
    for i in range(my_map.robot_num):
        robot.append(ROBOT(x_loc=i, y_loc=0, id=i, blood=10.0, dirction=(0,1)))
    for i in range(my_map.nato_num):
        nato.append(NATO(x_loc=i, y_loc=2, id=i, blood=10.0, dirction=(0,-1)))
    RL = QLearningTable(actions=list(['u','d','l','r','s']))
    my_map.init_robot(robot,my_map.robot_num)
    my_map.init_nato(nato,my_map.nato_num)

    my_map.after(10, update)
    my_map.mainloop()
    print(RL.q_table)

    # test area

