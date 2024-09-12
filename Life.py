from tkinter import *
import time
import random
def Bioscan(r, chance, speed):
    root = Toplevel(r)
    root.title("BIOSCAN")
    root.resizable(False, False)
    canvas = Canvas(root, background='#1B1B1B', highlightthickness=0)
    canvas.pack(fill=BOTH, expand = 1)
    canvas.create_oval(-425, 200, 1450, 650, fill='#FFFFFF', outline = '#FFFFFF')
    for i in range(int(975/speed)):
        time.sleep(0.001)
        rx, ry = r.winfo_x(), r.winfo_y()
        #root.geometry(str(int(i*speed))+"x250" + '+' + str(rx - i * int(speed / 2)) + '+' + str(ry))
        root.geometry(str(int(i*speed))+"x250" + '+' + str(rx + 500) + '+' + str(ry+150))
        if chance != '':
            def go(spawnChance, maxHeight, sizeLow, sizeHigh, col):
                seeLife = random.randint(0, random.randint(1, spawnChance))
                if seeLife == 0:
                    y = random.randint(maxHeight, 235)
                    size = random.randint(sizeLow, sizeHigh)
                    canvas.create_oval(int(i*speed),y,int(i*speed)+size,y+size, outline=col)
            if(chance == 'intelligent'):
                go(25, 210, 8, 12, '#00FF00')
            elif(chance == 'hostile'):
                go(25, 210, 8, 12, '#FF0000')
            elif(chance == 'bacterial'):
                go(1, 0, 2, 3, '#00FF00')
        root.update()
    return root
'''(yPos - int(975/speed))'''