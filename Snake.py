from tkinter import *
import random
import time

def colour():
    colours = ['red', 'green', 'blue', 'yellow']
    index = random.randint(0,3)
    return colours[index]

def ran20():
    n = random.randint(0,19)
    return n

class SnakeSegment:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x+self.width,
                                self.y+self.height, fill = 'green')
        
class Snake:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.movex = 0
        self.movey = 0
        self.end = False
        self.segments = [SnakeSegment(x, y)]

    def draw(self, canvas, score):
        #if you've scored (in fruit class) add a segment
        if len(self.segments) < score:
            self.segments.append(SnakeSegment(self.x, self.y))
            
        #changes position of all the segments
        for index,segment in enumerate(self.segments):
            
            #changes the position of the head
            if index == 0:
                next_x = self.x
                next_y = self.y
                self.x += self.movex
                self.y += self.movey
                segment.x = self.x
                segment.y = self.y
                
            #changes the position of each of the other segments
            else:
                old_x = segment.x
                old_y = segment.y
                segment.x = next_x
                segment.y = next_y
                next_x = old_x
                next_y = old_y
            segment.draw(canvas)
            
        #ends the game if the head touches the edge
        if self.y < 0 or self.y > 380:
            self.end = True
        if self.x < 0 or self.x > 380:
            self.end = True

        for index in range(len(self.segments)-1):
            if (self.x == self.segments[index+1].x and
                self.y == self.segments[index+1].y):
                self.end = True
            

class Fruit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.score = 1

    def draw(self, canvas, snake):
        if (((self.x >= snake.x and self.x <= snake.x+20) or
            (self.x+10 >= snake.x and self.x+10 <= snake.x+20)) and
            ((self.y >= snake.y and self.y <= snake.y+20) or
             (self.y+10 >= snake.y and self.y+10 <= snake.y+20))):
            self.score += 1
            self.x = ran20()*20 + 5
            self.y = ran20()*20 + 5
        canvas.create_oval(self.x, self.y,
                           self.x+10, self.y+10,
                           fill = 'red')

class GameWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = colour())
        #Frame(self,height=50).pack()
        self.parent = parent

        self.bindKeyboardEvents()

        self.snake = Snake(180,180)
        self.fruit = Fruit(ran20()*20+5,ran20()*20+5)

        self.setupScoreboard()
        self.setupCanvas()
        
        self.pack(fill=BOTH, expand=1)

    def bindKeyboardEvents(self):
        self.parent.bind('<Left>', self.Left_Arrow)
        self.parent.bind('<Right>', self.Right_Arrow)
        self.parent.bind('<Up>', self.Up_Arrow)
        self.parent.bind('<Down>', self.Down_Arrow)

    def setupCanvas(self):
        self.canvas = Canvas(self, height = 400, width = 400,
                             bg = 'dark grey', relief = 'raised')
        self.canvas.pack()

    def setupScoreboard(self):
        self.scoreboard = Label(self, height = 1, width = 5,
                               font = ('Helvetica', 30), bg = 'light grey',
                               relief = 'sunken')
        self.scoreboard.pack()

    def draw(self):
        self.canvas.delete(ALL)
        self.score_text = str(self.fruit.score)
        self.scoreboard.configure(text = self.score_text)
        if not self.snake.end:
            self.fruit.draw(self.canvas, self.snake)
            self.snake.draw(self.canvas, self.fruit.score)
        else:
            self.canvas.create_text(200,200, fill = 'black',
                               font = 'Helvetica 40 bold',
                               text = 'GAME OVER')

    def Left_Arrow(self, event):
        self.snake.movex = -20
        self.snake.movey = 0
        
    def Right_Arrow(self, event):
        self.snake.movex = 20
        self.snake.movey = 0
        
    def Up_Arrow(self, event):
        self.snake.movex = 0
        self.snake.movey = -20
        
    def Down_Arrow(self, event):
        self.snake.movex = 0
        self.snake.movey = 20


def main():
    master = Tk()
    master.title('SNAKE')
    master.geometry("500x500+100+100")
    game = GameWindow(master)

    while True:
        start = time.time()
        master.update()
        game.draw()

        #introduce delay between redraws
        end = time.time()
        length = end - start
        while length < 0.1:
            end = time.time()
            length = end - start

if __name__ == "__main__":
    main()
                             
