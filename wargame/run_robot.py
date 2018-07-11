from robot_carry import *

if __name__ == "__main__":

    map = ROBOT_MAP()
    robot = ROBOT(x_loc=39, y_loc=29, robot_id=10)
    robot.move('s', map)
    map.init_robot(robot)
    robot.move('u', map)
    map.init_robot(robot)
    updat()
    map.mainloop()