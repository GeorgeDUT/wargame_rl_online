import numpy as np
#import tensorflow as tf
import random
import time
import sys

if sys.version_info.major == 2:
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter import *
    import tkinter as tk

UNIT = 20
MAZE_H = 6
MAZE_W = 6
WATER_BLOCK=5
WATER_SIZE_H=1
WATER_SIZE_W=2
WOODS_BLOCK=5
WOODS_SIZE_H=2
WOODS_SIZE_W=2
RED_ARMY = 3
GRAY_ARMY = 1

class Warmap(tk.Tk, object):
    def __init__(self):
        super(Warmap, self).__init__()
        self.title('wargame')
        self.geometry('{0}x{1}'.format(MAZE_H * UNIT, MAZE_W * UNIT))
        self._build_map()
        self.last_state = []
        self.last_dis = 0
        self.new_dis = 0

    def _build_map(self):
        self.canvas = tk.Canvas(self, bg='white',height=MAZE_H*UNIT,width=MAZE_W*UNIT)
        # grids
        for c in range(0, MAZE_W * UNIT, UNIT):
            x0, y0, x1, y1 = c, 0, c, MAZE_H * UNIT
            self.canvas.create_line(x0, y0, x1, y1)
        for r in range(0, MAZE_H * UNIT, UNIT):
            x0, y0, x1, y1 = 0, r, MAZE_H * UNIT, r
            self.canvas.create_line(x0, y0, x1, y1)
        # env_map[][] = id, id 1 is water, id 2 is woods, id 9 is treasure
        self.env_map = []
        for i in range(MAZE_H):
            app = []
            for j in range(MAZE_W):
                app.append(0)
            self.env_map.append(app)
        # water
        for i in range(WATER_BLOCK):
            x = random.randint(1, MAZE_W-WATER_SIZE_W-1)
            y = random.randint(1, MAZE_H-WATER_SIZE_H-1)
            x = int(x)
            y = int(y)
            for k in range(WATER_SIZE_W):
                for m in range(WATER_SIZE_H):
                    self.env_map[x+k][y+m]=1
        # woods
        for i in range(WOODS_BLOCK):
            x = random.randint(2, MAZE_W - WOODS_SIZE_W - 2)
            y = random.randint(2, MAZE_H - WOODS_SIZE_H - 2)
            x = int(x)
            y = int(y)
            for k in range(WOODS_SIZE_W):
                for m in range(WOODS_SIZE_H):
                    self.env_map[x + k][y + m] = 2
        # treasure
        self.env_map[int(MAZE_W/2)][MAZE_H-1] = 9
        # draw
        for i in range(MAZE_H):
            for j in range(MAZE_W):
                if self.env_map[i][j] == 1:
                    self.canvas.create_rectangle(i * UNIT, j * UNIT,
                        (i + 1) * UNIT, (j + 1) * UNIT, fill='blue')
                elif self.env_map[i][j] == 2:
                    self.canvas.create_rectangle(i * UNIT, j * UNIT,
                         (i + 1) * UNIT, (j + 1) * UNIT, fill='green')
                elif self.env_map[i][j] == 9:
                    self.canvas.create_rectangle(i * UNIT, j * UNIT,
                                                 (i + 1) * UNIT, (j + 1) * UNIT, fill='white')
        self.army_loc = []
        self.army = []
        # agent red team
        self.red_army_loc = []
        for i in range(RED_ARMY):
            location = []
            location.append(i)
            location.append(0)
            self.red_army_loc.append(location)
        self.army_loc.append(self.red_army_loc)
        self.red_army = []
        for i in range(RED_ARMY):
            self.red_army.append(self.canvas.create_rectangle(self.red_army_loc[i][0]* UNIT,
                            self.red_army_loc[i][1] * UNIT, (self.red_army_loc[i][0]+ 1) * UNIT,
                            (self.red_army_loc[i][1]+1) * UNIT, fill='red'))
        self.army.append(self.red_army)
        # agent gray team
        self.gray_army_loc = []
        for i in range(GRAY_ARMY):
            location = []
            location.append(i)
            location.append(MAZE_H-1)
            self.gray_army_loc.append(location)
        self.army_loc.append(self.gray_army_loc)
        self.gray_army = []
        for i in range(GRAY_ARMY):
            self.gray_army.append(self.canvas.create_rectangle(self.gray_army_loc[i][0]* UNIT,
                            self.gray_army_loc[i][1] * UNIT, (self.gray_army_loc[i][0]+ 1) * UNIT,
                            (self.gray_army_loc[i][1]+1) * UNIT, fill='black'))
        self.army.append(self.gray_army)
        self.canvas.pack()

    def step(self, action, teamid, agentid):
        for i in range(RED_ARMY):
            self.last_state.append(self.army_loc[0][i])
        self.last_dis=0
        self.new_dis=0
        for i in range(RED_ARMY):
            for j in range(GRAY_ARMY):
                x=abs(self.last_state[i][0]-self.army_loc[1][j][0])
                y=abs(self.last_state[i][1]-self.army_loc[1][j][1])
                self.last_dis=self.last_dis+x+y
        add_x = 0
        add_y = 0
        if action == 'u':
            add_x = 0
            add_y = -1
        elif action == 'd':
            add_x = 0
            add_y = 1
        elif action == 'r':
            add_x = 1
            add_y = 0
        elif action == 'l':
            add_x = -1
            add_y = 0
        if self.army_loc[teamid][agentid][0] + add_x < 0:
            add_x = 0
        if self.army_loc[teamid][agentid][1] + add_y < 0:
            add_y = 0
        if self.army_loc[teamid][agentid][0] + add_x > (MAZE_W-1):
            add_x = 0
        if self.army_loc[teamid][agentid][1] + add_y > (MAZE_H-1):
            add_y = 0
        check_loc_x = self.army_loc[teamid][agentid][0] + add_x
        check_loc_y = self.army_loc[teamid][agentid][1] + add_y
        if self.env_map[check_loc_x][check_loc_y] == 1:
            add_x = 0
            add_y = 0
        self.army_loc[teamid][agentid][0]+=add_x
        self.army_loc[teamid][agentid][1]+=add_y
        self.canvas.move(self.army[teamid][agentid],
                         UNIT * add_x, UNIT * add_y)

        # reward function
        #'''
        s_ = []
        for i in range(RED_ARMY):
            s_.append(self.canvas.coords(self.army[teamid][i]))
        s_.append(self.canvas.coords(self.army[1][0]))
        gray_state = []
        reward = 0
        done = False
        for agent_id in range(GRAY_ARMY):
            gray_state.append(self.canvas.coords(self.army[1][agent_id]))
        for i in range(RED_ARMY):
            if s_[i] in gray_state:
                reward = 0
                done = True
                s_ = 'terminal'
                break
            else:
                reward = 0
                done = False
        #'''
        for i in range(RED_ARMY):
            for j in range(GRAY_ARMY):
                x=abs(self.army_loc[0][i][0]-self.army_loc[1][j][0])
                y=abs(self.army_loc[0][i][1]-self.army_loc[1][j][1])
                self.new_dis=self.new_dis+x+y
        # distance function
        if self.new_dis<self.last_dis:
            reward=abs(self.new_dis-self.last_dis)*abs(self.new_dis-self.last_dis)
        else:
            reward = -1
        # divide function
        dis = 0
        for i in range(RED_ARMY):
            for j in range(RED_ARMY):
                x = abs(self.army_loc[0][i][0] - self.army_loc[0][j][0])
                y = abs(self.army_loc[0][i][1] - self.army_loc[0][j][1])
                dis = dis + x + y
        reward=reward+dis*0.1

        '''
        gray_state = []
        for agent_id in range(GRAY_ARMY):
            gray_state.append(self.canvas.coords(self.army[1][agent_id]))
        s_ = self.canvas.coords(self.army[teamid][agentid])
        if s_ in gray_state:
            reward = 100
            done = True
            s_ = 'terminal'
        else:
            reward = 0
            done = False
        '''

        return  s_, reward, done

    def rand_step(self, action, teamid, agentid, run):
        add_x = 0
        add_y = 0
        if action == 'u':
            add_x = 0
            add_y = -1
        elif action == 'd':
            add_x = 0
            add_y = 1
        elif action == 'r':
            add_x = 1
            add_y = 0
        elif action == 'l':
            add_x = -1
            add_y = 0
        # check boarder
        if self.army_loc[teamid][agentid][0] + add_x < 0:
            add_x = 0
        if self.army_loc[teamid][agentid][1] + add_y < 0:
            add_y = 0
        if self.army_loc[teamid][agentid][0] + add_x > (MAZE_W - 1):
            add_x = 0
        if self.army_loc[teamid][agentid][1] + add_y > (MAZE_H - 1):
            add_y = 0
        check_loc_x = self.army_loc[teamid][agentid][0] + add_x
        check_loc_y = self.army_loc[teamid][agentid][1] + add_y
        if self.env_map[check_loc_x][check_loc_y] == 1:
            add_x = 0
            add_y = 0
        # escape from red army
        for direction in range(4):
            if run ==1:
                for i in range(RED_ARMY):
                    if check_loc_x == self.army_loc[0][i][0] and check_loc_y == self.army_loc[0][i][1]:
                        add_x = add_x * (-1)
                        add_y = add_y * (-1)
                        break
                check_loc_x = self.army_loc[teamid][agentid][0] + add_x
                check_loc_y = self.army_loc[teamid][agentid][1] + add_y

        '''  
        if run == 1:
            for i in range(RED_ARMY):
                if check_loc_x == self.army_loc[0][i][0] and check_loc_y == self.army_loc[0][i][1]:
                    add_x = add_x*(-1)
                    add_y = add_y*(-1)
                    break
        '''
        #check boarder
        if self.army_loc[teamid][agentid][0] + add_x < 0:
            add_x = 0
        if self.army_loc[teamid][agentid][1] + add_y < 0:
            add_y = 0
        if self.army_loc[teamid][agentid][0] + add_x > (MAZE_W - 1):
            add_x = 0
        if self.army_loc[teamid][agentid][1] + add_y > (MAZE_H - 1):
            add_y = 0
        check_loc_x=self.army_loc[teamid][agentid][0] + add_x
        check_loc_y=self.army_loc[teamid][agentid][1] + add_y
        if self.env_map[check_loc_x][check_loc_y]==1:
            add_y=0
            add_x=0
        self.army_loc[teamid][agentid][0] += add_x
        self.army_loc[teamid][agentid][1] += add_y
        self.canvas.move(self.army[teamid][agentid],
                         UNIT * add_x, UNIT * add_y)

    def reload(self,turn):
        if turn > 145:
            time.sleep(0.28)
        else:
            pass
        self.update()

    def reset(self, teamid, agentid):
       #time.sleep(0.1)
        self.update()
        self.canvas.delete(self.army[teamid][agentid])
        self.army_loc[teamid][agentid][0] = agentid
        if teamid == 0:
            self.army_loc[teamid][agentid][1] = 0
        else:
            self.army_loc[teamid][agentid][1] = MAZE_H-1
        if teamid == 0:
            self.army[teamid][agentid] = self.canvas.create_rectangle(self.army_loc[teamid][agentid][0]* UNIT,
                            self.army_loc[teamid][agentid][1] * UNIT, (self.army_loc[teamid][agentid][0]+ 1) * UNIT,
                            (self.army_loc[teamid][agentid][1]+1) * UNIT, fill='red')
        else:
            self.army[teamid][agentid] = self.canvas.create_rectangle(self.army_loc[teamid][agentid][0]* UNIT,
                            self.army_loc[teamid][agentid][1] * UNIT, (self.army_loc[teamid][agentid][0]+ 1) * UNIT,
                            (self.army_loc[teamid][agentid][1]+1) * UNIT, fill='black')
        #'''
        obs = []
        if teamid == 0:
            for i in range(RED_ARMY):
                obs.append(self.canvas.coords(self.army[teamid][i]))
        else:
            for i in range(GRAY_ARMY):
                obs.append(self.canvas.coords(self.army[teamid][i]))
        return obs
        #'''
        #return self.canvas.coords(self.army[teamid][agentid])
