
from tkinter import *
import time
import random

BAKAROONEYCOLORE = 'red'


class space (Frame):
    def __init__ (self, master):
        Frame.__init__(self, master, bg = BAKAROONEYCOLORE)
        self.bufferFrame = Frame (self, height = 100, bg = BAKAROONEYCOLORE)
        self.bufferFrame.pack()
        self.canvas = Canvas(self, height = 500, width = 500, bg = 'black')
        self.canvas.pack()
        self.lvlcounter = 1
        self.neowwwwpewpew = fighter(240, 475)

        self.score = 0
        
        self.lives = 3
        self.drawinglives()

        self.levelcounter()
        
        self.pack(fill=BOTH, expand = 1)
        
        self.boreeses = []
        self.borrets = []
        self.explosions = []
        
        self.levelone()
        
        master.bind('d',self.neowwwwpewpew.dPressed)
        master.bind('<space>',self.neowwwwpewpew.SpacePressed)
        master.bind('a',self.neowwwwpewpew.aPressed)

    def levelcounter(self):
        self.canvas2 = Canvas(self, height = 40, width = 100, bg = 'white')
        self.canvas2.pack()
        self.redrawLevelCounter()

    def redrawLevelCounter(self):
        self.canvas2.delete(ALL)
        self.canvas2.create_text(50,20,fill="black",font="Times 20 italic",text=("Level",self.lvlcounter))

    def levelone(self):
        for i in range (7):
            self.boreeses.append(boreesesmovement(15 + 42*i, 5, self.canvas))
            self.boreeses.append(boreesesmovement(15 + 42*i, 50, self.canvas))
            self.boreeses.append(boreesesmovement(15 + 42*i, 95, self.canvas))
            self.boreeses.append(boreesesmovement(15 + 42*i, 140, self.canvas))
            self.boreeses.append(boreesesmovement(15 + 42*i, 185, self.canvas))
            self.boreeses.append(boreesesmovement(15 + 42*i, 230, self.canvas))

    def shootback(self):
        if len(self.boreeses) >= 3:
            chosenboreeses = random.sample(self.boreeses, k = 3)
        else:
            chosenboreeses = random.sample(self.boreeses, k = 1)
        for boreeseplace in chosenboreeses:
            self.borrets.append(borret(boreeseplace.x, boreeseplace.y))
        
    def lifesystem(self):
        if self.lives == 1:
            print('you lose, loser')
            self.boreeses = []
            self.borrets = []
            self.neowwwwpewpew.bulyeets = []
            self.lives = 3
            self.levelcounter = 1
            self.levelone()
            return
        else:
            self.lives -= 1

    def drawinglives(self):
        self.canvas3 = Canvas(self, height = 30, width = 75, bg = 'white')
        self.canvas3.pack()
        self.redrawlifecounter()

    def redrawlifecounter(self):
        self.canvas3.delete(ALL)
        self.canvas3.create_text(38, 15, fill = 'black', font='Times 10 italic', text = "Lives left = %d" %(self.lives))
    
    def update(self):
        shouldShoot = False
        self.canvas.delete(ALL)
        self.redrawlifecounter()
        for borreet in self.borrets:
            borreet.draw(self.canvas)
        for guy in self.boreeses:
            if (guy.draw(self.canvas)):
                shouldShoot = True
            if guy.y >= 435:
                print('you lose, loser')
                self.boreeses = []
                self.levelone()
                self.levelcounter == 1
                break
        if (shouldShoot):
            self.shootback()

        for explosion in self.explosions:
            if (explosion.drawingtheexplosion(self.canvas)):
                self.explosions.remove(explosion)
        
        if len(self.boreeses) == 0:
            print('You win! You have saved the world from the ominous threat of Boreese... for now')
            self.nextLevel()
            
        self.neowwwwpewpew.draw(self.canvas)
        self.Aliensgettinghit(self.boreeses, self.neowwwwpewpew.bulyeets)
        self.bulletcollisions(self.borrets, self.neowwwwpewpew.bulyeets)
        self.AliensHittingback(self.borrets,self.neowwwwpewpew)

    def scoreaddhundred(self):
        self.score +=100

    def nextLevel(self):
        self.lvlcounter +=1
        self.redrawLevelCounter()
        for i in range (6+self.lvlcounter):
            xPos = 15 + (50 - 6*self.lvlcounter)*i
            self.boreeses.append(boreesesmovement(xPos, 5, self.canvas))
            self.boreeses.append(boreesesmovement(xPos, 50, self.canvas))
            self.boreeses.append(boreesesmovement(xPos, 95, self.canvas))
            self.boreeses.append(boreesesmovement(xPos, 140, self.canvas))
            self.boreeses.append(boreesesmovement(xPos, 185, self.canvas))
            self.boreeses.append(boreesesmovement(xPos, 230, self.canvas))

    def Aliensgettinghit(self, aliens, bullets):
        for alien in aliens:
            for bullet in bullets:
               if alien.x < bullet.x+10 \
               and alien.x+10 > bullet.x \
               and alien.y+10 > bullet.y \
               and alien.y < bullet.y+10:
                   aliens.remove(alien)
                   bullets.remove(bullet)

    def bulletcollisions(self, alienbullets, fighterbullets):
        for alienbullet in alienbullets:
            for fighterbullet in fighterbullets:
                if fighterbullet.x < alienbullet.x+8 \
                and fighterbullet.y+8 > alienbullet.y \
                and fighterbullet.y < alienbullet.y+8 \
                and fighterbullet.x+8 > alienbullet.x:
                    fighterbullets.remove(fighterbullet)
                    alienbullets.remove(alienbullet)
                    print('bulletcollision')
                    self.explosions.append(Explosion(alienbullet.x, alienbullet.y))
                    
    def AliensHittingback(self, alienbullets, fighter):
        for alienbullet in alienbullets:
            if alienbullet.x+22 > fighter.x and alienbullet.y+10 > fighter.y \
            and alienbullet.x < fighter.x+22 and alienbullet.y < fighter.y+10:
                alienbullets.remove(alienbullet)
                self.lifesystem()

