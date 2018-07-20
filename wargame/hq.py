import numpy as np

def brain_of_rboto(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    return action

def brain_of_nato(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    return action

