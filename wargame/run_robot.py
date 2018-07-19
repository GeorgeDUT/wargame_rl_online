from robot_carry import *
import time
from hq import *


robot_NUM = 10
nato_NUM = 10


def update():
    for turn in range(100):
        action_robot = []
        action_nato = []
        for i in range(map.robot_num):
            choice = brain_of_rboto(map)
            action_robot.append(robot[i].move(choice,map))
        for i in range(map.nato_num):
            choice2 = brain_of_nato(map)
            action_nato.append(nato[i].move(choice2, map))
        map.flash(map.robot_num, action_robot,robot)
        map.flash(map.nato_num, action_nato, nato)
        time.sleep(0.01)
    print(map.robot_loc)
    print(map.nato_loc)


if __name__ == "__main__":

    map = ROBOT_MAP(ROBOT_NUM=robot_NUM, NATO_NUM=nato_NUM)
    robot = []
    nato = []
    for i in range(map.robot_num):
        robot.append(ROBOT(x_loc=2*i+1, y_loc=0, id=i, blood=10.0, dirction=(0,1)))
    for i in range(map.nato_num):
        nato.append(NATO(x_loc=2*i+1, y_loc=29, id=i, blood=10.0, dirction=(0,-1)))
    map.init_robot(robot,map.robot_num)
    map.init_nato(nato,map.nato_num)
    map.after(10, update)
    map.mainloop()