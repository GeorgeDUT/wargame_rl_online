import sys

if sys.version_info.major == 2:
    from Tkinter import *
    import Tkinter as tk
else:
    from tkinter import *
    import tkinter as tk

MAP_W = 80
MAP_H = 50
UNIT_PIX = 10

class ROBOT(tk.Tk, object):
    def __init__(self):
        super(ROBOT, self).__init__()
        self.title('robot carry')
        self.geometry('{0}x{1}'.format(MAP_W * UNIT_PIX, MAP_H * UNIT_PIX))
        self._build_map()

    def display_window(self):
        display = Frame(tk)
        Button(display, text= 'show').pack(side=10,anchor=10,fill='red', expand=yes)
        pass

    def _build_map(self):
        pass


map=ROBOT()
map.display_window()
map.mainloop()