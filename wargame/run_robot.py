'''
this file is main function of all the model
'''

import time
import matplotlib.pyplot as plt
from robot_carry import *
from hq import *
from test_function import *


robot_NUM = 4
nato_NUM = 1


def update():
    for epsid in range(0):
        for step in range(5000):
            action_robot = []
            action_nato = []
            for i in range(my_map.robot_num):
                choice = brain_of_rboto(my_map)
                single_action, s_ = feedback_from_env(my_map, robot, i, choice)
                action_robot.append(single_action)
            for i in range(my_map.nato_num):
                choice2 = brain_of_nato(my_map)
                single_action2, s_2 = feedback_from_env(my_map, nato, i, choice2)
                action_nato.append(single_action2)
            my_map.flash(my_map.robot_num, action_robot,robot)
            my_map.flash(my_map.nato_num, action_nato, nato)
            reward = get_reward_from_env(my_map)
            if reward == 10:
                my_map.restart(robot,nato)
                break
                time.sleep(1)
            loss_agent_test(my_map,step)
    print('end')


if __name__ == "__main__":

    my_map = ROBOT_MAP(ROBOT_NUM=robot_NUM, NATO_NUM=nato_NUM)
    robot = []
    nato = []
    for i in range(my_map.robot_num):
        robot.append(ROBOT(x_loc=i, y_loc=0, id=i, blood=10.0, dirction=(0,1)))
    for i in range(my_map.nato_num):
        nato.append(NATO(x_loc=2, y_loc=2, id=i, blood=10.0, dirction=(0,-1)))
    my_map.init_robot(robot,my_map.robot_num)
    my_map.init_nato(nato,my_map.nato_num)
    my_map.after(10, update)
    my_map.mainloop()
    test_rand_function()
