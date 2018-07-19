from robot_carry import *
import time

robot_NUM = 5
nato_NUM = 5

def update():
    for turn in range(30):
        action_robot = []
        action_nato = []
        for i in range(map.robot_num):
            action_robot.append(robot[i].move('d',map))
        for i in range(map.nato_num):
            action_nato.append(nato[i].move('u', map))
        map.flash(map.robot_num, action_robot,1)
        map.flash(map.nato_num, action_nato, 2)
        time.sleep(0.25)
        print(robot[map.robot_num-1].x,robot[map.robot_num-1].y)
        print(robot[0].team)

if __name__ == "__main__":

    map = ROBOT_MAP(ROBOT_NUM = robot_NUM, NATO_NUM = nato_NUM)
    robot = []
    nato = []
    for i in range(map.robot_num):
        robot.append(ROBOT(x_loc=5*i+1, y_loc=0, robot_id=i, blood = 10, dirction=(0,1)))
    for i in range(map.nato_num):
        nato.append(NATO(x_loc=5*i, y_loc=29, nato_id=i, blood = 10, dirction=(0,-1)))
    map.init_robot(robot,map.robot_num)
    map.init_nato(nato,map.nato_num)
    map.after(10, update)
    map.mainloop()