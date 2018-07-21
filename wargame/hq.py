'''
in this file:
all the function use to contact env and run_robot
'''
import numpy as np
import time


def feedback_from_env(my_map, aclass, aclass_id,action):
    single_action = aclass[aclass_id].move(action, my_map)
    s_ ='terminal'
    my_map.regist(aclass[aclass_id])
    return single_action, s_


def get_reward_from_env(my_map):
    reward = 0
    if my_map.check_surround('nato', 0):
        print ('surround')
        time.sleep(1)
        reward = 10
    else:
        reward = 0
    return reward


def brain_of_rboto(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    return action


def brain_of_nato(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    return action


class RL(object):
    def __init__(self,ac):
        pass
