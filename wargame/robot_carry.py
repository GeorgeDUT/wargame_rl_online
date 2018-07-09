from __future__ import division
import sys

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


class ROBOT(object):
    def __init__(self,x_loc=0,y_loc=0,robot_id=0):
        super(ROBOT,self).__init__()
        self.x = x_loc
        self.y = y_loc
        self.id = robot_id

    def move(self, action, ROBOT_MAP):
        def move_up(self):
            return self.x - 1, self.y
        def move_down(self):
            return self.x + 1, self.y
        def move_left(self):
            return self.x, self.y - 1
        def move_right(self):
            return self.x, self.y + 1
        dic = {'u':move_up(self), 'd':move_down(self), 'l': move_left(self), 'r': move_right(self)}
        chang_x, chang_y = dic[action]
        #check border
        if chang_x<ROBOT_MAP.map_start_x:
            chang_x = ROBOT_MAP.map_start_x
        if chang_x>=ROBOT_MAP.map_w:
            chang_x=ROBOT_MAP.map_w
        if chang_y<ROBOT_MAP.map_start_y:
            chang_y=ROBOT_MAP.map_start_y
        if chang_y>=ROBOT_MAP.map_h:
            chang_y=ROBOT_MAP.map_h
        self.x = chang_x
        self.y = chang_y


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
        self.robot_loc = []
        self.env_map = []

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

    def hello(self):
        print('hi')





map=ROBOT_MAP()
robot=ROBOT(x_loc=1000,y_loc=100)
robot.move('r', map)
map.mainloop()