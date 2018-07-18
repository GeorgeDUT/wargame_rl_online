from robot_carry import *

robot_NUM = 10
nato_NUM = 10

def update():
    for turn in range(30):
        action = []
        for i in range(map.robot_num):
            action.append( robot[i].move('d',map))
        map.flash(map.robot_num, action)
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