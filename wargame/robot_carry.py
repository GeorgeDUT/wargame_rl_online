from __future__ import division
import sys
import time

if sys.version_info.major == 2:
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter import *
    import tkinter as tk

MAP_W = 50
MAP_H = 30
UNIT_PIX = 25
ROBOT_NUM = 10


def updat():
    print('ok')

class ROBOT(object):
    def __init__(self,x_loc=0,y_loc=0,robot_id=0,num=1):
        super(ROBOT,self).__init__()
        self.x = x_loc
        self.y = y_loc
        self.id = robot_id
        self.num = num

    def move(self, action, ROBOT_MAP):
        def move_up(self):
            return  0, -1
        def move_down(self):
            return  0, 1
        def move_left(self):
            return -1,  0
        def move_right(self):
            return 1, 0
        def move_stay(self):
            return 0, 0
        dic = {'u':move_up(self), 'd':move_down(self), 'l': move_left(self), 'r': move_right(self),'s':move_stay(self)}
        add_x,add_y = dic[action]
        chang_x = self.x+add_x
        chang_y = self.y+add_y
        #check border
        if chang_x<0:
            chang_x = 0
            add_x = 0
        if chang_x>=ROBOT_MAP.map_w-ROBOT_MAP.map_start_x-1:
            chang_x=ROBOT_MAP.map_w-ROBOT_MAP.map_start_x-1
            add_x = 0
        if chang_y<0:
            chang_y = 0
            add_y = 0
        if chang_y>=ROBOT_MAP.map_h-ROBOT_MAP.map_start_y-1:
            chang_y=ROBOT_MAP.map_h-ROBOT_MAP.map_start_y-1
            add_y = 0
        self.x = chang_x
        self.y = chang_y
        return add_x,add_y

class TRUCK(object):
    pass

class WAll(object):
    pass

class PEOPLE(object):
    pass


class ROBOT_MAP(tk.Tk, object):
    def __init__(self):
        super(ROBOT_MAP, self).__init__()
        self.title('robot carry')
        self.geometry('{0}x{1}'.format(MAP_W * UNIT_PIX, MAP_H * UNIT_PIX))
        self.robot_num = ROBOT_NUM
        self.map_start_x = 10
        self.map_start_y = 0
        self.map_w = MAP_W
        self.map_h = MAP_H
        #self.robot_loc = []
        self.env_map = []
        self.robot=[]
        self.truck=[]
        self.people=[]

        self.display_window()
        self._build_map()

    def display_window(self):
        fram1=Frame()
        line = tk.Canvas(self, bg='black', height=MAP_H*UNIT_PIX, width=2)
        line.place(x=(self.map_start_x-1)*UNIT_PIX,y=self.map_start_y)
        display = Label(fram1, text='information', bg='white', width=13, height=2, font=("Arial", 16))
        display.pack(side=TOP)
        a='agent 1'
        agent_inf = Label(fram1, text=a, bg='red', width=13, height=2, font=("Arial", 16))
        agent_inf.pack(side=TOP)
        fram1.place(x=0,y=0)

    def _build_map(self):
        self.map = tk.Canvas(self, bg='white', height=MAP_H * UNIT_PIX, width=(MAP_W-self.map_start_x) * UNIT_PIX)
        self.map.place(x=self.map_start_x*UNIT_PIX,y=self.map_start_y)
        # gird
        for c in range(0, (MAP_W-self.map_start_x) * UNIT_PIX, UNIT_PIX):
            x0, y0, x1, y1 = c, 0, c, MAP_H * UNIT_PIX
            self.map.create_line(x0, y0, x1, y1)
        for r in range(0, MAP_H * UNIT_PIX, UNIT_PIX):
            x0, y0, x1, y1 = 0, r, MAP_W * UNIT_PIX, r
            self.map.create_line(x0, y0, x1, y1)
        # init env_map,env_map[]=1,wall;env_map[]=2
        for i in range(self.map_h):
            a=[]
            for j in range(self.map_w-self.map_start_x):
                a.append(0)
            self.env_map.append(a)

    def init_robot(self, ROBOT):
        for i in range(ROBOT[0].num):
            self.robot.append(self.map.create_rectangle(ROBOT[i].x* UNIT_PIX,
                    ROBOT[i].y * UNIT_PIX, (ROBOT[i].x+ 1) * UNIT_PIX,
                    (ROBOT[i].y+1) * UNIT_PIX, fill='red'))
            print(ROBOT[i].x,ROBOT[i].y)

    def flash(self,num,action):
        # move robot
        time.sleep(0.25)
        for i in range(num):
            add_x = action[i][0]
            add_y = action[i][1]
            self.map.move(self.robot[i],
                             UNIT_PIX * add_x, UNIT_PIX * add_y)
        self.update()





