from map import Warmap
import random
RED_ARMY = 10
def update():
    for turn in range(600):
        env.reload()
        for agentid in range(RED_ARMY):
            num = random.randint(0,3)
            action=['u','d','l','r']
            env.step(action[num],agentid)

if __name__ == "__main__":
    env = Warmap()
    #env.step('d', 9)
    update()
    env.mainloop()