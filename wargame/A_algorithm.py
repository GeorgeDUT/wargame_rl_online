"""
this file is use to A* algorithm design
a_function is false
"""
import numpy as np
import random


def a_choose_agent(dis):
    choose = []
    for j in range(4):
        for idx in range(dis.shape[0]):
            if idx not in choose:
                mindis = dis[idx][j]
                break
            else:
                pass
        for i in range(dis.shape[0]):
            if i not in choose:
                if dis[i][j]<=mindis:
                    idx = i
                    mindis = dis[idx][j]
            else:
                pass
        choose.append(idx)
    return choose


def a_function(my_map, robot, nato):
    all_ation = []
    goal = []
    goal.append([my_map.nato_loc[0][0], my_map.nato_loc[0][1]-1])
    goal.append([my_map.nato_loc[0][0], my_map.nato_loc[0][1]+1])
    goal.append([my_map.nato_loc[0][0]-1, my_map.nato_loc[0][1]])
    goal.append([my_map.nato_loc[0][0]+1, my_map.nato_loc[0][1]])
    for i in range(my_map.robot_num):
        all_ation.append('s')
    dis = np.zeros(shape=(my_map.robot_num,4))
    for i in range(my_map.robot_num):
        dis[i][0]=abs(my_map.robot_loc[i][0]-goal[0][0])+abs(my_map.robot_loc[i][1]-goal[0][1])
        dis[i][1]=abs(my_map.robot_loc[i][0]-goal[1][0])+abs(my_map.robot_loc[i][1]-goal[1][1])
        dis[i][2]=abs(my_map.robot_loc[i][0]-goal[2][0])+abs(my_map.robot_loc[i][1]-goal[2][1])
        dis[i][3]=abs(my_map.robot_loc[i][0]-goal[3][0])+abs(my_map.robot_loc[i][1]-goal[3][1])
    choose_id = a_choose_agent(dis)
    for i in range(4):
        idx = choose_id[i]
        addx=my_map.robot_loc[idx][0]-goal[i][0]
        addy=my_map.robot_loc[idx][1]-goal[i][1]
        if addx == 0:
            if addy>0:
                all_ation[idx]='u'
            elif addy<0:
                all_ation[idx]='d'
        elif addy == 0:
            if addx>0:
                all_ation[idx]='l'
            elif addx<0:
                all_ation[idx]='r'
        else:
            if random.random()<0.5:
                if addx>0:
                    all_ation[idx]='l'
                elif addx<0:
                    all_ation[idx]='r'
            else:
                if addy>0:
                    all_ation[idx]='u'
                elif addy<0:
                    all_ation[idx]='d'

    for i in range(my_map.robot_num):
        if i not in choose_id:
            idx = i
            addx = my_map.robot_loc[idx][0] - my_map.nato_loc[0][0]
            addy = my_map.robot_loc[idx][1] - my_map.nato_loc[0][1]
            if addx == 0:
                if addy > 0:
                    all_ation[idx] = 'u'
                elif addy < 0:
                    all_ation[idx] = 'd'
            elif addy == 0:
                if addx > 0:
                    all_ation[idx] = 'l'
                elif addx < 0:
                    all_ation[idx] = 'r'
            else:
                if random.random() < 0.5:
                    if addx > 0:
                        all_ation[idx] = 'l'
                    elif addx < 0:
                        all_ation[idx] = 'r'
                else:
                    if addy > 0:
                        all_ation[idx] = 'u'
                    elif addy < 0:
                        all_ation[idx] = 'd'
    return all_ation
