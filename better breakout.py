from tkinter import *
import time
import random

BACKGROUND_COLOUR = 'blue'

def now():
    return int(time.time() * 1000)

class Block:
    def __init__(self):
        self.x = random.randint(0, 480)
        self.y = random.randint(0, 200)
        self.width = 30
        self.height = 10

    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x+30, self.y+10, fill = 'pink')
        

class Rectangle:
    def __init__(self, x, y, scorePosition, playernumb):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 10
        self.movex = 0
        
    def draw(self, canvas):

        if self.x >= 450:
            self.movex = 0
            self.x = 440
            
        if self.x <= 0:
            self.movex = 0
            self.x = 20

        self.x += self.movex
        
        canvas.create_rectangle(self.x,
                                self.y,
                                self.x+self.width,
                                self.y+self.height,
                                fill = 'blue')

    def moveLeft(self):
        self.movex = -1.5

    def moveRight(self):
        self.movex = 1.5

    def stoppage(self):
        self.movex = 0
        
class Oval:
    def __init__(self, x, y):
        self.assignPositions(x,y)
        self.originalSpeed = 1.5
        self.movex = self.originalSpeed
        self.movey = self.originalSpeed
        self.Hangaround = 10

    def assignPositions(self, x, y):
        self.leftX = x
        self.topY = y
        self.centreX = x + 10
        self.centreY = y + 10
        self.bottomY = y + 20
        self.rightX = x + 20

    def draw(self, canvas):
        if (self.Hangaround > 0):
            self.Hangaround -=1
        else:
            newX = self.leftX + self.movex
            newY = self.topY + self.movey
            self.assignPositions(newX, newY)

        canvas.create_oval(self.leftX,self.topY,self.rightX,self.bottomY,fill = 'green')

    def collideWith(self, rectangle):
        # bounce off top
        if self.bottomY > rectangle.y \
           and self.centreX > rectangle.x \
           and self.bottomY < rectangle.y + 10 \
           and self.centreX < rectangle.x + rectangle.width:
                self.movey = -1 * abs(self.movey)
                return True

        if self.topY < rectangle.y + 10 \
           and self.centreX > rectangle.x \
           and self.topY > rectangle.y \
           and self.centreX < rectangle.x + rectangle.width:
                self.movey = abs(self.movey)
                return True

        if self.rightX > rectangle.x \
           and self.
           and self.leftX < rectangle.x + 20 \
           and self.
                self.movey = -1 * abs(self.movey)
                return True

        return False
        

    def colliding(self):
        # bounce off side walls
        if self.leftX <= 0 or self.rightX >= 500:
            self.movex *= -1
        # bounce off top
        if self.topY <= 0:
            self.movey *= -1

        
class EkansGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=BACKGROUND_COLOUR)
        self.score = 0
        self.paddle = Rectangle(480,380, 450, '2')
        self.blocks = []
        for i in range(100):
            self.blocks.append(Block())

        self.lastDrawTime = 0

        self.ball = Oval(10,10)

        master.bind('<KeyPress>', self.KeyPressed)
        master.bind('<KeyRelease>', self.KeyRelease)

        self.bufferFrame = Frame(self,height=100, bg=BACKGROUND_COLOUR)
        self.bufferFrame.pack()

        self.canvas = Canvas(self, height=400, width=500, bg='white')
        self.canvas.pack()
        
        self.pack(fill=BOTH, expand=1)

    def KeyPressed(self, event):
        if (event.keysym == 'Left'):
            self.paddle.moveLeft()
        if (event.keysym == 'Right'):
            self.paddle.moveRight()

    def KeyRelease(self, event):
        if (event.keysym == 'Left'):
            self.paddle.stoppage()
        if (event.keysym == 'Right'):
            self.paddle.stoppage()

    def dueForDraw(self):
        timeSinceLast = now() - self.lastDrawTime
        return timeSinceLast > 5
        
    def draw(self):
        if (self.dueForDraw()):
            self.canvas.delete(ALL)

            self.ball.colliding()
            self.ball.collideWith(self.paddle)
            for block in self.blocks:
                if self.ball.collideWith(block):
                    self.blocks.remove(block)
                    self.score +=1
                    print(self.score)
                else:
                    block.draw(self.canvas)
            self.paddle.draw(self.canvas)
            self.ball.draw(self.canvas)

            self.lastDrawTime = now()

def main():
    mainWindow = Tk()
    mainWindow.geometry("700x700+600+100")
    game = EkansGame(mainWindow)
    while True:
        mainWindow.update()
        game.draw()

if __name__ == '__main__':
    main()
