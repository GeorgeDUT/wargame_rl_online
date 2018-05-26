from tkinter import *
import tkinter as tk
import numpy as np
#import tensorflow as tf
import random
import time
import sys
#def bulid_map(self):

UNIT = 20
MAZE_H = 50
MAZE_W = 50
WATER_BLOCK=4
WATER_SIZE_H=7
WATER_SIZE_W=2
WOODS_BLOCK=9
WOODS_SIZE_H=3
WOODS_SIZE_W=3
RED_ARMY = 10
top=tk.Tk()
top.geometry('{0}x{1}'.format(MAZE_H*UNIT,MAZE_H*UNIT))
top.title('war-game')
top.canvas=tk.Canvas(top, bg='white',height=MAZE_H*UNIT,width=MAZE_W*UNIT)
for c in range(0,MAZE_W*UNIT,UNIT):
    x0,y0,x1,y1=c,0,c,MAZE_H*UNIT
    top.canvas.create_line(x0,y0,x1,y1)
for r in range(0,MAZE_H*UNIT,UNIT):
    x0,y0,x1,y1=0,r,MAZE_H*UNIT,r
    top.canvas.create_line(x0,y0,x1,y1)
warmap=[]
print(warmap)
for i in range(MAZE_W):
    app=[]
    for j in range(MAZE_H):
        app.append(0)
    warmap.append(app)
water_x = np.empty((3, 3))
water_y = np.empty((3, 3))
for i in range(WATER_BLOCK):
        x = random.randint(2, MAZE_H-WATER_SIZE_H-2)
        y = random.randint(2, MAZE_W-WATER_SIZE_W-2)
        x=int(x)
        y=int(y)
        for k in range(WATER_SIZE_H):
            for m in range(WATER_SIZE_W):
                warmap[x+k][y+m]=1
for i in range(WOODS_BLOCK):
        x = random.randint(2, MAZE_H-WOODS_SIZE_H-2)
        y = random.randint(2, MAZE_W-WOODS_SIZE_H-2)
        x=int(x)
        y=int(y)
        for k in range(WOODS_SIZE_H):
            for m in range(WOODS_SIZE_W):
                warmap[x+k][y+m]=2

for i in range(MAZE_H):
    for j in range(MAZE_W):
        if warmap[i][j]==1:
            top.canvas.create_rectangle(i * UNIT, j * UNIT,
                                        (i + 1) * UNIT, (j + 1) * UNIT, fill='blue')
        elif warmap[i][j]==2:
            top.canvas.create_rectangle(i * UNIT, j * UNIT,
                                        (i + 1) * UNIT, (j + 1) * UNIT, fill='green')
agent_move=['u','d','l','r']
agent=[]
for i in range(RED_ARMY):
    agent.append(top.canvas.create_rectangle((i)*UNIT,0*UNIT,(i+1)*UNIT,1*UNIT,fill='red'))
top.canvas.pack()
agent_loc=[0,0,1,1]
for i in range(0,1000):
    x=random.randint(-1,1)
    y=random.randint(-1,1)
    if agent_loc[0]+x<0:
        x=0
    if agent_loc[1]+y<0:
        y=0
    if agent_loc[0] + x > MAZE_W:
        x = 0
    if agent_loc[1] + y > MAZE_H:
        y = 0
    top.canvas.move(agent[0],UNIT*x,UNIT*y)
    agent_loc[0]=agent_loc[0]+x
    agent_loc[1]=agent_loc[1]+y
    top.update()
    time.sleep(0.1)
agent2 = top.canvas.create_rectangle(0*UNIT,0*UNIT,1*UNIT,1*UNIT,fill='black')
top.mainloop()