"""
this file use to test the function of other model.
"""
import time
import pandas as pd
import numpy as np
from hq import *
import sys
import platform
from A_algorithm import *

if sys.version_info.major == 2:
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter import *
    import tkinter as tk


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
        print(turn, 'lost robot')
        print(cnt_robot)
        print(my_map.env_map)
        print(my_map.robot_loc)
        print(my_map.nato_loc)
        time.sleep(1)
    if cnt_nato != my_map.nato_num:
        print(turn, 'lost nato')
        print(cnt_nato)
        print(my_map.env_map)
        print(my_map.robot_loc)
        print(my_map.nato_loc)


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


def test_robot_map(robot, nato, my_map):
    for i in range(my_map.robot_num):
        if robot[i].x == my_map.robot_loc[i][0] and robot[i].y == my_map.robot_loc[i][1]:
            pass
        else:
            print('no loc')
    for i in range(my_map.nato_num):
        if nato[i].x == my_map.nato_loc[i][0] and nato[i].y == my_map.nato_loc[i][1]:
            pass
        else:
            print('no loc')


def test_observation_str(my_map):
    observation = []
    for i in range(my_map.robot_num):
        observation.append(get_state(my_map, 'robot', i))


# this function use to clear the list
def test_list_clear(alist):
    if sys.version_info.major == 3:
        alist.clear()
    else:
        while len(alist) > 0:
            alist.pop()


def test_if_is_not_else():
    b = None
    #b.append(1)
    a = 0 if b is not None else 1
    print('a',a)


def test_os():
    while 1:
        os = platform.version()
        print(os.find('Ubuntu'))
        print(os)


def test_list_to_str():
    l = [[1,2],[1,5],[1,0]]
    r = ''.join(l)
    print (r)


def test_list_newaxis():
    x = np.array([0,1,0,4])
    y = (np.array(x[:2]))
    y2 = (np.array(x[:2]))- (np.array(x[2:4]))
    print(np.array(x[2:4]))
    print(y)
    print(y2)


def test_key_input():
    action = input()
    if action == 'w':
        print('shang')


def test_mouse():
    root = Tk()
    def key(event):
        print ("pressed", repr(event.char))

    def callback(event):
        print ("clicked at", event.x, event.y)

    frame = Frame(root, width=100, height=100)
    frame.bind("<Key>", key)
    frame.bind("<Button-1>", callback)
    frame.pack()
    root.mainloop()




