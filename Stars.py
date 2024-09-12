from tkinter import *
from threading import *
import random
import time
import Planet

MAX_STAR_COUNT = 1200
MIN_STAR_COUNT = 50

class Star:
    def __init__(self, canvas, x, y):
        r, b = random.choice(['D','E','F']), random.choice(['D','E','F'])
        self.color = "#"+r+r+"DD"+b+b
        #self.star = canvas.create_line(x, y, x+1, y, fill=self.color, tags='stars')
        self.star = canvas.create_rectangle(x, y, x+1, y+1, fill=self.color, outline=self.color,tags='stars')
        self.mult = 1 + random.random() / 1.25
        self.flag_for_delete = False
        self.life = 0
        self.y_val = y
    def blink(self, canvas):
        canvas.itemconfig(self.star, fill = '#1b1b1b', outline = self.color)
        canvas.update()
        time.sleep(0.1)
        canvas.itemconfig(self.star, fill = self.color, outline = self.color)
    def move(self, canvas, width, height, length, bump):
        self.life += 1
        c = canvas.coords(self.star)
        canvas.coords(self.star, c[0], c[1], c[0]+(starL-length), c[3])
        c = canvas.coords(self.star)
        canvas.coords(self.star, c[0]+(starL-length) * self.mult, c[1], c[2]+(starL-length) * self.mult, c[3])
        if self.life >= 8:
            c = canvas.coords(self.star)
            r = bump * self.mult
            canvas.coords(self.star, c[0], self.y_val + r, c[2], self.y_val + r)
        if bump == 0:
            canvas.coords(self.star, c[0], self.y_val, c[2], self.y_val)
        if(c[0] > width):
            x = random.randint(0, int(width/random.randint(2, 9)))
            y = random.randint(0, height)
            canvas.coords(self.star, -starL-x, y, -x, y)
            if self.flag_for_delete:
                canvas.delete(self.star)
                stars.remove(self)
    def destroy(self):
        self.flag_for_delete = True

starL = 22
stars = []
speeding = False
speedI = 0

def packStars(canvas, width, height, starCountLow, starCountHigh):
    for i in range(0, random.randint(starCountLow, starCountHigh)):
        x, y = random.randint(0, width), random.randint(0, height)
        stars.append(Star(canvas, x, y))
def animateStars(root, canvas, helpInfo, timeLow, timeHigh):
    global speedI
    bumpChance = random.random() * 5 / 500
    bump = 0
    def flip(event):
        global speeding, speedI
        if (event.keysym == 'Shift_R'):
            speeding = not speeding
            speedI = 0
            root.title('PixelStellar ' + str(min(200, speedI)))
    root.bind("<Shift_R>", flip)
    root.bind("<KeyRelease>", flip)
    count = 0
    iterations = random.randint(timeLow, timeHigh)
    choices = [(0.65, 0.3), (0.3, 0.65)]
    pref = random.choice(choices)
    if (len(stars) <= 180):
        pref = (0.8, 0.1)
    if (len(stars) >= 700):
        pref = (0.1, 0.8)
    #pref = (max(0.1, (750 - len(stars)) / 750), min(0.95, 65 / (750 - len(stars))))
    st = canvas.itemcget(helpInfo, 'text')
    for i in range(iterations):
        canvas.itemconfig(helpInfo, text=st[i*2:])
        starLength = starL
        mult = 1
        '''if(speeding):
            root.title('PixelStellar ' + str(min(200, speedI)))
            i += 1
            starLength = min(int(1.25 * starL), int((1 + (speedI)/500) * starL))
            mult = min((1.2 * mult), ((1 + (speedI)/500)))
            speedI += 1'''
        if speeding:
            root.title('PixelStellar ' + str(min(200, speedI)))
            i = 0
            #starLength = min(int(0.25 * starL), int((1 + (speedI)/500) * starL))
            mult = min((0.2 * mult), ((1 + (speedI)/500)))
            speedI += 1
        x,y = root.winfo_width(), root.winfo_height()
        if False and i > 250:
            y = max((y - int((i - 50) / (100)), 400))
        else:
            y = 500
        rx, ry = root.winfo_x(), root.winfo_y()
        if x + i < 1200:
            rx -= int((i / 4) / 2)
        if (rx + root.winfo_width() >= root.winfo_screenwidth()):
            rx -= int(i / 4)
        if (rx <= 0):
            rx += int((i / 4) / 2)
        root.geometry(str(min(x + int(i / 4), 1200)) + 'x' + str(y) + '+' + str(rx) + '+' + str(ry))
        width = min(x + i, 1200)
        if False and speeding:
            root.after(40)
        else:
            root.after(100 - int((100/starL) * count))
        if random.random() <= pref[0] and len(stars) < MAX_STAR_COUNT:
            stars.append(Star(canvas, -30, random.randint(0, root.winfo_height())))
        if random.random() <= pref[1] and len(stars) > MIN_STAR_COUNT:
            ch = random.choice(stars)
            ch.destroy()
        if random.random() <= bumpChance and bump == 0 and i >= starL:
            bump = random.randint(4, 32)
            bumpChance = random.random() * 5 / 500
        bumpVolatility = 0
        if (bump > 0):
            bumpVolatility = random.randint(-8, 8)
        for star in stars:
            star.move(canvas, root.winfo_width(), root.winfo_height(), (-int(count * mult) + starL), bumpVolatility)
        if bump > 0:
            bump -= 1
        canvas.update()
        Planet.movePlanet(canvas, count, 1)
        if(count < starLength):
            count += 2

    Planet.config(canvas, root.winfo_height())
    rx, ry = root.winfo_x(), root.winfo_y()
    rw, rh = root.winfo_width(), root.winfo_height()
    for i in range(0, starL * 2):
        root.after(20)
        canvas.itemconfig(helpInfo, text=st[-int(i*1.5)-1:], fill = '#5B5B5B')
        x, y = int(rw - ((rw - 500) / (starL * 2 - i))), int(rh - ((rh - 500) / (starL * 2 - i)))
        root.geometry(str(x) + 'x' + str(y) + '+' + str(rx + int((rw - 500) / (starL * 2 - i)/2)) + '+' + str(ry))
        #root.geometry(str(x) + 'x' + str(y) + '+' + str(rx + i * (starL*2 - (starL * 2 - i))) + '+' + str(ry))
        width = min(x + int(i / 2), 1200)
        for star in stars:
            star.move(canvas, width, root.winfo_height(), int(i / 2), 0)
        canvas.update()
        Planet.movePlanet(canvas, int(i / 2), 0.55)