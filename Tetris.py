from tkinter import *
import random
import time
from playsound import playsound



#return a random colour
def colour(): 
    colours = ['red', 'green', 'blue', 'yellow']
    index = random.randint(0,3)
    return colours[index]


#creates a segment with a set position and set dimensions
class Segment:
    def __init__(self, x, y, colour):
        self.x = x
        self.y = y
        self.width = 20
        self.height = 20
        self.colour = colour
        self.move = 20
        
    def draw(self, canvas):
                canvas.create_rectangle(self.x, self.y, self.x+self.width,
                                self.y+self.height, fill = self.colour)


class CompositeBlock:
    #draws shape in correct next position    
    def draw(self, canvas, blocks, level):
        #moves each segment in shape down one position after 0.2seconds has elapsed
        self.end = time.time()
        elapsed = self.end - self.start
        if self.target and elapsed > 0.3 - level * 0.01:
            for segment in self.segments:
                #removes shape as target if it touches the bottom
                if segment.y + segment.move >= 390:
                    self.target = False
                #removes shape as target if it is going to be in the posiotion of  block
                for block in blocks:
                    if segment.y + segment.move == block.y and segment.x == block.x:
                        self.target = False
            #moves the target down one position
            if self.target:
                for segment in self.segments:
                    segment.y += segment.move
                    segment.draw(canvas)
                    self.start = time.time()
        else:
            for segment in self.segments:
                segment.draw(canvas)

    #adds the correct combination and colour of segments to the next canvas
    def drawNext(self, canvas):
        if self.colour == 'yellow':
            segments = [Segment(20, 20, self.colour),
                        Segment(40, 20, self.colour),
                        Segment(20, 40, self.colour),
                        Segment(40, 40, self.colour)]
        if self.colour == 'cyan':
            segments = [Segment(2.00, 30, self.colour),
                        Segment(21.75, 30, self.colour),
                        Segment(41.50, 30, self.colour),
                        Segment(61.25, 30, self.colour)]
        if self.colour == 'blue':
            segments = [Segment(10, 20, self.colour),
                        Segment(10, 40, self.colour),
                        Segment(30, 40, self.colour),
                        Segment(50, 40, self.colour)]
        if self.colour == 'orange':
            segments = [Segment(50, 20, self.colour),
                        Segment(10, 40, self.colour),
                        Segment(30, 40, self.colour),
                        Segment(50, 40, self.colour)]
        if self.colour == 'purple':
            segments = [Segment(30, 20, self.colour),
                        Segment(10, 40, self.colour),
                        Segment(30, 40, self.colour),
                        Segment(50, 40, self.colour)]
        if self.colour == 'green':
            segments = [Segment(30, 20, self.colour),
                        Segment(50, 20, self.colour),
                        Segment(10, 40, self.colour),
                        Segment(30, 40, self.colour)]
        if self.colour == 'red':
            segments = [Segment(10, 20, self.colour),
                        Segment(30, 20, self.colour),
                        Segment(30, 40, self.colour),
                        Segment(50, 40, self.colour)]
        for segment in segments:    
            segment.draw(canvas)

    

#creates yellow tetromino               
class Yellow(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'yellow'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour)]

    def rotateClockwise(self):
        return

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour)]
        
#creates cyan tetromino
class Cyan(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'cyan'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x + 40, self.y, self.colour),
                         Segment(self.x + 60, self.y, self.colour)]

    def rotateClockwise(self):
        if self.configuration >= 2:
            self.configuration -= 2

        if self.configuration == 0:
            self.segments[0].x -= 20
            self.segments[0].y += 20
            self.segments[2].x += 20
            self.segments[2].y -= 20
            self.segments[3].x += 40
            self.segments[3].y -= 40

        if self.configuration == 1:
            self.segments[0].x += 20
            self.segments[0].y -= 20
            self.segments[2].x -= 20
            self.segments[2].y += 20
            self.segments[3].x -= 40
            self.segments[3].y += 40

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x + 40, self.y, self.colour),
                         Segment(self.x + 60, self.y, self.colour)]

