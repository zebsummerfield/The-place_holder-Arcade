from tkinter import *
import time


#set up the GUI
master = Tk()
master.title("Naughts and Crosses")
master.geometry("300x500+100+100")
master.configure(bg = 'dark grey')
master.option_add('*Button.Font', 'verdana 50 ')
master.option_add('*Button.bg', 'light grey')
master.option_add('*Button.fg', 'black')
master.option_add('*Button.relief', 'ridge')
turn = 1
grid = [['','',''],['','',''],['','','']]
pve = False
cross_played = True



def nothing():
    return


#resets the button commands, text and the global variables
def reset():
    global turn
    global grid
    global pve
    global cross_played
    text_window.configure(text = "")
    position1.configure(text = "", command = lambda: click(1,0,0,position1))
    position2.configure(text = "", command = lambda: click(2,0,1,position2))
    position3.configure(text = "", command = lambda: click(3,0,2,position3))
    position4.configure(text = "", command = lambda: click(4,1,0,position4))
    position5.configure(text = "", command = lambda: click(5,1,1,position5))
    position6.configure(text = "", command = lambda: click(6,1,2,position6))
    position7.configure(text = "", command = lambda: click(7,2,0,position7))
    position8.configure(text = "", command = lambda: click(8,2,1,position8))
    position9.configure(text = "", command = lambda: click(9,2,2,position9))
    turn = 0
    grid = [['','',''],['','',''],['','','']]
    cross_played = True
    #plays first move by placing X in top right if pve is enabled
    if pve:
        turn += 1
        grid[0][2] = 'X'
        position3.configure(text = 'X')
        position3.configure(command = nothing)


#checks for each row,collumn and diagonal to see if any contain 3 of the same character
#if any contain reset is called and the wining message is set
def check_end(character):
    if character == 'X':
        winner = "Crosses"
    else:
        winner = "Naughts"
        
    for i in range(0,3):
        if (character == grid[i][0] and character == grid[i][1] and
            character == grid[i][2]):
            text_window.configure(text = winner + " Wins!")
            master.update()
            time.sleep(1)
            reset()
        if (character == grid[0][i] and character == grid[1][i] and
            character == grid[2][i]):
            text_window.configure(text = winner + " Wins!")
            master.update()
            time.sleep(1)
            reset()
            
    if (character == grid[0][0] and character == grid[1][1] and
        character == grid[2][2]):
        text_window.configure(text = winner + " Wins!")
        master.update()
        time.sleep(1)
        reset()
    if (character == grid[2][0] and character == grid[1][1] and
        character == grid[0][2]):
        text_window.configure(text = winner + " Wins!")
        master.update()
        time.sleep(1)
        reset()
    
    for i in range(0,3):
        for k in range(0,3):
            if grid[i][k] == '':
                return
    text_window.configure(text = "Draw")
    master.update()
    time.sleep(1)
    reset()


#if a button is clicked change the button text to the character corresponding to the turn
def click(num,y,x,position):
    global turn
    global grid
    global pve
    if turn % 2 == 0:
        character = 'O'
    else:
        character = 'X'
    position.configure(text = character)
    position.configure(command = nothing)
    grid[y][x] = character

    check_end(character)
    turn += 1

    #if pve is enabled call the AI's turn
    if pve:
        AI(num,x,y,position)


#plays the AI's move
def AI(num,x,y,position):
    global turn
    global grid
    global cross_played
    #on turn 3 if bottom left is taken play middle else play bottom left
    if turn == 3:
        if not num == 7:
            position7.configure(text = 'X')
            position7.configure(command = nothing)
            grid[2][0] = 'X'
        else:
            position5.configure(text = 'X')
            position5.configure(command = nothing)
            grid[1][1] = 'X'

    #on turns after 3 plays according to the smart_move algorithm
    if turn >= 5:
        cross_played = False
        #checks to see if a win can be made if not then checks to see if an opponent win needs to be stopped
        smart_move('X')
        check_end('X')
        smart_move('O')
        check_end('O')

    #if no move has been made by the AI yet it plays in the first available row
    if not cross_played:
        for i in range(0,3):
            for k in range(0,3):
                if grid[i][k] == '':
                    grid[i][k] = 'X'
                    num = (i + 1)*3 + (k - 2)
                    exec('position' + str(num) + '.configure(text = "X")')
                    exec('position' + str(num) + '.configure(command = nothing)')
                    cross_played = True
                    check_end('X')
                    turn += 1
                    return
                    
    turn += 1


