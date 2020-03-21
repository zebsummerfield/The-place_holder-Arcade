from tkinter import *
import time
import random

BACKGROUND_COLOUR = 'blue'

def now():
    return int(time.time() * 1000)

class Rectangle:
    def __init__(self, x, y, scorePosition, playernumb):
        self.x = x
        self.y = y
        self.width = 50
        
        self.height = 10
        self.movex = 0
        self.score = 0
        self.scorePosition = scorePosition
        self.playernumb = playernumb

    def draw(self, canvas):

        if self.x <= 0:
            self.movex = 0
            self.x = 10


        if self.x >= 450:
            self.movex = 0
            self.x = 440

        self.x += self.movex
        canvas.create_text(self.x -10, self.y, text=self.playernumb)
        canvas.create_text(self.scorePosition, 227, text='Score ' + self.playernumb + ' = ' + str(self.score))
        
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
        self.x = x
        self.y = y
        self.originalSpeedx = 1.2
        self.originalSpeedy = 0.8
        self.movex = self.originalSpeedx
        self.movey = self.originalSpeedy
        self.Hangaround = 10

    def draw(self, canvas):
        if (self.Hangaround > 0):
            self.Hangaround -=1
        else:
            self.x += self.movex
            self.y += self.movey

        canvas.create_oval(self.x,self.y,self.x+20,self.y+20,fill = 'green')

    def colliding(self, paddle1, paddle2):
        if self.x <= 0 or self.x >= 480:
            self.movex *= -1
            
        if self.y <= 0:
            self.movey *= -1
            paddle1.score +=1
            self.movey = self.originalSpeedy
            self.movex = self.originalSpeedx
            self.x = 225
            self.y = 225
            self.Hangaround = 100
            print ("Player One Score = " + str(paddle1.score))
            print ("Player Two Score = " + str(paddle2.score))
            
            
        if self.y >= 480:
            self.movey *= -1
            paddle2.score +=1
            self.movey = self.originalSpeedy
            self.movex = self.originalSpeedx
            self.x = 225
            self.y = 225
            self.Hangaround = 100
            print ("Player One Score = " + str(paddle1.score))
            print ("Player Two Score = " + str(paddle2.score))
    
        if self.x > paddle1.x \
            and self.x < paddle1.x + paddle1.width \
            and self.y < paddle1.y + paddle1.height:
                self.movey = abs(self.movey)
                self.movex *= 1.05
                self.movey *= 1.05

        if self.y > paddle2.y - 20 \
           and self.x > paddle2.x \
           and self.x < paddle2.x+paddle2.width:
                self.movey = -1 * abs(self.movey)
                self.movex *= 1.05
                self.movey *= 1.05
        
class EkansGame(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=BACKGROUND_COLOUR)
        self.rect1 = Rectangle(10,10, 50, '1')
        self.rect2 = Rectangle(480,480, 450, '2')

        self.lastDrawTime = 0

        self.oval1 = Oval(10,10)

        master.bind('<KeyPress>', self.KeyPressed)
        master.bind('<KeyRelease>', self.KeyRelease)

        self.bufferFrame = Frame(self,height=100, bg=BACKGROUND_COLOUR)
        self.bufferFrame.pack()

        self.canvas = Canvas(self, height=500, width=500, bg='white')
        self.canvas.pack()
        
        self.pack(fill=BOTH, expand=1)

    def KeyPressed(self, event):
        if (event.keysym == 'a'):
            self.rect1.moveLeft()
        if (event.keysym == 'd'):
            self.rect1.moveRight()
        if (event.keysym == 'Left'):
            self.rect2.moveLeft()
        if (event.keysym == 'Right'):
            self.rect2.moveRight()

    def KeyRelease(self, event):
        if (event.keysym == 'a'):
            self.rect1.stoppage()
        if (event.keysym == 'd'):
            self.rect1.stoppage()
        if (event.keysym == 'Left'):
            self.rect2.stoppage()
        if (event.keysym == 'Right'):
            self.rect2.stoppage()

    def dueForDraw(self):
        timeSinceLast = now() - self.lastDrawTime
        return timeSinceLast > 5
        
    def draw(self):
        if (self.dueForDraw()):
            self.canvas.delete(ALL)

            self.oval1.colliding(self.rect1, self.rect2)
            
            self.rect1.draw(self.canvas)
            self.rect2.draw(self.canvas)
            self.oval1.draw(self.canvas)

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

