from tkinter import *
import random
import time
################################################################################
import Atmosphere
import PrintText
import Mining
import Planet
import Stars
import Life
################################################################################
def beginEvent(eventRoot, bind, eventNum):
    global mineRoot, atmosRoot, lifeRoot, inAnimation
    transparent(None, -1)
    if not inAnimation:
        inAnimation = True
        root.unbind(bind)
        if eventNum == 1:
            mineRoot = Mining.Mine(root, Planet.resources, 4, Planet.color)
            mineRoot.bind("<FocusIn>", lambda event, alpha = 1, root = mineRoot: transparent(event, alpha, root))
            mineRoot.bind("<FocusOut>", lambda event, alpha = 0.25: transparent(event, alpha))
        elif eventNum == 2:
            atmosRoot = Atmosphere.Atmoscan(root, Planet.atmosphere, 4, Planet.color)
            atmosRoot.bind("<FocusIn>", lambda event, alpha = 1, root = atmosRoot: transparent(event, alpha, root))
            atmosRoot.bind("<FocusOut>", lambda event, alpha = 0.25: transparent(event, alpha))
        elif eventNum == 3:
            lifeRoot = Life.Bioscan(root, Planet.life, 4)
            lifeRoot.bind("<FocusIn>", lambda event, alpha = 1, root = lifeRoot: transparent(event, alpha, root))
            lifeRoot.bind("<FocusOut>", lambda event, alpha = 0.25: transparent(event, alpha))
        root.bind("<FocusOut>", lambda event, alpha = 0.25, root = root: transparent(event, alpha, root))
        root.bind("<FocusIn>", lambda event, alpha = 1: transparent(event, alpha))
        inAnimation = False
def destroyRoots():
    roots = [mineRoot, atmosRoot, lifeRoot]
    random.shuffle(roots)
    for i in range(len(roots)):
        try:
            roots[i].destroy()
            root.update()
            time.sleep(0.1)
        except:
            pass
def transparent(event, alpha, clickedRoot = None):
    roots = [mineRoot, atmosRoot, lifeRoot]
    for i in range(len(roots)):
        try:
            if alpha < 0:
                roots[i].unbind("<FocusOut>")
            else:
                roots[i].attributes('-alpha', alpha)
                if alpha == 1:
                    roots[i].lift()
        except:
            pass
    if alpha == 1:
        root.lift()
        if clickedRoot != None:
            clickedRoot.lift()
    root.unbind("<FocusOut>")
def startMine(event):
    beginEvent(mineRoot, 'g', 1)
def startAtmosphere(event):
    beginEvent(atmosRoot, 'a', 2)
def startLife(event):
    beginEvent(lifeRoot, 'b', 3)
mineRoot, atmosRoot, lifeRoot = None, None, None
################################################################################
vis = []
def nextSystem(event):
    global inAnimation
    root.bind('g', startMine)
    root.bind('a', startAtmosphere)
    root.bind('b', startLife)
    if not inAnimation:
        inAnimation = True
        for i in range(len(vis)):
            canvas.delete(vis[0])
            vis.remove(vis[0])
        PrintText.reset(canvas)
        destroyRoots()
        Planet.newSelection()
        Stars.animateStars(root, canvas, helpInfo, 100, 150)#50, 55)#670, 10000)
        y = random.choice([max(10, Planet._y_val - random.randint(-5, 50)),
                           min(root.winfo_height()-190, Planet._y_val + Planet._size + random.randint(-5, 50))])
        x = canvas.coords(Planet.leftMost)
        x[2] = random.choice([min(root.winfo_width() - 180, x[2] + random.randint(-5, 20)),
                              max(10, x[0] - random.randint(-5, 20) - 190)])
        vis.append(canvas.create_line(x[0] + int(Planet._size / 2), Planet._y_val + int(Planet._size/2), x[2]+180 if x[0] > x[2] + 50 else x[2], y+48, fill = 'white'))
        vis.append(canvas.create_line(x[2], y+48, x[2]+180, y+48, fill = 'white'))
        inAnimation = PrintText.printWord(root, canvas, Planet.toStr(), 10, x[2]+10, y)
inAnimation = False
################################################################################
height = 500
width = 500
################################################################################
root = Tk()
root.title("PixelStellar")
root.resizable(False, False)
root.geometry(str(width)+'x'+str(height)+'+475+125')
################################################################################
canvas = Canvas(root, highlightthickness=0, background='#1B1B1B')
canvas.pack(expand=1, fill=BOTH)
helpInfo = canvas.create_text(10, height-13, fill='#1b1b1b', font='consolas', text='', justify='left', anchor='w')
canvas.itemconfig(helpInfo, text = '[G]GEOLOGICAL SURVEY   [B]BIOSCAN   [A]ATMOSPHERIC READING')
Stars.packStars(canvas, width, height, 150, 700)
Planet.pack(canvas, width, height)
################################################################################
root.bind("<FocusOut>", lambda event, alpha = 0.25: transparent(event, alpha))
root.bind("<Return>", nextSystem)
root.mainloop()