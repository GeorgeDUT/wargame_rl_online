'''this file use to test the function of other modle.
'''
import time

def loss_agent(my_map,turn):
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
