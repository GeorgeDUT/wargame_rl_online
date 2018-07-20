from robot_carry import *
import time
from hq import *


robot_NUM = 4
nato_NUM = 1


def update():
    for turn in range(3000):
        action_robot = []
        action_nato = []
        for i in range(my_map.robot_num):
            choice = brain_of_rboto(my_map)
            #choice = 'd'
            action_robot.append(robot[i].move(choice,my_map))
            my_map.regist(robot[i])
        for i in range(my_map.nato_num):
            choice2 = brain_of_nato(my_map)
            #choice2 = 'u'
            action_nato.append(nato[i].move(choice2, my_map))
            my_map.regist(nato[i])
        my_map.flash(my_map.robot_num, action_robot,robot)
        my_map.flash(my_map.nato_num, action_nato, nato)
        # surround one
        if my_map.check_surround('nato',0):
            print ('surround')
            time.sleep(3)
            my_map.restart(robot,nato)
            time.sleep(3)


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