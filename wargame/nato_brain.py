import random
import numpy as np


def brain_of_nato(my_map):
    action_space = ['u', 'd', 'r', 'l', 's']
    action = np.random.choice(action_space)
    if random.random()>1:
        action = 's'
    #action = 's'
    return action

    '''
    if sys.version_info.major == 2:
        action = raw_input('action')
        if action == 'w':
            return_action = 'u'
        elif action == 's':
            return_action = 'd'
        elif action == 'a':
            return_action = 'l'
        elif action == 'd':
            return_action = 'r'
        else:
            return_action = 's'
    else:
        action = input('action')
        if action == 'w':
            return_action = 'u'
        elif action == 's':
            return_action = 'd'
        elif action == 'a':
            return_action = 'l'
        elif action == 'd':
            return_action = 'r'
        else:
            return_action = 's'
    return return_action
    '''