from tkinter import *
import time
import random
def Mine(r, chance, speed, color):
    root = Toplevel(r)
    root.title("GEOLOGICAL SURVEY")
    root.resizable(False, False)
    #color = '#56341B'
    canvas = Canvas(root, background=color, highlightthickness=0)
    canvas.pack(fill=BOTH, expand = 1)
    root.geometry("300x1" + '+' + str(r.winfo_x() + 100) + '+' + str(r.winfo_y()+530))
    root.update()
    for i in range(int(750/speed)):
        time.sleep(0.001)
        root.geometry("300x"+str(int(i*speed)))
        spawnMineral = random.randint(0, chance)
        if spawnMineral <= 1:
            x = random.randint(0, 280)
            size = random.randint(2,5)
            canvas.create_rectangle(x,int(i*speed),x+size,int(i*speed)+size,fill = "#CFA949", outline = '#CFA949')
            root.update()
        root.update()
    return root
