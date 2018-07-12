from robot_carry import *

def update():
    for turn in range(50):
        action = []
        for i in range(5):
            action.append( robot[i].move('d',map))
        map.flash(robot[0].num, action)
        print(robot[0].x,robot[0].y)

if __name__ == "__main__":

    map = ROBOT_MAP()
    robot=[]
    for i in range(5):
        robot.append( ROBOT(x_loc=2*i+1, y_loc=0, robot_id=i,num=5))
    map.init_robot(robot)
    map.after(10, update)
    map.mainloop()