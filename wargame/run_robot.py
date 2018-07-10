from robot_carry import *

if __name__ == "__main__":

    map = ROBOT_MAP()
    robot = ROBOT(x_loc=50, y_loc=100, robot_id=10)
    robot.move('s', map)
    map.draw_robot(robot)
    map.mainloop()