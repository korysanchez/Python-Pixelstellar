from tkinter import *
import time
import random
def Atmoscan(r, chance, speed, color):
    chance = 100
    root = Toplevel(r)
    root.title("ATMOSPHERIC READING")
    root.resizable(False, False)
    bgColor = '#1B1B1B'
    if chance < 100:
        bgColor = '#009DDE'
    canvas = Canvas(root, background=bgColor, highlightthickness=0)
    canvas.pack(fill=BOTH, expand = 1)
    canvas.create_oval(-425, 200, 1450, 650, fill=color, outline = color)
    rx, ry = r.winfo_x(), r.winfo_y()
    for i in range(int(975/speed)):
        time.sleep(0.001)
        root.geometry(str(int(i*speed))+"x250" + '+' + str(rx - (i * int(speed))) + '+' + str(ry+150))
        spawnPollution = random.randint(0, int((101-chance)/5))
        if spawnPollution == 0 and chance > 11:
            y = random.randint(0, 240)
            size = random.randint(2,5)
            canvas.create_rectangle(int(i*speed),y,int(i*speed)+size,y+size, fill = "#CCCCCC", outline = '#CCCCCC')
            root.update()
        root.update()
    return root
