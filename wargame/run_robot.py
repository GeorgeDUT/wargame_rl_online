from robot_carry import *

if __name__ == "__main__":

    map = ROBOT_MAP()
    robot=[]
    for i in range(5):
        robot.append( ROBOT(x_loc=2*i+1, y_loc=0, robot_id=i,num=5))
    map.init_robot(robot)
    updat()
    map.mainloop()