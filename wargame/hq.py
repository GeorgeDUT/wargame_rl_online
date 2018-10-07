"""
in this file:
all the function use to contact env and run_robot
define reward:
    1)surround version:
        if nato is surrounded by robot, get reward 100
        other situation, get reward 0
"""

import numpy as np
import time


def get_state(my_map,class_name, agent_id):
    s = []
    if class_name == 'robot':
        a = int(my_map.robot_loc[agent_id][0])
        b = int(my_map.robot_loc[agent_id][1])
        s.append(a)
        s.append(b)
        '''
        for i in range(my_map.map_h-my_map.map_start_y):
            for j in range(my_map.map_w-my_map.map_start_x):
                if my_map.env_map[i][j] == 'robot':
                    x = j
                    y = i
                    s.append([x,y])
        '''
        for i in range(my_map.map_h-my_map.map_start_y):
            for j in range(my_map.map_w-my_map.map_start_x):
                if my_map.env_map[i][j] == 'nato':
                    x = j
                    y = i
                    s.append(x)
                    s.append(y)
    if class_name == 'nato':
        s = 'null'
    return str(s)


def get_full_state(my_map,class_name, agent_id):
    s = np.array()
    if class_name == 'robot':
        a = int(my_map.robot_loc[agent_id][0])
        b = int(my_map.robot_loc[agent_id][1])
        s.append(a)
        s.append(b)
        for i in range(my_map.map_h-my_map.map_start_y):
            for j in range(my_map.map_w-my_map.map_start_x):
                if my_map.env_map[i][j] == 'robot':
                    x = j
                    y = i
                    s.append(x)
                    s.append(y)
        for i in range(my_map.map_h-my_map.map_start_y):
            for j in range(my_map.map_w-my_map.map_start_x):
                if my_map.env_map[i][j] == 'nato':
                    x = j
                    y = i
                    s.append(x)
                    s.append(y)
    if class_name == 'nato':
        s = 'null'
    return str(s)


def get_dqn_state(my_map,class_name, agent_id):
    s = []
    a = 0
    b = 0
    if class_name == 'robot':
        for i in range(my_map.robot_num):
            for j in range(my_map.nato_num):
                a = a+(my_map.robot_loc[i][0]-my_map.nato_loc[j][0])
                b = b+(my_map.robot_loc[i][1]-my_map.nato_loc[j][1])
        s.append(a)
        s.append(b)
    else:
        s.append(0)
        s.append(0)
    s_return = np.array(s[:2])

    return s_return


def feedback_from_env(my_map, aclass, aclass_id, action):
    single_action = aclass[aclass_id].move(action, my_map)
    my_map.regist(aclass[aclass_id])
    s_ = get_state(my_map, aclass[aclass_id].class_name, aclass_id)
    return single_action, s_


def feedback_dqn_from_env(my_map, aclass, aclass_id, action):
    if action == 0:
        action='u'
    elif action == 1:
        action='d'
    elif action == 2:
        action='l'
    elif action == 3:
        action='r'
    elif action == 4:
        action ='s'
    single_action = aclass[aclass_id].move(action, my_map)
    my_map.regist(aclass[aclass_id])
    s_ = get_dqn_state(my_map, aclass[aclass_id].class_name, aclass_id)
    return single_action, s_


def get_reward_from_env(my_map,robot,nato):
    for i in range(my_map.nato_num):
        if my_map.check_surround('nato',i) and nato[i].state == 'live':
            my_map.remove_agent(nato[i],i)
    sum = 0
    for i in range(my_map.nato_num):
        if nato[i].state == 'dead':
            sum = sum+1
    if sum == my_map.nato_num:
        reward = 10
        done = True
    else:
        reward = 0
        done = False
    return reward,done