#creates blue tetromino
class Blue(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'blue'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour),
                         Segment(self.x + 40, self.y + 20, self.colour)]

    def rotateClockwise(self):
        if self.configuration >= 4:
            self.configuration -= 4

        if self.configuration == 0:
            self.segments[0].x += 20
            self.segments[0].y -= 20
            self.segments[2].x += 20
            self.segments[2].y += 20
            self.segments[3].x += 40
            self.segments[3].y += 40
        
        if self.configuration == 1:
            self.segments[0].x += 20
            self.segments[0].y += 20
            self.segments[2].x -= 20
            self.segments[2].y += 20
            self.segments[3].x -= 40
            self.segments[3].y += 40

        if self.configuration == 2:
            self.segments[0].x -= 20
            self.segments[0].y += 20
            self.segments[2].x -= 20
            self.segments[2].y -= 20
            self.segments[3].x -= 40
            self.segments[3].y -= 40

        if self.configuration == 3:
            self.segments[0].x -= 20
            self.segments[0].y -= 20
            self.segments[2].x += 20
            self.segments[2].y -= 20
            self.segments[3].x += 40
            self.segments[3].y -= 40

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour),
                         Segment(self.x + 40, self.y + 20, self.colour)]       

        
#creates orange tetromino
class Orange(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'orange'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x - 20, self.y + 20, self.colour),
                         Segment(self.x - 40, self.y + 20, self.colour)]

    def rotateClockwise(self):
        if self.configuration >= 4:
            self.configuration -= 4
            
        if self.configuration == 0:
            self.segments[0].x += 20
            self.segments[0].y -= 20
            self.segments[2].x -= 20
            self.segments[2].y -= 20
            self.segments[3].x -= 40
            self.segments[3].y -= 40

        if self.configuration == 1:
            self.segments[0].x += 20
            self.segments[0].y += 20
            self.segments[2].x += 20
            self.segments[2].y -= 20
            self.segments[3].x += 40
            self.segments[3].y -= 40
            
        if self.configuration == 2:
            self.segments[0].x -= 20
            self.segments[0].y += 20
            self.segments[2].x += 20
            self.segments[2].y += 20
            self.segments[3].x += 40
            self.segments[3].y += 40
        
        if self.configuration == 3:
            self.segments[0].x -= 20
            self.segments[0].y -= 20
            self.segments[2].x -= 20
            self.segments[2].y += 20
            self.segments[3].x -= 40
            self.segments[3].y += 40

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x - 20, self.y + 20, self.colour),
                         Segment(self.x - 40, self.y + 20, self.colour)]       


#creates purple tetromino
class Purple(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'purple'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x - 20, self.y + 20, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour)]

    def rotateClockwise(self):
        if self.configuration >= 4:
            self.configuration -= 4

        if self.configuration == 0:
            self.segments[1].x -= 20
            self.segments[1].y -= 20
            self.segments[0].x += 20
            self.segments[0].y -= 20
            self.segments[3].x += 20
            self.segments[3].y += 20

        if self.configuration == 1:
            self.segments[1].x += 20
            self.segments[1].y += 20

        if self.configuration == 2:
            self.segments[0].x -= 20
            self.segments[0].y += 20

        if self.configuration == 3:
            self.segments[3].x -= 20
            self.segments[3].y -= 20

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x - 20, self.y + 20, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour)]        


#creates green tetromino
class Green(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'green'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x - 20, self.y + 20, self.colour)]

    def rotateClockwise(self):
        if self.configuration >= 2:
            self.configuration -= 2

        if self.configuration == 0:
            self.segments[1].x += 20
            self.segments[1].y -= 20
            self.segments[2].x += 20
            self.segments[2].y += 20
            self.segments[3].x -= 0
            self.segments[3].y += 40

        if self.configuration == 1:
            self.segments[1].x -= 20
            self.segments[1].y += 20
            self.segments[2].x -= 20
            self.segments[2].y -= 20
            self.segments[3].x += 0
            self.segments[3].y -= 40

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x, self.y + 20, self.colour),
                         Segment(self.x - 20, self.y + 20, self.colour)]
            

