import time
import math
import random
from PIL import Image
import colorsys

name = ''
temp = 0
life = 0
color = ''
resources = 0
atmosphere = 0
planetType = 0
image = 0

_size = 0
_y_val = 0
_x_val = 0
leftMost = 0
_close = 0
_ceil = 0
_floor = 0
_primColor = ""
_secColor = ""


def selectInfo(variationFloorLow, variationFloorHigh,
               variationCeilLow, variationCeilHigh,
               sizeLow, sizeHigh,
               closeLow, closeHigh,
               tempLow, tempHigh,
               resourcesLow, resourcesHigh,
               atmosphereLow, atmosphereHigh,
               lifeOdds, intelligentOdds,
               primCols, secCols):
    global name, temp, life, color, resources, atmosphere, _size, _close, _ceil, _floor, _primColor, _secColor
    tempName = ''
    for i in range(random.randint(5, 18)):
        tempName += random.choice(['0','1','2','3','4','5','6','7','8','9','0','a','b','c','d','e','f'])
    name = tempName

    _floor = random.randint(variationFloorLow, variationFloorHigh)
    _ceil = random.randint(variationCeilLow, variationCeilHigh)

    _close = random.randint(closeLow, closeHigh)
    
    _size = random.randint(sizeLow, sizeHigh)
    temp = random.randint(tempLow, tempHigh)
    resources = random.randint(resourcesLow, resourcesHigh)
    atmosphere = random.randint(atmosphereLow, atmosphereHigh)
    
    life = ''
    if random.randint(0,lifeOdds)==0:
        lifePick = random.randint(0,intelligentOdds)
        if lifePick==intelligentOdds-1:
            life='intelligent'
        elif lifePick==intelligentOdds-2:
            life='hostile'
        else:
            life='bacterial'

    
    colChoice = random.randint(0, len(primCols) - 1)
    _primColor = primCols[colChoice]
    _secColor = secCols[colChoice]
    color = _primColor
def newSelection():
    global planetType
    options = ['ice','sand','lush','water','gaseous','rocky']
    weights = (50, 50, 5, 10, 100, 150)
    planetSelection = random.choices(options, weights)
    planetType = planetSelection[0]
    #ceil = random.randint(3, 10)
    #floor = -random.randint(3, 10)
    #close = random.randint(4, 6)
    #variation = random.randint(30, 60)
    #primCols = ['blue', 'tan', 'darkred', 'darkmagenta', 'darkolivegreen', 'slategrey', 'lightskyblue']
    #secCols = ['deepskyblue', 'beige', 'orangered', 'slateblue', 'yellowgreen', 'darkgrey', 'aliceblue']
    #primCols = ['saddlebrown', 'darkslategrey', 'mediumblue', '#303030']
    #secCols = ['sandybrown', 'teal', 'blue', 'orangered']
    #if planetSelection == 'ice':
    #    selectInfo(50, 300, -670, -200, 5, 20, 0, 500, 20, 10)
    #                               size        close?    temperater    resource, atmo, life
    if planetType == 'ice':
        selectInfo(3, 10, 3, 10,    30,60,       4,6,     -670,-200,    5, 20,    0, 500, 20, 10, ['blue', 'lightskyblue', 'deepskyblue'], ['deepskyblue', 'aliceblue', 'slategrey'])
    if planetType == 'sand':
        selectInfo(3, 10, 3, 10,   50,300,       4,6,      104,670,      5,20,     50, 500, 10, 5, ['saddlebrown', 'sandybrown'], ['sandybrown', ''])
    if planetType == 'lush':
        selectInfo(3, 10, 3, 10,   50,200,       4,6,       45,108,       2,10,     0, 500, 5, 5, ['green', 'darkolivegreen'], ['darkolivegreen', ''])
    if planetType == 'water':
        selectInfo(3, 10, 3, 10,   50,300,       4,6,       32,170,       0,5,      0, 500, 0, 25, ['blue', 'darkblue'], ['blue', ''])
    if planetType == 'gaseous':
        selectInfo(3, 10, 3, 10,   100,300,      4,6,     -400,600,      5,15,     200, 500, 50, 5, ['green', 'purple'], ['purple', ''])
    if planetType == 'rocky':
        selectInfo(3, 10, 3, 10,    50,200,      4,6,     -100,800,     12,20,      0, 500, 15, 15, ['darkslategrey', 'darkgrey', 'lightgrey'], ['darkgrey', '', ''])
def pixelate(canvas, _x, _y, width, height, color, pixelSize):
    global leftMost
    pixels = []
    left = 0
    image = Image.open('../Resources/circle2.png')
    image = image.resize((width, height))
    SqDist = ((height - height / 2) ** 2 + (width - width / 2) ** 2) / 2.1
    leftMost = canvas.create_oval(_x+pixelSize, _y+pixelSize, _x + width, _y + height, fill=color, outline='')
    pixels.append(leftMost)
    for y in range(0, height, pixelSize):
        for x in range(0, width, pixelSize):
            if (abs((height/2 - x) ** 2 + (width/2 - y) ** 2 - SqDist) <= height*(pixelSize * 2)/3 ):
                pixel = canvas.create_rectangle(_x+x, _y+y, _x+x+2, _y+y+2, fill = color, outline = '')
                pixels.append(pixel)
    return pixels

#def pixelate2(canvas, _x, _Y, width, height, color, pixelSize):


planet = 0
planetPixels = []
def pack(canvas, width, height):
    global planet
    planet = canvas.create_text(int(width/2), int(height/2), text='Press enter to begin', fill='white',
                                font = ('consolas','24'))
    return planet
def movePlanet(canvas, length, multiplier):
    global planet
    if type(planet) == int:
        c = canvas.coords(planet)
        canvas.coords(planet, c[0]+(length/3)+(length/2), c[1])
    else:
        for pixel in planet:
            c = canvas.coords(pixel)
            canvas.coords(pixel, c[0]+(length/3)+(length/2) * multiplier, c[1],
                        c[2]+(length/3)+(length/2) * multiplier, c[3])
def config(canvas, height):
    global planet, _y_val, _x_val, leftMost
    #planet = canvas.create_oval(0, 0, 0, 0)
    if type(planet) != int:
        for i in range(len(planet)):
            canvas.delete(planet[0])
            planet.remove(planet[0])
    else:
        canvas.delete(planet)
    y = random.randint(int(height / 8), min(int(height / 1.25), height - int(_size * 1.25)))
    _y_val = y
    _x_val = _size + int(_size/2)

    planet = pixelate(canvas, -_size, y, _size, _size, color, 2)

def toStr():
    return [str(name), "planetType: "+str(planetType),
                      "Temperature: "+str(temp)+"º",
                      "Mass: "+str(_size / 100)+"x earth mass"]

        
