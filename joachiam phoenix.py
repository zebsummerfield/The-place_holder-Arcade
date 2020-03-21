from tkinter import *
import time

BACKGROUND_COLOUR = 'dark green'

#one pipe moves from right to left
#same pipe reappears from right
#bird boy jumpes up and always falls 
#teleport up on space pressed

def now():
    return int(time.time() * 1000)



class FlappyBird:
    def __init__(self,x, y):
        self.movex = 0
        self.x = x
        self.y = y
        self.tiltUpImage = PhotoImage(file="flap.gif").subsample(10,10)
        self.tiltDownImage = PhotoImage(file="flap1.gif").subsample(10,10)
        self.movingUp = 0
        self.fallingRate = 0.5

    def draw(self,canvas):

        if self.y <= 0:
            self.y = 10
            
        if self.movingUp > 0:
            canvas.create_image(self.x, self.y, image=self.tiltUpImage, anchor=NW)
        else:
            canvas.create_image(self.x, self.y, image=self.tiltDownImage, anchor=NW)

        self.x += self.movex
        self.y += self.fallingRate

        if (self.movingUp > 0):
            self.movingUp -= 1
        else:
            self.fallingRate = 0.5

    def moveUp(self):
        if (self.movingUp == 0):
            self.movingUp = 200
            self.fallingRate = -0.5
            

class Pipey:
    def __init__(self,x,y, imageSrc):
        self.movex = x
        self.x = x
        self.y = y
        self.height = 190
        self.imageP = PhotoImage(file=imageSrc).subsample(2,2)

    def draw(self,canvas):
        if (self.x < 0):
            self.x = 400
        self.x -=0.3
        canvas.create_image(self.x, self.y, image=self.imageP, anchor=NW)

                
class FlappyBord (Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg=BACKGROUND_COLOUR)
        self.FlappyBird = FlappyBird(121,220)
        self.Pipe = Pipey(400, 350, "pipe up.gif")
        self.topPipe = Pipey(400, 0, "pipe down.gif")

        self.score = 0

        self.lastDrawTime = 0

        self.bufferFrame = Frame(self,height=100, bg=BACKGROUND_COLOUR)
        self.bufferFrame.pack()

        self.canvas = Canvas(self, height=500, width=500, bg='white')
        self.canvas.pack()
        
        self.pack(fill=BOTH, expand=1)

        master.bind('<KeyPress>', self.KeyPressed)

    def Reset(self):
        self.FlappyBird.x = 121
        self.FlappyBird.y = 220
        self.score = 0

    def KeyPressed(self, event):
        if (event.keysym == 'space'):
            self.FlappyBird.moveUp()

    def dueForDraw(self):
        timeSinceLast = now() - self.lastDrawTime
        return timeSinceLast > 0.01
        
    def draw(self):
        if (self.dueForDraw()):
            self.canvas.delete(ALL)


            self.FlappyBird.draw(self.canvas)
            self.Pipe.draw(self.canvas)
            self.topPipe.draw(self.canvas)

            
            if self.FlappyBird.y >= 450:
                self.Reset()
                return

            if self.colliding(self.FlappyBird, self.topPipe) or \
                self.colliding(self.FlappyBird, self.Pipe):
                self.Reset()
                return

            if self.PassedAPipe(self.FlappyBird, self.Pipe):
                self.score += 1
                print(self.score)
            
            self.lastDrawTime = now()

    def colliding(self, bird, pipe):
        if bird.x >= pipe.x and bird.y >= pipe.y and bird.y <= pipe.y+pipe.height:
            return True

    def PassedAPipe(self, bird, pipe):
        if bird.x >= pipe.x + 20.5 and bird.x < pipe.x + 21:
            return True
        
def main():
    mainWindow = Tk()
    mainWindow.geometry("700x700+600+100")
    game = FlappyBord(mainWindow)
    while True:
        mainWindow.update()
        game.draw()

if __name__ == '__main__':
    main()

