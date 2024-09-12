import time


currentLine = 0
texts = []
def printWord(root, canvas, phrases, speed, x, y):
    global currentLine, texts
    for i in range(len(phrases)):
        for j in range(len(phrases[i])):
            text = canvas.create_text(x+j*8, y+currentLine,
                            text=str.lower(phrases[i][j]), font='consolas', fill='#FFFFFF')
            texts.append(text)
            canvas.update()
            root.after(speed)
        currentLine += 13
    return False
def reset(canvas):
    global currentLine, texts
    for i in range(len(texts)):
        canvas.delete(texts[i])
    texts.clear()
    currentLine = 0
