from tkinter import *
import Pong
import Snake
import Tetris
import NaughtsAndCrosses
#import SpaceInvaders


class GameWindow(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent, bg = 'brown')
        self.parent = parent

        self.pack(fill=BOTH, expand=1)

        self.title_box = Label(self, width = 50, font = ('Helvetica', 30),
                               bg = 'light grey', relief = 'sunken',
                               text = 'The End Racism Arcade')
        self.game1 = Button(self, text = 'Pong', command = Pong.main,
                            width = 16, bg = 'dark grey', relief = 'raised',
                            font = ('Helvetica', 30))
        self.game2 = Button(self, text = 'Snake', command = Snake.main,
                            width = 16, bg = 'dark grey', relief = 'raised',
                            font = ('Helvetica', 30))
        self.game3 = Button(self, text = 'Tetris', command = Tetris.main,
                            width = 16, bg = 'dark grey', relief = 'raised',
                            font = ('Helvetica', 30))
        self.game4 = Button(self, text = 'NaughtsAndCrosses',
                            command = NaughtsAndCrosses.main, width = 16,
                            bg = 'dark grey', relief = 'raised',
                            font = ('Helvetica', 30))
        #self.game5 = Button(self, text = 'SpaceInvaders',
                            #command = SpaceInvaders.main, width = 16,
                            #bg = 'dark grey', relief = 'raised',
                            #font = ('Helvetica', 30))
        self.title_box.pack()
        self.game1.pack()
        self.game2.pack()
        self.game3.pack()
        self.game4.pack()
        #self.game5.pack()

def game():
    master = Tk()
    master.title('ARCADE')
    master.geometry("500x500+100+100")
    game = GameWindow(master)

if __name__ == '__main__':
    game()
