from tkinter import *
import random
import time

def colour():
    colours = ['red', 'green', 'blue', 'yellow']
    index = random.randint(0,3)
    return colours[index]

class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movex = 0
        self.score = 0
        self.speed = 2

    def draw(self, canvas):
        if self.x <= 0 or self.x >= 360:
            self.movex *= -1
        self.x += self.movex     
        canvas.create_rectangle(self.x, self.y, self.x+40, self.y+10, fill = 'orange')

class Ball:
    def __init__(self, x, y):
        self.colour = colour()
        self.x = x
        self.y = y
        self.movex = 2.5
        self.movey = 1.5
        self.scored = False
        self.wait = False

    def draw(self, canvas):
        self.x += self.movex
        self.y += self.movey
        canvas.create_oval(self.x, self.y, self.x+20, self.y+20, fill = self.colour)

    def collisions(self, paddle1, paddle2):
        if self.x <= 0 or self.x >= 380:
            self.movex *= -1
        if self.y <= 0:
            self.movey *= -1
            paddle2.score += 1
            self.scored = True
            self.colour = colour()
        if self.y >= 380:
            self.movey *= -1
            paddle1.score += 1
            self.scored = True
            self.colour = colour()
        if self.y <= 20 and self.x+10 >= paddle1.x and self.x+10 <= paddle1.x+40:
            self.movey *= -1
            #if round(self.y,2) == 20:
            #    self.movex *= (random.randint(5,15)/10)
        if self.y >= 360 and self.x+10 >= paddle2.x and self.x+10 <= paddle2.x+40:
            self.movey *= -1
            #if round(self.y,2) == 360:
            #    self.movex *= (random.randint(5,15)/10)
        


class GameWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = colour())

        parent.bind('a', self.A)
        parent.bind('d', self.D)
        parent.bind('<Left>', self.Left_Arrow)
        parent.bind('<Right>', self.Right_Arrow)

        self.paddle1 = Paddle(180,10)
        self.paddle2 = Paddle(180,380)
        self.ball = Ball(190,190)
        self.speed = 2

        #Frame(self,height=10).pack()
        self.score_box = Label(self, height = 1, width = 10,
                               font = ('Helvetica', 30), bg = 'light grey',
                               relief = 'sunken')
        self.score_box.pack()
        self.canvas = Canvas(self, height=400, width=400,
                             bg = 'dark grey', relief = 'raised')
        self.canvas.pack()

        self.pack(fill=BOTH, expand=1)

    def draw(self):
        self.score_text = str(self.paddle1.score) + ' : ' + str(self.paddle2.score)
        self.score_box.configure(text = self.score_text)
        self.canvas.delete(ALL)
        self.ball.collisions(self.paddle1, self.paddle2)
        if self.ball.wait:
            self.ball.wait = False
            time.sleep(1)
        if self.ball.scored:
            self.ball.x = 190
            self.ball.y = 190
            self.paddle1.x = 180
            self.paddle2.x = 180
            self.ball.scored = False
            self.ball.wait = True
        self.paddle1.draw(self.canvas)
        self.paddle2.draw(self.canvas)
        self.ball.draw(self.canvas)
        

    def A(self, event):
        self.paddle1.movex =-self.paddle1.speed
    def D(self, event):
        self.paddle1.movex = self.paddle1.speed
    def Left_Arrow(self, event):
        self.paddle2.movex = -self.paddle2.speed
    def Right_Arrow(self, event):
        self.paddle2.movex = self.paddle2.speed


def main():
    master = Tk()
    master.geometry("500x500+100+100")
    game = GameWindow(master)
    
    while True:
        start = time.time()
        master.update()
        game.draw()

        #introduce wait till delay between redraws
        end = time.time()
        length = end - start
        while length < 0.01:
            end = time.time()
            length = end - start

if __name__ == '__main__':
    main()
    