#creates red tetromino
class Red(CompositeBlock):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.configuration = 0
        self.colour = 'red'
        self.start = time.time()
        self.end = time.time()
        self.target = True
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour),
                         Segment(self.x + 40, self.y + 20, self.colour)]
    
    def rotateClockwise(self):
        if self.configuration >= 2:
            self.configuration -= 2

        if self.configuration == 0:
            self.segments[0].x -= 20
            self.segments[0].y += 20
            self.segments[2].x += 20
            self.segments[2].y += 20
            self.segments[3].x += 40
            self.segments[3].y -= 0

        if self.configuration == 1:
            self.segments[0].x += 20
            self.segments[0].y -= 20
            self.segments[2].x -= 20
            self.segments[2].y -= 20
            self.segments[3].x -= 40
            self.segments[3].y += 0

    def reset(self):
        self.segments = [Segment(self.x, self.y, self.colour),
                         Segment(self.x + 20, self.y, self.colour),
                         Segment(self.x + 20, self.y + 20, self.colour),
                         Segment(self.x + 40, self.y + 20, self.colour)]

            
#creates the game window               
class GameWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = colour())
        self.parent = parent

        self.bindKeyboardEvents()
        self.setupLabels()
        self.setupCanvases()
        self.pack(fill=BOTH, expand=1)
        self.blocks = []
        self.shapes = ['Yellow(80, -40)', 'Cyan(60, -20)', 'Blue(80, -40)', 'Orange(120, -40)',
                       'Purple(100, -40)', 'Green(100, -40)', 'Red(80, -40)']
        self.target = eval(random.choice(self.shapes))
        self.next = eval(random.choice(self.shapes))
        self.hold = Cyan(60, -20)
        self.clock1 = time.time()
        self.clock2 = time.time()
        playsound('tetris.mp3', False)
        self.level = 1
        self.score = 0
        self.cleared = 0
        self.end = False
        self.swapped = False

    #binds buttons to functions 
    def bindKeyboardEvents(self):
        self.parent.bind('<Left>', self.Left_Arrow)
        self.parent.bind('<Right>', self.Right_Arrow)
        self.parent.bind('w', self.W)
        self.parent.bind('a', self.A)
        self.parent.bind('s', self.S)
        self.parent.bind('d', self.D)
        self.parent.bind('e', self.E)

    #creates canvases that game takes place in
    def setupCanvases(self):
        self.canvas = Canvas(self, height = 400, width = 200,
                             bg = 'black', relief = 'raised')
        self.canvas.place(x = 50, y = 50)

        self.canvasNext = Canvas(self, height = 80, width = 80,
                                 bg = 'black', relief = 'sunken')
        self.canvasNext.place(x = 285, y = 125)

        self.canvasHold = Canvas(self, height = 80, width = 80,
                                 bg = 'black', relief = 'sunken')
        self.canvasHold.place(x = 285, y = 250)

    #creates a scoreboard and a title for the next canvas
    def setupLabels(self):
        self.scoreboard = Label(self, height = 1, width = 25,
                               font = ('Helvetica', 15), bg = 'dark grey',
                               relief = 'sunken')
        self.scoreboard.place(x = 50, y = 10)

        self.nextlabel = Label(self, height = 1, width = 5,
                               font = ('Helvetica', 15), bg = 'dark grey',
                               relief = 'sunken', text = 'Next:')
        self.nextlabel.place(x = 295, y = 90)

        self.holdlabel = Label(self, height = 1, width = 5,
                               font = ('Helvetica', 15), bg = 'dark grey',
                               relief = 'sunken', text = 'Hold:')
        self.holdlabel.place(x = 295, y = 215)



    def draw(self):
        
        self.canvas.delete(ALL)
        self.clock2 = time.time()
        if self.clock2 - self.clock1 > 84:
            self.clock1 = time.time()
            playsound('tetris.mp3', False)
            

        #creates a new random shape from the list of shapes 
        if not self.target.target:
            for segment in self.target.segments:
                self.blocks.append(segment)
            self.target = self.next
            self.next = eval(random.choice(self.shapes))
            self.swapped = False
        self.target.draw(self.canvas, self.blocks, self.level)

        for block in self.blocks:
            if block.y <= 0:
                self.end = True
                

        #deletes all blocks in a row if there are 10 blocks in the row
        blocksy = []
        deleted_blocks = 0
        deleted_block_y = 400
        for block in self.blocks:
            blocksy.append(block.y)
        blocks_to_clear = []
        for block in self.blocks:
            if blocksy.count(block.y) >= 10:
                blocks_to_clear.append(block)
                deleted_block_y = block.y
                deleted_blocks += 1
        #when blocks are deleted moves all blocks down
        for block in self.blocks:
            if block.y < deleted_block_y:
                block.y += (deleted_blocks / 10) * 20
        for block in blocks_to_clear:
            self.blocks.remove(block)

        #draws all the blocks
        for block in self.blocks:
            block.draw(self.canvas)

        if len(blocks_to_clear) == 10:
            self.score += 40 * self.level
        if len(blocks_to_clear) == 20:
            self.score += 100 * self.level
        if len(blocks_to_clear) == 30:
            self.score += 300 * self.level
        if len(blocks_to_clear) == 40:
            self.score += 1200 * self.level

        self.cleared += len(blocks_to_clear)
        if self.cleared >= 100 and self.level < 16:
            self.cleared -= 100
            self.level += 1
            
        self.scoreboard.configure(text = "level: " + str(self.level) +
                                  " score: " + str(self.score))


        #draws in the canvas for next and hold
        self.canvasNext.delete(ALL)
        self.next.drawNext(self.canvasNext)
        self.canvasHold.delete(ALL)
        self.hold.drawNext(self.canvasHold)



    #makes the arrow keys move the target
    def A(self, event):
        for segment in self.target.segments:
            #checks if move is possible
            if segment.x - segment.move  < 0:
                return
            for block in self.blocks:
                if segment.y == block.y and segment.x - segment.move == block.x:
                    return
        for segment in self.target.segments:
            segment.x -= segment.move
        
    def D(self, event):
        for segment in self.target.segments:
            if segment.x + segment.move > 180:
                return
            for block in self.blocks:
                if segment.y == block.y and segment.x + segment.move == block.x:
                    return
        for segment in self.target.segments:
            segment.x += segment.move

    def Right_Arrow(self, event):
        self.target.configuration += 1
        self.target.rotateClockwise()
        if not self.check_rotate():
            for n in range(0,3):
                self.target.configuration += 1
                self.target.rotateClockwise()    

    def Left_Arrow(self, event):
        for n in range(0,3):
            self.target.configuration += 1
            self.target.rotateClockwise()
        if not self.check_rotate():
            self.target.configuration += 1
            self.target.rotateClockwise()

    def W(self, event):
        move_possible = True
        while move_possible:
            for segment in self.target.segments:
                if  segment.y + segment.move >= 390:
                    move_possible = False
                for block in self.blocks:
                    if  segment.y + segment.move == block.y and segment.x == block.x:
                        move_possible = False
            if move_possible:
                for segment in self.target.segments:
                    segment.y += segment.move
                segment.draw(self.canvas)

    def S(self, event):
        move_possible = True
        for segment in self.target.segments:
            if  segment.y + segment.move >= 390:
                move_possible = False
            for block in self.blocks:
                if  segment.y + segment.move == block.y and segment.x == block.x:
                    move_possible = False
        if move_possible:
            for segment in self.target.segments:
                segment.y += segment.move
            segment.draw(self.canvas)

    def E(self, event):
        if not self.swapped:
            self.hold,self.target = self.target,self.hold
            self.hold.reset()
            self.swapped = True
            
        

    def check_rotate(self):
        for segment in self.target.segments:
            if segment.x < 0 or segment.x > 180 or segment.y >= 400:
                return False
            for block in self.blocks:
                if segment.x == block.x and segment.y == block.y:
                    return False
        return True
        


#intitiates the game
def main():
    master = Tk()
    master.title('TETRIS')
    master.geometry("400x500+300+50")
    game = GameWindow(master)

    while True:
        start = time.time()
        master.update()
        if game.end:
            game.canvas.delete(ALL)
            break
        game.draw()

        #introduce 0.01 second delays between updates
        end = time.time()
        length = end - start
        while length < 0.01:
            end = time.time()
            length = end - start



#runs when run in this window
if __name__ == "__main__":
    main()