#checks to see if any row,, collumn or diagonal contains 2 of the target character and a blank
#if so the AI plays in the blank    
def smart_move(character):
    global grid
    global turn
    global cross_played
    grid_placeholder = grid

    #row check 
    for i in range(0,3):
        plays = 0
        for k in range(0,3):
            if grid_placeholder[i][k] == character:
                plays += 1
        if plays == 2:
            for index,m in enumerate(grid_placeholder[i]):
                if m == '':
                    grid[i][index] = 'X'
                    num = (i + 1)*3 + ( index - 2)
                    exec('position' + str(num) + '.configure(text = "X")')
                    exec('position' + str(num) + '.configure(command = nothing)')
                    cross_played = True
                    return

    #collumn check                
    for i in range(0,3):
        plays = 0
        for k in range(0,3):
            if grid_placeholder[k][i] == character:
                plays += 1
        if plays == 2:
            for index,m in enumerate(grid_placeholder):
                if m[i] == '':
                    grid[index][i] = 'X'
                    num = (index + 1)*3 + (i - 2)
                    exec('position' + str(num) + '.configure(text = "X")')
                    exec('position' + str(num) + '.configure(command = nothing)')
                    cross_played = True
                    return

    major = [grid[0][0], grid[1][1], grid[2][2]]
    minor = [grid[2][0], grid[1][1], grid[0][2]]

    #major diagonal check
    plays = 0
    for i in major:
        if i == character:
            plays += 1
    if plays == 2:
        if grid[0][0] == '':
            grid[0][0] = 'X'
            position1.configure(text = "X")
            position1.configure(command = nothing)
            cross_played = True
            return
        if grid[1][1] == '':
            grid[1][1] = 'X'
            position5.configure(text = "X")
            position5.configure(command = nothing)
            cross_played = True
            return
        if grid[2][2] == '':
            grid[2][2] = 'X'
            position9.configure(text = "X")
            position9.configure(command = nothing)
            cross_played = True
            return

    #minor diagonal check
    plays = 0
    for i in minor:
        if i == character:
            plays += 1
    if plays == 2:
        if grid[2][0] == '':
            grid[2][0] = 'X'
            position7.configure(text = "X")
            position7.configure(command = nothing)
            cross_played = True
            return
        if grid[1][1] == '':
            grid[1][1] = 'X'
            position5.configure(text = "X")
            position5.configure(command = nothing)
            cross_played = True
            return
        if grid[0][2] == '':
            grid[0][2] = 'X'
            position3.configure(text = "X")
            position3.configure(command = nothing)
            cross_played = True
            return


#enables pve
def loner():
    global turn
    global pve
    pve = True
    reset()
    turn += 1

#enable pvp
def competitive():
    global turn
    global pve
    pve = False
    reset()
    turn += 1

        

#creates the buttons and text box and places them in the GUI
position1 = Button(master, command = lambda: click(1,0,0,position1))
position1.place(x=20, y = 100, width = 80, height = 80)
position2 = Button(master, command = lambda: click(2,0,1,position2))
position2.place(x=110, y = 100, width = 80, height = 80)
position3 = Button(master, command = lambda: click(3,0,2,position3))
position3.place(x=200, y = 100, width = 80, height = 80)
position4 = Button(master, command = lambda: click(4,1,0,position4))
position4.place(x=20, y = 190, width = 80, height = 80)
position5 = Button(master, command = lambda: click(5,1,1,position5))
position5.place(x=110, y = 190, width = 80, height = 80)
position6 = Button(master, command = lambda: click(6,1,2,position6))
position6.place(x=200, y = 190, width = 80, height = 80)
position7 = Button(master, command = lambda: click(7,2,0,position7))
position7.place(x=20, y = 280, width = 80, height = 80)
position8 = Button(master, command = lambda: click(8,2,1,position8))
position8.place(x=110, y = 280, width = 80, height = 80)
position9 = Button(master, command = lambda: click(9,2,2,position9))
position9.place(x=200, y = 280, width = 80, height = 80)

PvP = Button(master, text = "PvP", font = ('verdana', 25),
             command = competitive)
PvP.place(x = 60, y = 380, width = 80, height = 50)
PvE = Button(master, text = "PvE", font = ('verdana', 25),
             command = loner)
PvE.place(x = 160, y = 380, width = 80, height = 50)

text_window = Label(font = ('verdana', 15), bg = 'light grey',
                    relief = 'sunken')
text_window.place(x = 50, y = 25, width = 200, height = 50)



#only plays when launched from this window
def main():  
    master.mainloop()

if __name__ == '__main__':
    main()


    