class Explosion:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.image5 = PhotoImage(file = 'explosion.gif').subsample(5, 5)
        self.drawcooldown = 1000
    
    def drawingtheexplosion (self, canvas):
        if self.drawcooldown <= 0:
            return True
            
        canvas.create_image(self.x, self.y, image = self.image5, anchor = NW)
        self.drawcooldown -=50
        

class fighter:
    def __init__ (self, x, y):
        self.x = x
        self.y = y
        self.xdirection = 0
        self.bulyeets = []
        self.image1 = PhotoImage(file='fighter.gif').subsample(4,4)
        self.cooldown = 0

    def bounceback(self):
        if self.x < 0:
            self.xdirection *=-1
        elif self.x > 475:
            self.xdirection *=-1

    def aPressed(self, event):
        self.xdirection = -1

    def dPressed(self, event):
        self.xdirection = 1

    def SpacePressed(self, event):
        if self.cooldown <= 0:
            self.bulyeets.append(bullit(self.x, self.y))
            self.cooldown = 10
        
    def draw(self, canvas):
        self.cooldown -= 40
        canvas.create_image(self.x, self.y, image = self.image1, anchor = CENTER)
        self.x += self.xdirection*1
        self.bounceback()
        for bullet in self.bulyeets:
            bullet.draw(canvas)
        
class borret:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image4 = PhotoImage(file='Borret.gif').subsample(18,18)

    def draw(self, canvas):
        self.y +=4.5
        canvas.create_image(self.x, self.y, anchor = NW, image = self.image4)
        
class bullit:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.image3 = PhotoImage(file='actualbullet.gif').subsample(25,18)
        
    def draw(self, canvas):
        fighterbulletspeed = 3.5
        self.y -= fighterbulletspeed
        canvas.create_image(self.x, self.y, anchor = NW, image = self.image3)

class boreesesmovement:
    def __init__ (self, x, y, canvas):
        self.image2 = PhotoImage(file='Boreese.gif').subsample(15,15)
        self.originx = x
        self.originy = y
        self.x = x
        self.y = y
        self.xdirection = 0.1
        self.ydirection = 0
 

    def draw(self, canvas) :
        self.xmoved = self.x - self.originx
        self.ymoved = self.y - self.originy
        justMovedDown = False

        
        #gets to end of right move and goes down
        if self.xmoved > 200 and self.ymoved < 40:
            self.xdirection = 0
            self.ydirection = 0.4
            

        #gets to end of down move and goes left
        elif self.xmoved > 200 and self.ymoved > 40:
            self.xdirection = -0.1
            self.ydirection = 0
            self.originx = self.x
            self.originy = self.y
            justMovedDown = True

        #gets to end of left move and goes down
        elif self.xmoved < -200 and self.ymoved == 0:
            self.xdirection = 0
            self.ydirection = 0.4
            
        
        #gets to end of down move and goes right
        elif self.xmoved < -200 and self.ymoved > 40:
            self.xdirection = 0.1
            self.ydirection = 0
            self.originx = self.x
            self.originy = self.y
            justMovedDown = True
            
        self.x +=self.xdirection*5
        self.y +=self.ydirection*5
        
        canvas.create_image(self.x, self.y, image = self.image2, anchor=NW)
        return justMovedDown
        
mainWindow = Tk()

mainWindow.geometry("500x700+450+150")

game = space(mainWindow)

while True:
    mainWindow.update()
    game.update()
