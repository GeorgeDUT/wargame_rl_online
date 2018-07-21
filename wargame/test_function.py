'''this file use to test the function of other modle.
'''
import time
import pandas as pd
import numpy as np


def loss_agent_test(my_map,turn):
    cnt_robot = 0
    cnt_nato = 0
    for i in range(my_map.map_h):
        for j in range(my_map.map_w - my_map.map_start_x):
            if my_map.env_map[i][j] == 'robot':
                cnt_robot = cnt_robot + 1
            elif my_map.env_map[i][j] == 'nato':
                cnt_nato = cnt_nato + 1
    if cnt_robot != my_map.robot_num:
        print(turn, 'lost agent')
        print(cnt_robot)
        print(my_map.env_map)
        print(my_map.robot_loc)
        print(my_map.nato_loc)
        time.sleep(1)


def test_var(new_map):
    new_map.env_map[0][0]='ok'
    #return new_map

def test_index():
    actions = ['a','b','c']
    a = pd.DataFrame(columns=actions,dtype=np.float64)
    a = a.append(pd.Series([0]*len(actions),index = a.columns,name = 'ok'))
    state = 'ok'
    if state not in a.index:
        print('not in a.index')
    else:
        print('in a.index')

def test_rand_function():
    for i in range(100):
        print(np.random.rand())