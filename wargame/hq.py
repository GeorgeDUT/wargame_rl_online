import numpy as np


def feedback_from_env(my_map, aclass, aclass_id,action):
    single_action = aclass[aclass_id].move(action, my_map)
    #my_map.regist(aclass[aclass_id])
    return single_action

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
