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

class ROBOT(tk.Tk, object):
    def __init__(self):
        super(ROBOT, self).__init__()
        self.title('robot carry')
        self.geometry('{0}x{1}'.format(MAP_W * UNIT_PIX, MAP_H * UNIT_PIX))
        self.robot_num = ROBOT_NUM
        self.map_start_x = 5
        self.map_start_y = 0

        self.display_window()
        self._build_map()

    def display_window(self):
        fram1=Frame()
        line = tk.Canvas(self, bg='black', height=MAP_H*UNIT_PIX, width=2)
        line.place(x=(self.map_start_x-1)*UNIT_PIX,y=0)
        display = Label(fram1, text='information', bg='white', width=10, height=2, font=("Arial", 16))
        display.pack(side=TOP)
        a=1
        agent_inf = Label(fram1, text=a, bg='red', width=10, height=2, font=("Arial", 16))
        agent_inf.pack(side=TOP)
        fram1.place(x=0,y=0)


    def _build_map(self):
        self.map = tk.Canvas(self, bg='white', height=MAP_H * UNIT_PIX, width=(MAP_W-self.map_start_x) * UNIT_PIX)
        self.map.place(x=self.map_start_x*UNIT_PIX,y=self.map_start_y)
        # gird
        for c in range(0, (MAP_W-self.map_start_x) * UNIT_PIX, UNIT_PIX):
            x0, y0, x1, y1 = c, 0, c, MAP_H * UNIT_PIX
            self.map.create_line(x0, y0, x1, y1)
        for r in range(0, MAP_W * UNIT_PIX, UNIT_PIX):
            x0, y0, x1, y1 = 0, r, MAP_H * UNIT_PIX, r
            self.map.create_line(x0, y0, x1, y1)


map=ROBOT()
map.mainloop()