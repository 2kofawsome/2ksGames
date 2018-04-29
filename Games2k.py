from tkinter import *
import tkinter as tk
import random, time, os
from tkinter.font import Font
from PIL import ImageTk, Image

print("LOADING...")
print("Please wait...")

#################################################################################################### TicTacToe2.0 start

#Sam Gunter
#TicTacToe2.14 was finished 5:50pm on the 18th of March, 2018.
#This was created to play TicTacToe either 2 player or against varying degrees of AI. The easy AI should be easy (duh) to win against and the hard should be impossible to beat.
#Unlike TicTacToe1.0 this has a GUI to make the experience better. The hard AI is much better and now not only gets lines and blocks lines, but sets up plays where it is a guaranteed win.
#I created this in functions and procedures instead of linear to allow both single player and multiplayer to use the same blocks of code. This is also so multiple games can be added together in one document.

#Next step is to add a leaderboard document (will have to learn how to do file manipulation).

#TicTacToe: Global variables and functions normally have a "Tic" at the end incase another game uses similar variables later on.
#First function is gamemode, then if single player was chosen difficulty, then a function to set difficulty.
#No matter if single or multiplayer the next function creates the tkinter window and then one of the turns happen either turnTic or one of the AI, ends with endTic. User can go back to menu or click again and the person starting alternates.
#It is always set up so the next function is last in the current function (using if and else statements).

def TicTacToe():
   for widget in master.winfo_children():
      widget.destroy()
   global gamesTic
   global levelTic #most of these variables only have to be called up in 1 or 2 functions
   global gridWinTic
   global gridTic
   global playerTic
   global sizeTic
   global screenWidth
   global screenHeight
   if screenWidth<screenHeight:
      sizeTic=((screenWidth-60)//3)
   else:
      sizeTic=((screenHeight-60)//3)
   gamesTic=0 #if playing against ai this sets who plays first (alternates)
   levelTic=0 #default, if it stays as 0 multiplayer will run, if singleplayer is chosen this will change to 1 (random ai) or 2 (ai that knows how to win)
   gridTic=[' ', ' ', ' ', #this is the TicTacToe grid, only has 3 lines to make it easier to look at
        ' ', ' ', ' ',
        ' ', ' ', ' ']
   gridWinTic=[0, 0, 0, #0 means there have been no wins, will change to 1 when a winning line made
        0, 0, 0,
        0, 0, 0]
   playerTic="X" #default start is X, this will not matter if singleplayer is chosen
   master.configure(bg = "#000000") #Sets initial background colour to black
   Label(master, bg = "#000000", fg="#fff", text="TicTacToe2.0").grid(row = 0, column = 1) #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: menu()).grid(row = 0, column = 0, sticky = "we") #right now ends the program, later will redirect
   tk.Button(master, text = "Multiplayer", height = 5, width = 20, bg = "#fff", command = lambda: reloadTic()).grid(row = 1, column = 0) #command=lambda stops the programs from running when the window is first created
   tk.Button(master, text = "Singleplayer", height = 5, width = 20, bg = "#fff", command = lambda: singleplayerTic()).grid(row = 1, column = 1) #when clicked redirects to whichever function is command

def howToPlayTic(): #just tutorial on how to play
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "#000000", fg = "#fff", text="TicTacToe2.0").grid(row = 0, column = 1)
   tk.Button(master, text = "Play", height = 1, width = 10, bg = "#fff", command = lambda: TicTacToe()).grid(row = 0, column = 0, sticky = "we") #play instead of menu

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/3)) #a third of the screen, leaves room for top bar
   frameMine1.grid(row=1, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2)) #half the screen
   frameMine2.grid(row=2, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   
   Label(frameMine1, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//35) + " bold", text=""" 
Program specific instructions

1. Click on an empty tile to place an X or an O.
2. If playing multiplayer, alternate with the other player.
3. If playing single player, the AI will automatically play instantly.""").pack(expand=True, fill="both") #game specfic instructions (buttons)

   Label(frameMine2, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//35), text="""Rules to Game:

The game is played on a grid that's 3 squares by 3 squares.
Players take turns putting their marks in empty squares.
The first player to get 3 marks in a row (up, down, across, or diagonally) is the winner.
If all 9 squares are full, the game is over.
If no player has 3 marks in a row, the game ends in a tie.""").pack(expand=True, fill="both") #how to play, taken from some website probably


def againTic(): #if the user wants to play again
   global gridWinTic
   global levelTic
   global gridTic
   global playerTic
   global gamesTic
   gamesTic+=1
   gridTic=[' ', ' ', ' ', #resets board
        ' ', ' ', ' ',
        ' ', ' ', ' ']
   gridWinTic=[0, 0, 0, #clears winning line
        0, 0, 0,
        0, 0, 0]
   if levelTic==0: #if multiplayer, just switch who is playing first and go again (loser plays first next time)
      if playerTic == "X":
         playerTic="O"
         reloadTic()
      else:
         playerTic="X"
         reloadTic()
   else:
      if gamesTic % 2 == 0:
         reloadTic() #player goes first
      else: #ai goes first
         if levelTic == 1: #tiggers easy ai
            aiTic(1)
         elif levelTic == 2: #triggers medium ai
            aiTic(2)
         elif levelTic == 3: #triggers hard ai
            aiTic(3)
         
def singleplayerTic():
   for widget in master.winfo_children():
      widget.destroy()
   Label(master, bg = "#000000", fg="#fff", text="TicTacToe2.0").grid(row = 0, column = 1)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: TicTacToe()).grid(row = 0, column = 0, sticky = "we") #sends back to first TicTacToe screen 
   tk.Button(master, text = "Easy", height = 5, width = 20, bg = "#fff", command = lambda: setTic("easy")).grid(row = 1, column = 0) #random ai
   tk.Button(master, text = "Medium", height = 5, width = 20, bg = "#fff", command = lambda: setTic("medium")).grid(row = 1, column = 1) #ai that knows how to win, user goes first
   tk.Button(master, text = "Hard", height = 5, width = 20, bg = "#fff", command = lambda: setTic("hard")).grid(row = 1, column = 2) #same ai as above, user goes second

def setTic(difficulty): #difficulty changes depending on whether medium or hard was clicked
   global levelTic
   if difficulty=="easy": #easy ai
      levelTic=1
      reloadTic()
   elif difficulty=="medium": #medium ai
      levelTic=2
      reloadTic()
   else: #the only other possibility is hard
      levelTic=3
      reloadTic()

def reloadTic():
   global playerTic
   global sizeTic
   global frameTic
   for widget in master.winfo_children():
      widget.destroy()
   Label(master, bg = "#000000", fg="#fff", text="TicTacToe2.0").grid(row = 0, column = 1)
   Label(master, bg = "#000000", fg="#fff", text=playerTic + "'s turn").grid(row = 4, column = 1) #to keep it constant has a blank label at the bottom with no words, this is where winner is displayed or where it tells you you can't play there
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: TicTacToe()).grid(row = 0, column = 0, sticky = "we") #menu goes right back to start
   tk.Button(master, text = "How To Play", height = 1, width = 10, bg = "#fff", command = lambda: howToPlayTic()).grid(row = 0, column = 2, sticky = "we") #menu goes right back to start
   frameTic=[]
   myFont=Font(family="Helvetica", size=((sizeTic//7)*4))
   for r in range(0, 3):
      for c in range(0,3): #r is the number of rows, c is the column number
         frameTic.append(tk.Frame(master, width = sizeTic, height = sizeTic))
         frameTic[r*3+c].grid(row=r+1, column=c, sticky="nsew")
         frameTic[r*3+c].propagate(False)
         if r*3+c == 0:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(0)).pack(expand=True, fill="both") #drops it down a bit so the bold does not make the square bigger than the other (57 instead of 60)
         elif r*3+c == 1:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(1)).pack(expand=True, fill="both")
         elif r*3+c == 2:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(2)).pack(expand=True, fill="both")
         elif r*3+c == 3:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(3)).pack(expand=True, fill="both")
         elif r*3+c == 4:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(4)).pack(expand=True, fill="both")
         elif r*3+c == 5:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(5)).pack(expand=True, fill="both")
         elif r*3+c == 6:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(6)).pack(expand=True, fill="both")
         elif r*3+c == 7:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(7)).pack(expand=True, fill="both")
         elif r*3+c == 8:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(8)).pack(expand=True, fill="both")
   if gridTic[0]!=" " and gridTic[1]!=" " and gridTic[2]!=" " and gridTic[3]!=" " and gridTic[4]!=" " and gridTic[5]!=" " and gridTic[6]!=" " and gridTic[7]!=" " and gridTic[8]!=" ": #This means everything is filled up
      endTic("tie") #putting "tie" tells the function it was a tie for the bottom label

def endTic(result):
   global gridWinTic
   global playerTic
   global sizeTic
   global frameTic
   myFont=Font(family="Helvetica", size=((sizeTic//7)*4))
   winFont=Font(family="Helvetica", size=((sizeTic//5)*3), weight='bold') #different fonts for win or game in progress
   for widget in master.winfo_children():
      widget.destroy()
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: TicTacToe()).grid(row = 0, column = 0, sticky = "we")
   tk.Button(master, text = "Again", height = 1, width = 10, bg = "#fff", command = lambda: againTic()).grid(row = 0, column = 2, sticky = "we")
   Label(master, bg = "#000000", fg="#fff", text="TicTacToe2.0").grid(row = 0, column = 1)
   if result=="tie": #if it is a tie display this
      Label(master, bg = "#000000", fg="#fff", text="It is a tie.").grid(row = 4, column = 1)
   elif result=="multi": #if multiplayer, the playerTic was the last one who played therefore the winner
      Label(master, bg = "#000000", fg="#fff", text=playerTic+" wins!").grid(row = 4, column = 1)
   elif result=="player": #in player vs ai, player wins
      Label(master, bg = "#000000", fg="#fff", text="You win!").grid(row = 4, column = 1)
   elif result=="ai": #in player vs ai, ai wins
      Label(master, bg = "#000000", fg="#fff", text="You lose.").grid(row = 4, column = 1)
   frameTic=[]
   for r in range(0, 3): #THIS WHOLE THING IS ONLY TO MAKE THE CODE SHORTER, WAS AROUND 50 LINES FOR THIS BEFORE WITH IF, ELIF, ELSE STATEMENTS
      for c in range(0,3): #r is the number of rows, c is the column number
         frameTic.append(tk.Frame(master, width = sizeTic, height = sizeTic))
         frameTic[r*3+c].grid(row=r+1, column=c, sticky="nsew", padx = 0, pady = 0)
         frameTic[r*3+c].propagate(False)
         if gridWinTic[r*3+c]==1: #the row number minus 1 multiplied by 3 added by the column gets the spot on the grid, the 1 was set by an earlier function if there was a winner, if the line contained these characters then they will be bold for player to see
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=winFont,  bg = "#fff").pack(expand=True, fill="both") #drops it down a bit so the bold does not make the square bigger than the other (57 instead of 60)
         else:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont, bg = "#fff").pack(expand=True, fill="both") #normal text
      #once this is done it will sit and wait for user to click menu and restart

def turnTic(number): #number is whichever button was clicked
   global playerTic
   global gridWinTic
   global levelTic
   if gridTic[number] == " ": #if it is valid (if no one has played there yet)
      gridTic[number] = playerTic #grid gets replaced with the player, if going against ai it will always be X, if multiplayer it starts as X but switched later in this function
      for counter in range(0,3): #this is just to make less code, happens 3 times (0,1,2, ends when at 3)
         if gridTic[0+counter*3] == gridTic[1+counter*3] == gridTic[2+counter*3] == playerTic: #left to right wins
            gridWinTic[0+counter*3]=gridWinTic[1+counter*3]=gridWinTic[2+counter*3]=1 #sets these to 1 (they started as 0) so that they will be bold at the end, and so program knows a winner was declared
         if gridTic[0+counter] == gridTic[3+counter] == gridTic[6+counter] == playerTic: #up and down wins
            gridWinTic[0+counter]=gridWinTic[3+counter]=gridWinTic[6+counter]=1
      if gridTic[0] == gridTic[4] == gridTic[8] == playerTic: #cross and the next is cross other way
         gridWinTic[0]=gridWinTic[4]=gridWinTic[8]=1
      if gridTic[2] == gridTic[4] == gridTic[6] == playerTic:#Using only if statements here because it is possible for more than one to make a row at the same time, elif would cancel out the rest after the first is found
         gridWinTic[2]=gridWinTic[4]=gridWinTic[6]=1
      if gridWinTic[0] == gridWinTic[4] == gridWinTic[8] == 0: #Every possible winning combo has one of these numbers in it, for that reason only those 3 need to be checked
         if levelTic == 1: #tiggers easy ai
            aiTic(1)
         elif levelTic == 2: #triggers hard ai
            aiTic(2)
         elif levelTic == 3: #triggers hard ai
            aiTic(3)
         elif playerTic == "X": #switches from x to o, remakes window, and goes again
            playerTic="O"
            reloadTic()
         else: #switches from o to x, remakes window, and goes again
            playerTic="X"
            reloadTic()
      else: #if there was a winner (not all the earlier 3 were 0s)
         if levelTic==0: #multiplayer
            endTic("multi") #see endtic for explanation
         else: #against ai, player won
            endTic("player")
   else: #if it wasn't valid, the bottom label gets used and the user goes again      
      Label(master, bg = "#000000", fg="#fff", text="You cannot play there.").grid(row = 4, column = 1)

def aiTic(difficulty):
   global gridTic
   global GridWinTic
   number=-1 #number will be 0-8 by the end, so must start as something else
   if gridTic[0]!=" " and gridTic[1]!=" " and gridTic[2]!=" " and gridTic[3]!=" " and gridTic[4]!=" " and gridTic[5]!=" " and gridTic[6]!=" " and gridTic[7]!=" " and gridTic[8]!=" ":
      endTic("tie") #checks to see if a tie, sends to endTic function if so
   else:
      if difficulty>1: #medium or hard
         if gridTic[4]==' ': #always play middle if possible. Since it will be a maximum of 2 turns until this is filled up (this bot will play here in its first move) there is no reason to check for 2 in a rows first
            number=4 #sets number as middle one
      if number==-1: #if the middle wasn't open and no 2 in the rows, the number is still -1. Now go to second priority
         if difficulty>1: #medium or hard
            counter=0
            while counter < 3:
               if gridTic[0+counter*3] == gridTic[1+counter*3] == "O" and gridTic[2+counter*3] == " ": #similar to the checking for a winner, but checking for 2 in a row that can make a winner. This is top priority
                  number=2+counter*3
               elif gridTic[0+counter*3] == gridTic[2+counter*3] == "O" and gridTic[1+counter*3] == " ":
                  number=1+counter*3
               elif gridTic[2+counter*3] == gridTic[1+counter*3] == "O" and gridTic[0+counter*3] == " ":
                  number=0+counter*3
               elif gridTic[0+counter] == gridTic[3+counter] == "O" and gridTic[6+counter] == " ":
                  number=6+counter
               elif gridTic[0+counter] == gridTic[6+counter] == "O" and gridTic[3+counter] == " ":
                  number=3+counter
               elif gridTic[6+counter] == gridTic[3+counter] == "O" and gridTic[0+counter] == " ":
                  number=0+counter
               counter+=1
            if gridTic[0] == gridTic[4] == "O" and gridTic[8] == " ":
               number=8
            elif gridTic[0] == gridTic[8] == "O" and gridTic[4] == " ":
               number=4
            elif gridTic[8] == gridTic[4] == "O" and gridTic[0] == " ":
               number=0
            elif gridTic[2] == gridTic[4] == "O" and gridTic[6] == " ":
               number=6
            elif gridTic[2] == gridTic[6] == "O" and gridTic[4] == " ":
               number=4
            elif gridTic[6] == gridTic[4] == "O" and gridTic[2] == " ":
               number=2
         if number==-1: #if the middle wasn't open and no 2 in the rows, the number is still -1. Now go to second priority
            if difficulty>1: #medium or hard
               counter=0
               while counter < 3: 
                  if gridTic[0+counter*3] == gridTic[1+counter*3] == "X" and gridTic[2+counter*3] == " ": #good offence is a good defence so winning would be ideal, but now checking to see if there are any 2 in a rows of the player to block
                     number=2+counter*3
                  elif gridTic[0+counter*3] == gridTic[2+counter*3] == "X" and gridTic[1+counter*3] == " ":
                     number=1+counter*3
                  elif gridTic[2+counter*3] == gridTic[1+counter*3] == "X" and gridTic[0+counter*3] == " ":
                     number=0+counter*3
                  elif gridTic[0+counter] == gridTic[3+counter] == "X" and gridTic[6+counter] == " ":
                     number=6+counter
                  elif gridTic[0+counter] == gridTic[6+counter] == "X" and gridTic[3+counter] == " ":
                     number=3+counter
                  elif gridTic[6+counter] == gridTic[3+counter] == "X" and gridTic[0+counter] == " ":
                     number=0+counter
                  counter+=1
               if gridTic[0] == gridTic[4] == "X" and gridTic[8] == " ":
                  number=8
               elif gridTic[0] == gridTic[8] == "X" and gridTic[4] == " ":
                  number=4
               elif gridTic[8] == gridTic[4] == "X" and gridTic[0] == " ":
                  number=0
               elif gridTic[2] == gridTic[4] == "X" and gridTic[6] == " ":
                  number=6
               elif gridTic[2] == gridTic[6] == "X" and gridTic[4] == " ":
                  number=4
               elif gridTic[6] == gridTic[4] == "X" and gridTic[2] == " ":
                  number=2
            if number==-1: #I don't count this as a priority, because it is a very specific scenario which can go anywhere in the code, just decided to put after the 2 ina  rows
               if difficulty==3:
                  if gridTic[4] == "O" and gridTic[0] == gridTic[8] == "X" and gridTic[1] == gridTic[2] == gridTic[3] == gridTic[5] == gridTic[6] == gridTic[7] == " ":
                     number=1
                  elif gridTic[4] == "O" and gridTic[2] == gridTic[6] == "X" and gridTic[1] == gridTic[0] == gridTic[3] == gridTic[5] == gridTic[8] == gridTic[7] == " ":
                     number=1
               if number==-1: #I don't count this as a priority, because it is a very specific scenario which can go anywhere in the code, just decided to put after the 2 ina  rows
                  if difficulty==3:
                     if gridTic[1] == gridTic[3] == "X" and gridTic[0] == gridTic[2] == gridTic[6] == " ":
                        number=0
                     elif gridTic[5] == gridTic[1] == "X" and gridTic[2] == gridTic[0] == gridTic[8] == " ":
                        number=2
                     elif gridTic[5] == gridTic[7] == "X" and gridTic[8] == gridTic[2] == gridTic[6] == " ":
                        number=8
                     elif gridTic[7] == gridTic[3] == "X" and gridTic[6] == gridTic[8] == gridTic[0] == " ":
                        number=6
                  if number==-1: #there is nowhere to block, so now goes to third priority
                     if difficulty==3: #hard
                        if gridTic[4] == gridTic[0] == "O" and gridTic[1] == " " == gridTic[2] == gridTic[7]: #if 2 out of 3 of a cross are filled but player blocked third. This checks for the adjacent spots empty, so user has to block 2 lines (not possible)
                           number=1
                        elif gridTic[4] == gridTic[0] == "O" and gridTic[3] == " " == gridTic[6] == gridTic[5]:
                           number=3
                        elif gridTic[4] == gridTic[8] == "O" and gridTic[5] == " " == gridTic[2] == gridTic[3]:
                           number=5
                        elif gridTic[4] == gridTic[8] == "O" and gridTic[7] == " " == gridTic[1] == gridTic[6]:
                           number=7
                        elif gridTic[4] == gridTic[2] == "O" and gridTic[1] == " " == gridTic[0] == gridTic[7]:
                           number=1
                        elif gridTic[4] == gridTic[2] == "O" and gridTic[5] == " " == gridTic[3] == gridTic[8]:
                           number=5
                        elif gridTic[4] == gridTic[6] == "O" and gridTic[7] == " " == gridTic[1] == gridTic[8]:
                           number=7
                        elif gridTic[4] == gridTic[6] == "O" and gridTic[3] == " " == gridTic[0] == gridTic[5]:
                           number=3
                     if number==-1:
                        if difficulty==3: #hard
                           if gridTic[4] == "O" and gridTic[0] == "X" and gridTic[8] == " ": #if possible and ai has middle, go in opposite corner to set up what was just checked for above
                              number=8
                           elif gridTic[4] == "O" and gridTic[8] == "X" and gridTic[0] == " ":
                              number=0
                           elif gridTic[4] == "O" and gridTic[2] == "X" and gridTic[6] == " ":
                              number=6
                           elif gridTic[4] == "O" and gridTic[6] == "X" and gridTic[2] == " ":
                              number=2
                        if number==-1: #last thing to check
                           if difficulty==3:
                              if gridTic[0] == gridTic[8] == " " == gridTic[1] == gridTic[3]: #checks for open opposite corners and adjacent open. this is used to make opportunities when ai has the middle, or to block opportunities when ai does not have the middle
                                 number=0
                              elif gridTic[2] == gridTic[6] == " " == gridTic[1] == gridTic[5]:
                                 number=2
                              elif gridTic[6] == gridTic[2] == " " == gridTic[3] == gridTic[7]:
                                 number=6
                              elif gridTic[8] == gridTic[0] == " " == gridTic[7] == gridTic[5]:
                                 number=8
                           if number==-1: #easy medium or hard
                              while True: #Last chance random, this will rarely happen for medium, almost never for hard and always for easy
                                 number=random.randint(0,8) #random number on grid (0-8)
                                 if gridTic[number] == " ": #if no one has played in this random spot move on (break), else do it again
                                    break
      gridTic[number] = "O" #sets whichever number was chosen to O
      for counter in range(0,3):
         if gridTic[0+counter*3] == gridTic[1+counter*3] == gridTic[2+counter*3] == "O":
            gridWinTic[0+counter*3]=gridWinTic[1+counter*3]=gridWinTic[2+counter*3]=1
         elif gridTic[0+counter] == gridTic[3+counter] == gridTic[6+counter] == "O":
            gridWinTic[0+counter]=gridWinTic[3+counter]=gridWinTic[6+counter]=1
      if gridTic[0] == gridTic[4] == gridTic[8] == "O":
         gridWinTic[0]=gridWinTic[4]=gridWinTic[8]=1
      if gridTic[2] == gridTic[4] == gridTic[6] == "O":
         gridWinTic[2]=gridWinTic[4]=gridWinTic[6]=1
      if gridWinTic[0] == gridWinTic[4] == gridWinTic[8] == 0: #if no winner, goes to player again
         reloadTic()
      else:
         endTic("ai") #if the ai won, endTic function

#################################################################################################### TicTacToe2.0 end

#################################################################################################### MineSweeper start

#Sam Gunter
#MineSweeper was finished 2:05am on the 31st of March, 2018.
#This was created to copy the microsoft minesweeper game that we know and love.
#I have tried my best to make it as efficient as possible with my (I admit) limited knowledge of programming, but on some computers it does have severe lag.

#Next step is to add a leaderboard document.

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then choice of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper().
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first click will never be a bomb. Allows user to chose to play again.


def MineSweeper(errorCheck):
   master.bind("<Button-3>", flagMine)
   master.bind("<Button-2>", chordMine)
   global varSizeMine #this becomes a non var variable later (var is from tkinter)
   global varBombMine
   for widget in master.winfo_children():
      widget.destroy()
   master.configure(bg = "darkgrey") #Sets initial background colour to dark grey
   Label(master, bg = "darkgrey", text="MineSweeper").grid(row = 0, column = 1) #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: unbind()).grid(row = 0, column = 0, sticky = "we") #sticky we causes it to fill all availible space
   varSizeMine=IntVar() #declaired the var variables
   varBombMine=IntVar()
   tk.Scale(master, bg="#fff", from_=8, to=24, orient=HORIZONTAL, variable=varSizeMine, label="The size of your grid (X by X)").grid(row = 3, columnspan = 3, sticky="we") #this is a scale (slider) for custom games, sticky makes it fill full column span
   tk.Scale(master, bg="#fff", from_=8, to=99, orient=HORIZONTAL, variable=varBombMine, label="The number of bombs").grid(row = 5, columnspan = 3, sticky="we") #horizontal is side to side, from/to is range
   tk.Button(master, text = "Custom Game: (The sliders)", height = 5, width = 20, bg = "darkgrey", command = lambda: gameSetMine(0)).grid(row = 8, columnspan = 3, sticky="we") #command=lambda stops the programs from running when the window is first created
   tk.Button(master, text = "How To Play", height = 1, width = 10, bg = "#fff", command = lambda: howToPlayMine()).grid(row = 0, column = 2, sticky="we")
   tk.Button(master, text = "Easy", height = 5, width = 20, bg = "darkgrey", command = lambda: gameSetMine(1)).grid(row = 1, column = 0)
   tk.Button(master, text = "Medium", height = 5, width = 20, bg = "darkgrey", command = lambda: gameSetMine(2)).grid(row = 1, column = 1)
   tk.Button(master, text = "Hard", height = 5, width = 20, bg = "darkgrey", command = lambda: gameSetMine(3)).grid(row = 1, column = 2)
   if errorCheck=="True":
      Label(master, bg = "darkgrey", fg = "darkred", text="You have too many bombs").grid(row = 9, columnspan = 3, sticky="we")

def howToPlayMine(): #see TicTacToe how to play, all others will have no comments
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "darkgrey", text="MineSweeper").grid(row = 0, column = 1)
   tk.Button(master, text = "Play", height = 1, width = 10, bg = "#fff", command = lambda: MineSweeper(" ")).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frameMine1.grid(row=1, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=2, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   
   Label(frameMine1, bg = "white smoke", font = "Helvetica " + str(pixelMine//35) + " bold", text="""Program specific instructions

1. Left Click: Click on Tile
2. Right Click: Place flag
3. Middle Click: Chord""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "white smoke", font = "Helvetica " + str(pixelMine//40), text="""Rules to Game:

In order to win the game, you must reveal all the squares that DO NOT contain a mine,
whether you flag them or not is a matter of personal preference.
If a mine is revealed, you lose.
When you click a tile, you get a number.
That number is the number of how many mines that are surrounding it.
If you find the mine, you can open the tiles around it, gainning more numbers.
for example if you have a tile saying "1", and only 1 tile touching it.
You know that the one tile is a bomb, if another tile says "1" and
is touching that bomb and 2 other tiles,
you know the 2 other tiles are safe to click.""").pack(expand=True, fill="both")


def gameSetMine(level):
   global sizeMine
   global bombMine
   if level==0: #custom board
         sizeMine=varSizeMine.get() #as I said above, sets var variable to int
         bombMine=varBombMine.get()
         if bombMine >= sizeMine*sizeMine:
            MineSweeper("True")
         else:
            createBoardMine()
   else:
      if level==1: #easy
            sizeMine=8 #these numbers are the official minesweeper numbers
            bombMine=10
      elif level==2: #medium
            sizeMine=16
            bombMine=40
      elif level==3: #hard
            sizeMine=24
            bombMine=99
      createBoardMine() #triggers next function

def createBoardMine():
   global shownMine #Similar to TicTacToe(), most of these are barely called again, but have to all be declared here as global
   global frameMine
   global reliefMine
   global hiddenMine
   global myFont
   global pixelMine
   global statusMine
   global bombsLeftMine
   global buttonMine
   global flagImgMine
   global bombImgMine
   bombsLeftMine=bombMine #keep track of flag counter in top corner
   statusMine="start"
   for widget in master.winfo_children(): #same as TicTacToe2.0 this delete all widgets onscreen
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth//(sizeMine+1))
   else:
      pixelMine=(screenHeight//(sizeMine+1))
   flagImgMine = ImageTk.PhotoImage(Image.open("gameFiles/flagMine.png").resize((pixelMine, pixelMine), resample=0))
   bombImgMine = ImageTk.PhotoImage(Image.open("gameFiles/bombMine.png").resize((pixelMine, pixelMine), resample=0))
   
   hiddenMine=[[]] #this will be the minesweeper board fully filled up and user can not see it
   shownMine=[[]] #what the user gets shown
   reliefMine=[[]] #same as both lists of lists above, but is to set the buttons as raised so they can be changed to appear pushed down later on when they are clicked
   buttonMine=[[]]
   for r in range(sizeMine): #for the rows, which is the variable
      if len(hiddenMine)==r: #if if maxed out make a new list
         hiddenMine.append([])
         shownMine.append([])
         reliefMine.append([])
         buttonMine.append([])
      for c in range(sizeMine): #for columns which si the same variable (square)
         hiddenMine[r].append(" ") #adds an empty space, this is solely to make the list of lists
         shownMine[r].append("") #adds nothing this time instead of  a space so later on the program can see the difference between shown and hidden values
         reliefMine[r].append("raised")

   myFont=Font(family="Helvetica", size=pixelMine//2) #font seems to work if it is half the size of the block, needs more testing on different monitors
   Label(master, bg = "darkgrey", font=("Helvetica", pixelMine//5), text="MineSweeper").grid(row = 0, columnspan = sizeMine) #column span makes it take up more lines
   tk.Button(master, text = "Menu", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: MineSweeper(" ")).grid(row = 0, column = 0, columnspan=3, sticky = "we")
   button1=tk.Button(master, text = str(bombsLeftMine)+" bombs left", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff").grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we") #this button is named because it has to be edited later on
   frameMine=[] #sets the frames, this is needed to specify the amount of pixels each box should be
   for r in range(sizeMine):
      for c in range(sizeMine):
         frameMine.append(tk.Frame(master, width = pixelMine, height = pixelMine)) #makes frame with the pixel by pixel value
         frameMine[r*sizeMine+c].grid(row=r+1, column=c, sticky="nsew") #makes it so button inside takes up whole frame
         frameMine[r*sizeMine+c].propagate(False) #makes it so frame doesn't get smaller
         buttonMine[r].append(tk.Button(frameMine[r*sizeMine+c], text = shownMine[r][c], font=myFont, activebackground = "grey", bg = "lightgrey", command = lambda forCommand=[r, c]: clickMine(forCommand[0], forCommand[1])))
         buttonMine[r][c].pack(expand=True, fill="both") #adds the button into the frame, these act as each square in minesweeper with a predefined textsize, background, etc

def flagMine(event): #This might be one of the most complicated codes I have created, so many numbers together all of which are variables and most of which are pixels related to screen
   if statusMine!="end": #makes it so this code doesn't run if bomb has been triggered
      global bombsLeftMine
      global shownMine #flagImgMine
      global buttonMine
      for r in range(sizeMine):
         for c in range(sizeMine):
            if frameMine[r*sizeMine+c].winfo_y() < master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_y()+pixelMine > master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_x() < master.winfo_pointerx() and frameMine[r*sizeMine+c].winfo_x()+pixelMine > master.winfo_pointerx() and reliefMine[r][c]=="raised": #long thing to see if the cursor is within frame window and if it is still raised (not checked yet)
               if shownMine[r][c] == "?": #if already a flag
                  bombsLeftMine+=1 #adds 1 bomb (because 1 less flag)
                  shownMine[r][c]="" #turns off flag
                  buttonMine[r][c].config(image="", text = shownMine[r][c], command = lambda forCommand=[r, c]: clickMine(forCommand[0], forCommand[1])) #creates button as normal
               else:
                  bombsLeftMine-=1 #takes a away 1 bomb from counter
                  shownMine[r][c]="?" #makes a flag
                  buttonMine[r][c].config(image=flagImgMine, command = 0, disabledforeground = "#000000") #button that has no command, just to display question mark until clicked again
      if bombsLeftMine>=0: #if not negative it will display bombs left
         button1=tk.Button(master, text = str(bombsLeftMine)+" bombs left", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff").grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we")
      else: #if negative it says too many flags
         button1=tk.Button(master, text = "Too many flags", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff").grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we")

def chordMine(event):
   if statusMine!="end":
      global sizeMine
      global pixelMine
      for r in range(sizeMine):
         for c in range(sizeMine):
            if frameMine[r*sizeMine+c].winfo_y() < master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_y()+pixelMine > master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_x() < master.winfo_pointerx() and frameMine[r*sizeMine+c].winfo_x()+pixelMine > master.winfo_pointerx() and reliefMine[r][c]=="sunken":
               chording=0 #this variable checks to see if all flags around the number have been declared
               if r-1>=0 and c-1>=0 and shownMine[r-1][c-1] == "?": #if it exists and is a ?
                  chording+=1 #add 1 to chord
               if c-1>=0 and shownMine[r][c-1] == "?":
                  chording+=1
               if r+1<sizeMine and c-1>=0 and shownMine[r+1][c-1] == "?":
                  chording+=1          
               if r-1>=0 and shownMine[r-1][c] == "?":
                  chording+=1            
               if r+1<sizeMine and shownMine[r+1][c] == "?":
                  chording+=1
               if r-1>=0 and c+1<sizeMine and shownMine[r-1][c+1] == "?":
                  chording+=1           
               if c+1<sizeMine and shownMine[r][c+1] == "?":
                  chording+=1           
               if r+1<sizeMine and c+1<sizeMine and shownMine[r+1][c+1] == "?":
                  chording+=1
               if chording == hiddenMine[r][c]: #if there are the same amount of flags as the number
                  if r-1>=0 and c-1>=0 and shownMine[r-1][c-1] == "": #clicks on every open spot around it
                     checkMine(r-1, c-1)
                  if c-1>=0 and shownMine[r][c-1] == "":
                     checkMine(r, c-1)            
                  if r+1<sizeMine and c-1>=0 and shownMine[r+1][c-1] == "":
                     checkMine(r+1, c-1)            
                  if r-1>=0 and shownMine[r-1][c] == "":
                     checkMine(r-1, c)            
                  if r+1<sizeMine and shownMine[r+1][c] == "":
                     checkMine(r+1, c)
                  if r-1>=0 and c+1<sizeMine and shownMine[r-1][c+1] == "":
                     checkMine(r-1, c+1)            
                  if c+1<sizeMine and shownMine[r][c+1] == "":
                     checkMine(r, c+1)            
                  if r+1<sizeMine and c+1<sizeMine and shownMine[r+1][c+1] == "":
                     checkMine(r+1, c+1)

def updateMine(row, column): #this updates only 1 square, before it was updating all of them but that make a slight lag (less than a second) which was not good
   global buttonMine
   if shownMine[row][column] == " " or shownMine[row][column] == 1:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", activeforeground = "navy", bg = "lightgrey", fg = "blue", relief = "sunken") #active colours so they dont turn white and black when clicked
   elif shownMine[row][column] == 2:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", activeforeground = "dark green", bg = "lightgrey", fg = "green4", relief = "sunken")
   elif shownMine[row][column] == 3:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", activeforeground = "red4", bg = "lightgrey", fg = "red", relief = "sunken")
   elif shownMine[row][column] == 4:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", activeforeground = "midnight blue", bg = "lightgrey", fg = "navy", relief = "sunken")
   elif shownMine[row][column] == 5:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", activeforeground = "brown4", bg = "lightgrey", fg = "crimson", relief = "sunken")
   elif shownMine[row][column] == 6:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", activeforeground = "dark slate grey", bg = "lightgrey", fg = "darkcyan", relief = "sunken")
   elif shownMine[row][column] == 7:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", bg = "lightgrey", fg = "black", relief = "sunken")
   elif shownMine[row][column] == 8:
      buttonMine[row][column].config(text = shownMine[row][column], activebackground = "grey", bg = "lightgrey", fg = "silver", relief = "sunken")
      
   win="True" #starts as the person assumed won
   for r in range(sizeMine):
      for c in range(sizeMine):
         if reliefMine[r][c] == "raised" and hiddenMine[r][c] != "!": #if a block is raised (therefore not clicked) and it is not a bomb
            win="False" #makes them not win yet
   if win == "True": #if that wasn’t triggered
      endMine("win") #triggers end game won

def endMine(result): #end game
   button1=tk.Button(master, text = "Again", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: createBoardMine()).grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we") #allows user to play again with the same specifications (board size and amount of bombs)
   global statusMine
   global buttonMine
   statusMine="end"
   for r in range(sizeMine):
      for c in range(sizeMine):
         if hiddenMine[r][c] == "!" and result == "lose": #if lose
            buttonMine[r][c].config(image=bombImgMine, bg = "indianred")  #make bombs show as red
         elif hiddenMine[r][c] == "!" and result == "win": #if win
            buttonMine[r][c].config(image=flagImgMine, text = "?") #make bombs show as defused

def clickMine(row, column): #This is used 1 time to make sure the user doesn't get out 1st time
   global statusMine
   global sizeMine
   global hiddenMine
   if statusMine == "start": #if this function has not been triggered yet
      for b in range(bombMine): #to adds bombs to hidden list
         while True:
            rowLocation=random.randint(0, sizeMine-1) #random row in range
            columnLocation=random.randint(0, sizeMine-1) #random column in range
            if hiddenMine[rowLocation][columnLocation] == " " and (rowLocation != row or columnLocation != column): #if nothing is there and it isn't the match of either row or column to where the user clicked
               hiddenMine[rowLocation][columnLocation]="!" #sets bomb, otherwise the while loop makes new random row and column
               break
      for r in range(sizeMine):
         for c in range(sizeMine):
            if  hiddenMine[r][c] == " ":
               touching=0 #sets how many it is touching to 0
               if r-1>=0 and c-1>=0 and hiddenMine[r-1][c-1] == "!": #checks for north west
                  touching+=1 #adds 1 to its value
               if c-1>=0 and hiddenMine[r][c-1] == "!": #checks for north
                  touching+=1
               if r+1<sizeMine and c-1>=0 and hiddenMine[r+1][c-1] == "!": #checks for north east
                  touching+=1
               if r-1>=0 and hiddenMine[r-1][c] == "!": #checks for west
                  touching+=1
               if r+1<sizeMine and hiddenMine[r+1][c] == "!": #checks for east
                  touching+=1
               if r-1>=0 and c+1<sizeMine and hiddenMine[r-1][c+1] == "!": #checks for south west
                  touching+=1
               if c+1<sizeMine and hiddenMine[r][c+1] == "!": #checks for south
                  touching+=1
               if r+1<sizeMine and c+1<sizeMine and hiddenMine[r+1][c+1] == "!": #checks for south east
                  touching+=1
               if touching==0:
                  hiddenMine[r][c]=" " #if it is 0 (because we don't want to display 0s)
               else:
                  hiddenMine[r][c]=touching #if above 0, sets it as that number
      statusMine = " " #switches this to nothing
      checkMine(row, column) #triggers the actually function to play minesweeper
   elif statusMine != "end":
      checkMine(row, column) #after the first time just goes through this function instantly everytime

def checkMine(row, column): #when a button is clicked
   if hiddenMine[row][column]=="!": #if a bomb
      endMine("lose") #triggers lose
      for widget in frameMine[row*sizeMine+column].winfo_children():
         widget.destroy()
      tk.Button(frameMine[row*sizeMine+column], image=bombImgMine, font=myFont, bg = "darkred").pack(expand=True, fill="both") #dark red to make them know it was the bomb that killed them
      
   elif hiddenMine[row][column]==" ": #if not touching any bomb
      shownMine[row][column]=hiddenMine[row][column] #switches shown to hidden, I need this because shown is " " and hidden is "", so this makes the code run faster as it does not go over the same blocks multiple times
      reliefMine[row][column]="sunken" #switches to sunken not raised
      if row-1>=0 and column-1>=0 and shownMine[row-1][column-1] == "": #each one of these checks one of the blocks around to see 1. If it exists, 2. If it was not done yet
         checkMine(row-1, column-1) #triggers this same function with the new square
      if column-1>=0 and shownMine[row][column-1] == "":
         checkMine(row, column-1)            
      if row+1<sizeMine and column-1>=0 and shownMine[row+1][column-1] == "":
         checkMine(row+1, column-1)            
      if row-1>=0 and shownMine[row-1][column] == "":
         checkMine(row-1, column)            
      if row+1<sizeMine and shownMine[row+1][column] == "":
         checkMine(row+1, column)
      if row-1>=0 and column+1<sizeMine and shownMine[row-1][column+1] == "":
         checkMine(row-1, column+1)            
      if column+1<sizeMine and shownMine[row][column+1] == "":
         checkMine(row, column+1)            
      if row+1<sizeMine and column+1<sizeMine and shownMine[row+1][column+1] == "":
         checkMine(row+1, column+1)
      updateMine(row, column) #then updates
   else: #if a number
      shownMine[row][column]=hiddenMine[row][column] #simply displays the number
      reliefMine[row][column]="sunken"
      updateMine(row, column) #then updates

#################################################################################################### MineSweeper end

#################################################################################################### 2048 start

#Sam Gunter
#2048 was finished 2:18pm on the 6th of April, 2018.
#This was created to play 2048. The hardest and longest part was making the program appear fluid, not a sudden movement where the entire screen refreshes,
#but making it refresh one by one as the label moves. If the entire screen reloaded it would be too slow, so I had to completely change how I made frames on tkinter.

#Next step is to add a leaderboard document.

#2048: Global variables and functions normally have a 2048 at the end, main one is called the2048 because had to have letters.
#Creates board with 2 numbers inside it. Then user can click arrow or swipe mouse/finger across screen.
#All numbers move in that direction and combine if possible. Constantly checking for game end.

def the2048():
   global pixel2048
   global value2048
   global frame2048
   global label2048
   global win2048
   global delay2048
   delay2048=time.time()
   win2048="schrodinger"
   master.bind("<Up>", up2048) #binds the up, down, left, right arrows on keyboard
   master.bind("<Down>", down2048)
   master.bind("<Left>", left2048)
   master.bind("<Right>", right2048)
   master.bind("<Button-1>", buttonclick2048) #so arrows arent needed, allows swiping (finger down...
   master.bind("<ButtonRelease-1>", buttonrelease2048) #... finger up
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixel2048=(screenWidth//5)
   else:
      pixel2048=(screenHeight//5)
   Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//6), text="2048").grid(row = 0, column=1, columnspan = 2)
   tk.Button(master, text = "Menu", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: unbind()).grid(row = 0, column = 0, sticky = "we")
   tk.Button(master, text = "How To Play", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: howToPlay2048()).grid(row = 0, column = 3, sticky = "we")

   label2048=[[]]
   frame2048=[[]] #same as all lists above, but for flags
   for r in range(4):
      if len(frame2048)==r:
         frame2048.append([])
         label2048.append([])
      for c in range(4):
         frame2048[r].append(tk.Frame(master, bd = 2, width = pixel2048, height = pixel2048))
         frame2048[r][c].grid(row=r+1, column=c, sticky="nsew") 
         frame2048[r][c].propagate(False)
         label2048[r].append("")

   value2048=[[" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "], [" ", " ", " ", " "]] #creates empty grid

   row = random.randint(0, 3) #row for the first 2
   column = random.randint(0, 3) #column for first 2
   value2048[row][column] = 2 #places 2
   while True:
      row = random.randint(0, 3) #same as above
      column = random.randint(0, 3)
      if value2048[row][column] == " ": #checks to make sure 2 isn't already there
         value2048[row][column] = 4 #places the 4
         break

   for r in range(4):
      for c in range(4):
         if value2048[r][c] == " ":
            label2048[r][c] = tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "grey") #only need " ", 2 and 4 for this first one
         elif value2048[r][c] == 2:
            label2048[r][c] = tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "white")
         elif value2048[r][c] == 4:
            label2048[r][c] = tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "lemonchiffon")
         label2048[r][c].pack(expand=True, fill="both")
   reloadFull2048()

def howToPlay2048():
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "#000000", fg = "#fff", text="2048").grid(row = 0, column = 1)
   tk.Button(master, text = "Play", height = 1, width = 10, bg = "#fff", command = lambda: the2048()).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frameMine1.grid(row=1, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=2, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)
   
   Label(frameMine1, bg = "grey", font = "Helvetica " + str(pixelMine//35) + " bold", text="""


Program specific instructions

1.Use the arrow keys to go up, down, left or right.
2.You can also use your finger (or mouse)
to drag across the screen to shift the board.""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "grey", font = "Helvetica " + str(pixelMine//35), text="""Rules to Game:

When two tiles with the same number touch they merge into one,
that means 2s become a 4, 4s a 8, 8s a 16 and so on.
You are attempting to try to get a block of 2048 (2^11),
which makes you win the game!""").pack(expand=True, fill="both")

def reloadFull2048():
   global win2048
   global label2048
   win2048="False" #game set as over
   for r in range(4):
      for c in range(4):
         if value2048[r][c] == " ":
            win2048="schrodinger" #if any of these things are met, game continues (see schrodingers cat thought experiment)
         if r>0: #need layers here because an error code would happen for out of range
            if value2048[r][c] == value2048[r-1][c]:
               win2048="schrodinger"
         if r<3:
            if value2048[r][c] == value2048[r+1][c]:
               win2048="schrodinger"
         if c>0:
            if value2048[r][c] == value2048[r][c-1]:
               win2048="schrodinger"
         if c<3:
            if value2048[r][c] == value2048[r][c+1]:
               win2048="schrodinger"
               
         if value2048[r][c] == 2048:
            win2048="True"
         if value2048[r][c] == " ":
            label2048[r][c].config(text = value2048[r][c], bg = "grey", font=("Helvetica", pixel2048//2)) #changes colour, text and size
         elif value2048[r][c] == 2:
            label2048[r][c].config(text = value2048[r][c], bg = "white", font=("Helvetica", pixel2048//2))
         elif value2048[r][c] == 4:
            label2048[r][c].config(text = value2048[r][c], bg = "lemonchiffon", font=("Helvetica", pixel2048//2))
         elif value2048[r][c] == 8:
            label2048[r][c].config(text = value2048[r][c], bg = "sandybrown", font=("Helvetica", pixel2048//2))
         elif value2048[r][c] == 16:
            label2048[r][c].config(text = value2048[r][c], bg = "chocolate", font=("Helvetica", pixel2048//2))
         elif value2048[r][c] == 32:
            label2048[r][c].config(text = value2048[r][c], bg = "salmon", font=("Helvetica", pixel2048//2))
         elif value2048[r][c] == 64:
            label2048[r][c].config(text = value2048[r][c], bg = "tomato", font=("Helvetica", pixel2048//2))
         elif value2048[r][c] == 128:
            label2048[r][c].config(text = value2048[r][c], bg = "khaki", font=("Helvetica", pixel2048//3))
         elif value2048[r][c] == 256:
            label2048[r][c].config(text = value2048[r][c], bg = "yellow", font=("Helvetica", pixel2048//3))
         elif value2048[r][c] == 512:
            label2048[r][c].config(text = value2048[r][c], bg = "gold", font=("Helvetica", pixel2048//3))
         elif value2048[r][c] == 1024:
            label2048[r][c].config(text = value2048[r][c], bg = "orange", font=("Helvetica", pixel2048//4))
         elif value2048[r][c] == 2048:
            label2048[r][c].config(text = value2048[r][c], bg = "goldenrod", font=("Helvetica", pixel2048//4))
   if win2048 == "True":
      Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="You Win!").grid(row = 5, columnspan = 4, sticky = "we")
      tk.Button(master, text = "Play Again", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: the2048()).grid(row = 0, column = 3, sticky = "we")
   elif win2048 == "False":
      Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="You Lose").grid(row = 5, columnspan = 4, sticky = "we")
      tk.Button(master, text = "Play Again", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: the2048()).grid(row = 0, column = 3, sticky = "we")

   
def reload2048(r, c): #reloads one at a time, this gives the game its cascading effect
   if value2048[r][c] == " ":
      label2048[r][c].config(text = value2048[r][c], bg = "grey", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 2:
      label2048[r][c].config(text = value2048[r][c], bg = "white", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 4:
      label2048[r][c].config(text = value2048[r][c], bg = "lemonchiffon", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 8:
      label2048[r][c].config(text = value2048[r][c], bg = "sandybrown", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 16:
      label2048[r][c].config(text = value2048[r][c], bg = "chocolate", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 32:
      label2048[r][c].config(text = value2048[r][c], bg = "salmon", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 64:
      label2048[r][c].config(text = value2048[r][c], bg = "tomato", font=("Helvetica", pixel2048//2))
   elif value2048[r][c] == 128:
      label2048[r][c].config(text = value2048[r][c], bg = "khaki", font=("Helvetica", pixel2048//3))
   elif value2048[r][c] == 256:
      label2048[r][c].config(text = value2048[r][c], bg = "yellow", font=("Helvetica", pixel2048//3))
   elif value2048[r][c] == 512:
      label2048[r][c].config(text = value2048[r][c], bg = "gold", font=("Helvetica", pixel2048//3))
   elif value2048[r][c] == 1024:
      label2048[r][c].config(text = value2048[r][c], bg = "orange", font=("Helvetica", pixel2048//4))
   elif value2048[r][c] == 2048:
      label2048[r][c].config(text = value2048[r][c], bg = "goldenrod", font=("Helvetica", pixel2048//4))

def buttonclick2048(event): #checks x and y value with first click
   global x2048
   global y2048
   x2048=master.winfo_pointerx() #x value
   y2048=master.winfo_pointery() #y value

def buttonrelease2048(event): #when button is released (the mouse was slide in this time)
   xslide2048=master.winfo_pointerx() - x2048 #checks difference in start and end
   yslide2048=master.winfo_pointery() - y2048
   if xslide2048 > pixel2048: #if x bigger than one block (to the right)
      if yslide2048 < pixel2048 and yslide2048 > -1 * pixel2048: #checks if opposite (y in this case) was moved less than a block
         right2048(" ") 
   if xslide2048 < -1 * pixel2048: #if x smaller than negative one block (to the left)
      if yslide2048 < pixel2048 and yslide2048 > -1 * pixel2048:
         left2048(" ") 
   if yslide2048 > pixel2048: #if y bigger than one block (down)
      if xslide2048 < pixel2048 and xslide2048 > -1 * pixel2048:
         down2048(" ")
   if yslide2048 < -1 * pixel2048: #if y smaller than negative one block (up)
      if xslide2048 < pixel2048 and xslide2048 > -1 * pixel2048:
         up2048(" ")

def up2048(event):
   global delay2048
   if (time.time()-delay2048) > .05:
      if win2048 == "schrodinger": #neither true nor false
         together=[[]]
         for r in range(4): #makes it so only 1 thing happens on each line
            if len(together)==r:
               together.append([])
            for c in range(4):
               together[r].append(False)
         moved=False #checks to see if any move happened
         for r in range(3): #one less because dont need to check the highest row
            for adjustment in range(3): #adjustment makes it go to end, and not just up once
               for c in range(4):
                  if value2048[r+1-adjustment][c] != " " and (r+1-adjustment)>=0: #if the tile is not empty, saves code time
                     if value2048[r-adjustment][c] == " " and (r-adjustment)>=0: #if the one above is empty
                        value2048[r-adjustment][c] = value2048[r+1-adjustment][c] #replace with one under
                        value2048[r+1-adjustment][c] = " " #delete one under
                        moved=True #it moved at least once
                     else: #if a number above
                        if value2048[r-adjustment][c] == value2048[r+1-adjustment][c] and (r-adjustment)>=0 and together[r-adjustment][c] == False: #if the number below and above are the same
                           value2048[r-adjustment][c] = (value2048[r-adjustment][c])*2 #multiply above
                           value2048[r+1-adjustment][c] = " " #and delete bottom
                           together[r-adjustment][c] = True
                           together[r-adjustment-1][c] = True
                           moved=True #it moved at least once
                     reload2048(r+1-adjustment, c)
                     reload2048(r-adjustment, c)
                     master.update_idletasks()
                     time.sleep(.005)
         if moved == True: #if something moved, create a new number
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="").grid(row = 5, columnspan = 4, sticky = "we")
            column = random.randint(0, 3) #random column
            for c in range(4): #makes it so it will check all fast and not just random
               if value2048[3][(column+c)%4] == " ": #if empty. % is modular so remainder
                  value2048[3][(column+c)%4] = 2 #put in a 2
                  break #then break, else do again with 1 higher
         else: #else, display a message saying no
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="Can't go that way").grid(row = 5, columnspan = 4, sticky = "we")
         reloadFull2048()
   delay2048 = time.time()

def down2048(event):
   global delay2048
   if (time.time()-delay2048) > .05:
      if win2048 == "schrodinger":
         together=[[]]
         for r in range(4):
            if len(together)==r:
               together.append([])
            for c in range(4):
               together[r].append(False)
         moved=False
         for r in range(3):
            for adjustment in range(3):
               for c in range(4):
                  if value2048[(-r-1)-1+adjustment][c] != " " and (-r-1)-1+adjustment<0: #row is reversed
                     if value2048[(-r-1)+adjustment][c] == " " and ((-r-1)+adjustment)<0: #plus adjustment not minus
                        value2048[(-r-1)+adjustment][c] = value2048[(-r-1)-1+adjustment][c] #minus 1, not plus 1
                        value2048[(-r-1)-1+adjustment][c] = " "
                        moved=True
                     else:
                        if value2048[(-r-1)+adjustment][c] == value2048[(-r-1)-1+adjustment][c] and ((-r-1)+adjustment)<0 and together[(-r-1)+adjustment][c] == False:
                           value2048[(-r-1)+adjustment][c] = (value2048[(-r-1)+adjustment][c])*2
                           value2048[(-r-1)-1+adjustment][c] = " "
                           moved=True
                           together[(-r-1)+adjustment][c] = True
                           together[(-r-1)+adjustment+1][c] = True
                     reload2048((-r-1)-1+adjustment, c)
                     reload2048((-r-1)+adjustment, c)
                     master.update_idletasks()
                     time.sleep(.005)
         if moved == True:
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="").grid(row = 5, columnspan = 4, sticky = "we")
            column = random.randint(0, 3)
            for c in range(4):
               if value2048[0][(column+c)%4] == " ": #0 not 3
                  value2048[0][(column+c)%4] = 2
                  break
         else:
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="Can't go that way").grid(row = 5, columnspan = 4, sticky = "we")

         reloadFull2048()
   delay2048 = time.time()

def left2048(event): #this is the same code as up2048, but r and c is switched throughout it
   global delay2048
   if (time.time()-delay2048) > .05:
      if win2048 == "schrodinger":
         together=[[]]
         for r in range(4): #makes it so only 1 thing happens on each line
            if len(together)==r:
               together.append([])
            for c in range(4):
               together[r].append(False)
         moved=False
         for c in range(3):
            for adjustment in range(3):
               for r in range(4):
                  if value2048[r][c+1-adjustment] != " " and (c+1-adjustment)>=0:
                     if value2048[r][c-adjustment] == " " and (c-adjustment)>=0:
                        value2048[r][c-adjustment] = value2048[r][c+1-adjustment]
                        value2048[r][c+1-adjustment] = " "
                        moved=True
                     else:
                        if value2048[r][c-adjustment] == value2048[r][c+1-adjustment] and (c-adjustment)>=0 and together[r][c-adjustment] == False:
                           value2048[r][c-adjustment] = (value2048[r][c-adjustment])*2
                           value2048[r][c+1-adjustment] = " "
                           moved=True
                           together[r][c-adjustment] = True
                           together[r][c-adjustment-1] = True
                     reload2048(r, c+1-adjustment)
                     reload2048(r, c-adjustment)
                     master.update_idletasks()
                     time.sleep(.005)
         if moved == True:
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="").grid(row = 5, columnspan = 4, sticky = "we")
            row = random.randint(0, 3)
            for r in range(4):
               if value2048[(row+r)%4][3] == " ":
                  value2048[(row+r)%4][3] = 2
                  break 
         else:
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="Can't go that way").grid(row = 5, columnspan = 4, sticky = "we")

         reloadFull2048()
   delay2048 = time.time()
      
def right2048(event): #this is the same code as down,2048 but r and c are switched throughout it
   global delay2048
   if (time.time()-delay2048) > .05:
      if win2048 == "schrodinger":
         together=[[]]
         for r in range(4): #makes it so only 1 thing happens on each line
            if len(together)==r:
               together.append([])
            for c in range(4):
               together[r].append(False)
         moved=False
         for c in range(3):
            for adjustment in range(3):
               for r in range(4):
                  if value2048[r][(-c-1)-1+adjustment] != " " and ((-c-1)-1+adjustment)<0:
                     if value2048[r][(-c-1)+adjustment] == " " and ((-c-1)+adjustment)<0:
                        value2048[r][(-c-1)+adjustment] = value2048[r][(-c-1)-1+adjustment]
                        value2048[r][(-c-1)-1+adjustment] = " "
                        moved=True
                     else:
                        if value2048[r][(-c-1)+adjustment] == value2048[r][(-c-1)-1+adjustment] and ((-c-1)+adjustment)<0 and together[r][(-c-1)+adjustment] == False:
                           value2048[r][(-c-1)+adjustment] = (value2048[r][(-c-1)+adjustment])*2
                           value2048[r][(-c-1)-1+adjustment] = " "
                           moved=True
                           together[r][(-c-1)+adjustment]= True
                           together[r][(-c-1)+adjustment+1]= True 
                     reload2048(r, (-c-1)-1+adjustment)
                     reload2048(r, (-c-1)+adjustment)
                     master.update_idletasks()
                     time.sleep(.005)
         if moved == True:
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="").grid(row = 5, columnspan = 4, sticky = "we")
            row = random.randint(0, 3)
            for r in range(4):
               if value2048[(row+r)%4][0] == " ":
                  value2048[(row+r)%4][0] = 2
                  break
         else:
            Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="Can't go that way").grid(row = 5, columnspan = 4, sticky = "we")
         reloadFull2048()
   delay2048 = time.time()
      
#################################################################################################### 2048 end

#################################################################################################### Sudoku start

#Sam Gunter
#Sudoku was finished 1:03am on the 14th of April, 2018.
#This was created to allow the user to play sudoku on the computer.
#I have tried my best to add a random generator to make the games less static, but it came down to the tried and true method of "f--- it, it is good enough".

#Next steps is to make a leaderboard document.

#Sudoku: Global variables and functions normally have a "Su" at the end incase another game uses similar variables later on (or earlier on).
#First function is Sudoku(). Then chocie of easy, medium or hard. Then triggers a board to be generated from one of the preset fully complete and semi-random tiles chosen to show.
#Next it loads the board, then when users click and type in numbers it saves, always checking for errors or to end the game. At the end you can play again.

def Sudoku():
   for widget in master.winfo_children():
      widget.destroy()
   Label(master, bg = "#000000", fg="#fff", text="Sudoku").grid(row = 0, column = 1)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: menu()).grid(row = 0, column = 0, sticky = "we")
   tk.Button(master, text = "Easy", height = 5, width = 20, bg = "#fff", command = lambda: generateSu(20)).grid(row = 1, column = 0) #different difficulties are solely how many clues at the beginning
   tk.Button(master, text = "Medium", height = 5, width = 20, bg = "#fff", command = lambda: generateSu(15)).grid(row = 1, column = 1) #I wanted to improve this, but alas I could not
   tk.Button(master, text = "Hard", height = 5, width = 20, bg = "#fff", command = lambda: generateSu(10)).grid(row = 1, column = 2)

def solvedBoardSu(number):

   hiddenSu = open(".\gameFiles\SudokuBoards.txt").readlines()
   hiddenSu = hiddenSu[number] #takes that line specfied
   hiddenSu=hiddenSu.split('|') #splits at | each 9

   for n in range(9):
      hiddenSu[n]=hiddenSu[n].split(" ") #then each one at " "

   for r in range(9):
      for c in range(9):
         hiddenSu[r][c]=int(hiddenSu[r][c]) #turns str to in
   return hiddenSu #returns the board

def generateSu(difficulty):
   global shownSu
   global staticSu
   global hiddenSu

   fileSu = open(".\gameFiles\SudokuBoards.txt").readlines() #from a txt file, to add more to file and see more its wroking see "CreateBoardsSudoku.py"
   
   hiddenSu = solvedBoardSu(random.randint(0, (len(fileSu)-2))) #choses board from random number within the amount of boards

   patternSu=[[False, False, False, False, False, False, False, False, False], #sets pattern as non shown
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False],
              [False, False, False, False, False, False, False, False, False]]

   for n in range(9):
      for m in range(3): #3 times for each of the 9 numbers to assure mostly solvable boards
         r=random.randint(0,8) #random row
         c=random.randint(0,8) #random column
         while True: #loops next process until it works
            if hiddenSu[r][c] == (n+1) and patternSu[r][c] == False: #if not yet chosen and it is the number
               patternSu[r][c] = True # make it appear
               break #move on to next one
            r+=1 #no need for else because of break, adds one to row
            if r == 9: #if past row, row = 0 and column + 1
               r = r - 9
               c+=1
               if c == 9: #if column past, column = 0 and back at start
                  c = c - 9
                  
   for n in range(3): #checks for eahc box
      for m in range(3):
         amount=0 #the amount of numbers shown
         for x in range(3): #checks each tile in box
            for y in range(3):
               if patternSu[n*3+x][m*3+y] == True: #if shown
                  amount+=1
         while amount < 3: #at least 3 must be shown
            while True: #or another will be put in to assure solvability
               r=random.randint(0, 2)
               c=random.randint(0, 2)
               if patternSu[n*3+r][m*3+c] == False:
                  patternSu[n*3+r][m*3+c] = True
                  amount+=1 #adjusts amount and checks again
                  difficulty = difficulty - 1 #1 less random one later
                  break

   for n in range(difficulty): #depending on difficulty adds a number of hints to help user
      while True:
         r=random.randint(0,8)
         c=random.randint(0,8)
         if patternSu[r][c] == False: #this time can be any number, so only checks for if shown yet
            patternSu[r][c] = True
            break
   staticSu=[[]] #determines labels vs buttons
   shownSu=[[]] #creates what to show
   for r in range(9):
      if len(shownSu)==r:
         shownSu.append([])
         staticSu.append([])
      for c in range(9):
         if patternSu[r][c] == True:
            shownSu[r].append(hiddenSu[r][c]) #adds number
            staticSu[r].append(hiddenSu[r][c]) #adds number
         else:
            shownSu[r].append(" ") #hidden one
            staticSu[r].append(" ")

   loadBoardSu() #triggers next fucntion

def howToPlaySu():
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "#000000", fg = "#fff", text="Sudoku").grid(row = 0, column = 1)
   tk.Button(master, text = "Play", height = 1, width = 10, bg = "#fff", command = lambda: loadBoardSu()).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frameMine1.grid(row=1, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=2, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   
   Label(frameMine1, bg = "white smoke", font = "Helvetica " + str(pixelMine//35) + " bold", text="""


Program specific instructions

1. Click on a space you want to edit,
then us your keyboard to type a number.
2. To save the number either click enter or click on another tile.
3. Leave a tile empty to delete.
4. Red squares mean that there are numbers that conflict.""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "white smoke", font = "Helvetica " + str(pixelMine//35), text="""Rules to Game:

The objective is to fill a 9x9 grid so that each column,
each row, and each of the nine 3x3 boxes (also called
blocks or regions) contains the digits from 1 to 9. """).pack(expand=True, fill="both")

def loadBoardSu():
   global myFont #most variables are only called a few times
   global pixelMine
   global buttonsSu
   global shownSu
   global frameSu
   global rowSu
   global columnSu
   global errorSu
   global mistakeSu
   master.bind("<Return>", enterSu)
   
   for widget in master.winfo_children():
      widget.destroy()
   rowSu=-1 #for clickSu() later on
   columnSu=-1
   if screenWidth<screenHeight: #screen size as normal
      pixelMine=(screenWidth//10)
   else:
      pixelMine=(screenHeight//10)
   myFont=Font(family="Helvetica", size=pixelMine//2)
   boldFont=Font(family="Helvetica", size=pixelMine//2, weight='bold')
   Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixelMine//5), text="Sudoku").grid(row = 0, columnspan = 9)
   tk.Button(master, text = "Menu", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: Sudoku()).grid(row = 0, column = 0, columnspan=3, sticky = "we")
   tk.Button(master, text = "How To Play", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: howToPlaySu()).grid(row = 0, column = 6, columnspan=3, sticky = "we")
   errorSu = tk.Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixelMine//5), text="Use numbers only!")

   mistakeSu=[[]] #if numbers conflict, first made with no conflictions
   frameSu=[[]] #frames for size
   buttonsSu=[[]] #buttons in frames
   for r in range(9):
      if len(buttonsSu)==r:
         mistakeSu.append([])
         buttonsSu.append([])
         frameSu.append([])
      for c in range(9):
         mistakeSu[r].append(False) #all made with no conflictions
         frameSu[r].append(tk.Frame(master, width = pixelMine, height = pixelMine, borderwidth = "1")) #borderwidth of 1 gives it that nice look of slight lines between
         frameSu[r][c].grid(row=r+1, column=c, sticky="nsew") 
         frameSu[r][c].propagate(False)
         if staticSu[r][c]==" " and (r//3 + c//3) % 2 == 0: #floored divison where it causes the blocks of 9 to be different colors
            buttonsSu[r].append(tk.Button(frameSu[r][c], relief = 'flat', font=myFont, bg = "white", borderwidth = "0", text = shownSu[r][c], command = lambda forCommand=[r, c]: clickSu(forCommand[0], forCommand[1]))) #relief flat makes it look flat (duh)
         elif staticSu[r][c]==" " and (r//3 + c//3) % 2 == 1: #If you cant understand from looking at this, I will need to draw it out as cant explain in words
            buttonsSu[r].append(tk.Button(frameSu[r][c], relief= 'flat', font=myFont, bg = "light grey", borderwidth = "0", text = shownSu[r][c], command = lambda forCommand=[r, c]: clickSu(forCommand[0], forCommand[1])))
         elif (r//3 + c//3) % 2 == 0:
            buttonsSu[r].append(tk.Label(frameSu[r][c], text = staticSu[r][c], font=boldFont, bg = "white", )) #if a number is already there, makes a label, not button
         elif (r//3 + c//3) % 2 == 1:
            buttonsSu[r].append(tk.Label(frameSu[r][c], text = staticSu[r][c], font=boldFont, bg = "light grey"))
         buttonsSu[r][c].pack(expand=True, fill="both")

def clickSu(row, column):
   global buttonsSu
   global frameSu
   global shownSu
   global rowSu
   global columnSu
   global entry

   try: #tries to do this, will only work if not first one
      enterSu("event") #runs the same as if user clicks enter, saves last number
   except:
      a=1 #this is soley ot allow the except statement
   
   if rowSu >= 0 and columnSu >=0: #if after first time, gets rid of entry box for last one
      entry.pack_forget()
      buttonsSu[rowSu][columnSu].pack(expand=True, fill="both")
   rowSu=row
   columnSu=column
   buttonsSu[row][column].pack_forget()
   
   if (row//3 + column//3) % 2 == 0 and mistakeSu[row][column]==False: #if no mistake its white
      entry = tk.Entry(frameSu[row][column], bg = "white", font = myFont, justify = "center") #for user to enter number, justfies to center
   elif (row//3 + column//3) % 2 == 1 and mistakeSu[row][column]==False:
      entry = tk.Entry(frameSu[row][column], bg = "light grey", font = myFont, justify = "center")
   elif (row//3 + column//3) % 2 == 0 and mistakeSu[row][column]==True: #if mistake it is red
      entry = tk.Entry(frameSu[row][column], bg = "firebrick1", font = myFont, justify = "center")
   elif (row//3 + column//3) % 2 == 1 and mistakeSu[row][column]==True:
      entry = tk.Entry(frameSu[row][column], bg = "firebrick3", font = myFont, justify = "center")
   entry.pack(expand=True, fill="both")
   entry.focus_set() #sets focus to the netry so user does not have to click

def enterSu(event):
   global shownSu
   global mistakeSu
   try: #tries to save the number and bring up button
      errorSu.grid_forget()
      if int(entry.get()[-1]) == 0: #if a 0
         shownSu[rowSu][columnSu] = " " #delete that, we dont want no 0s
      else:
         shownSu[rowSu][columnSu]=int(entry.get()[-1]) #only the last digit
      entry.pack_forget()
      buttonsSu[rowSu][columnSu].config(text = shownSu[rowSu][columnSu])
      buttonsSu[rowSu][columnSu].pack(expand=True, fill="both")
   except: #if not a number
      if str(entry.get()) == "" or str(entry.get()) == " ": #if space and empty
         shownSu[rowSu][columnSu] = " " #clear tile
         entry.pack_forget()
         buttonsSu[rowSu][columnSu].config(text = shownSu[rowSu][columnSu])
         buttonsSu[rowSu][columnSu].pack(expand=True, fill="both")
      else: #if anything else
         errorSu.grid(row = 10, columnspan = 9) #tell them they broke the game

   for r in range(9):
      for c in range(9):
         mistakeSu[r][c]=False #deletes all mistakes each time and rechecks for errors
         
   for r in range(9):
      for c in range(9): #choses a specfic block
         for n in range(8):
            if shownSu[r-(n+1)][c] == shownSu[r][c] and shownSu[r-(n+1)][c] != " ": #checks for mistake in same row
               for x in range(9): #makes every tile in row an error
                  mistakeSu[r-(x)][c]=True
               break #speeds up by ending before full loop
         for n in range(8):
            if shownSu[r][c-(n+1)] == shownSu[r][c] and shownSu[r][c-(n+1)] != " ": #checks for mistake in same column
               for x in range(9): #makes every tile in column an error
                  mistakeSu[r][c-(x)]=True
               break
         for n in range(3): #3 by 3 block
            for m in range(3):
               if shownSu[(r//3)*3+n][(c//3)*3+m] == shownSu[r][c] and shownSu[r][c] != " " and (r != (r//3)*3+n or c != (c//3)*3+m): #checks for mistake in block
                  for x in range(3):
                     for y in range(3):
                        mistakeSu[(r//3)*3+x][(c//3)*3+y]=True #makes all tiles in block an error
                  break
      
   for r in range(9):
      for c in range(9): #replaces colour of each tile
         if (c//3 + r//3) % 2 == 0 and mistakeSu[r][c]==False:
            buttonsSu[r][c].config(bg='white')
         elif (c//3 + r//3) % 2 == 1 and mistakeSu[r][c]==False:
            buttonsSu[r][c].config(bg='light grey')
         elif (c//3 + r//3) % 2 == 0 and mistakeSu[r][c]==True:
            buttonsSu[r][c].config(bg='firebrick1')
         elif (c//3 + r//3) % 2 == 1 and mistakeSu[r][c]==True:
            buttonsSu[r][c].config(bg='firebrick3')

   gameEnd=True #sets game as over
   for c in range(9):
      for r in range(9):
         if mistakeSu[r][c]==True: #if any mistakes
            gameEnd=False #keeps playing
            break
         elif shownSu[r][c]==" ": #if any blank
            gameEnd=False #keeps playing
            break
   if gameEnd==True: #if neither of those were met
      tk.Button(master, text = "Play Again", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: Sudoku()).grid(row = 0, column = 6, columnspan=3, sticky = "we") #allows the user to play again
      errorSu.config(text="You win!") #changes from preset error message (earlier) to winner message
      errorSu.grid(row = 10, columnspan = 9)

#################################################################################################### Sudoku end

#################################################################################################### Connect4 start

#Sam Gunter
#Connect4 was finished 3:31am on the 28th of April, 2018
#This was created to play Connect 4 either against another player or against AI.
#AI checks for winning plays, blocking plays, but the rest is random. This allows the user to set up plays, but no easy wins.

#Next step is to add leaderboard document.

#Connect: Global variables and functions normally have a "Con" at the end incase another game uses similar variables later on or earlier on.
#Creates a 6 by 7 board which users can click to drop in connect 4 pieces. The game automatically checks for where the user clicks, no buttons, only labels.
#Multiplayer is alternating while looking for any wins or for if the game is full, which ends the game and allows user to restart. Single player alternates between player and AI.
#Singleplayer mode has good AI but not perfect.

def Connect4():
   global oneCon
   oneCon = False #preset as multiplayer
   master.unbind("<ButtonRelease-1>")
   for widget in master.winfo_children():
      widget.destroy()
   Label(master, bg = "#000000", fg="#fff", text="Connect4").grid(row = 0, column = 1)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: menu()).grid(row = 0, column = 0, sticky = "we")
   tk.Button(master, text = "Single Player", height = 5, width = 20, bg = "#fff", command = lambda: singleCon()).grid(row = 1, column = 0)
   tk.Button(master, text = "Multiplayer", height = 5, width = 20, bg = "#fff", command = lambda: boardCon()).grid(row = 1, column = 1)

def howToPlayCon(): #see other how-to-plays
   master.unbind("<ButtonRelease-1>")
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "#000000", fg = "#fff", text="Connect4").grid(row = 0, column = 1)
   tk.Button(master, text = "Play", height = 1, width = 10, bg = "#fff", command = lambda: Connect4()).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frameMine1.grid(row=1, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=2, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)
   
   Label(frameMine1, bg = "#000000", fg = "#fff", font = "Helvetica " + str(pixelMine//35) + " bold", text="""


Program specific instructions

1.Click in any column to add a connect 4 piece.""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "#000000", fg = "#fff", font = "Helvetica " + str(pixelMine//35), text="""Rules to Game:

Players first choose a color and then take turns dropping colored discs,
from the top into a seven-column, six-row vertically suspended grid.
The pieces fall straight down, occupying the next available space within the column.
The objective of the game is to be the first
to form a horizontal, vertical, or diagonal line of four of one's own discs. """).pack(expand=True, fill="both")

def singleCon(): #if single player is chosen
   global oneCon
   oneCon = True #sets to single player
   boardCon() #then continues along multiplayer route

def boardCon():
   global frameCon #SO MANY VARIABLES
   global labelCon
   global pixelCon
   global blackImgCon
   global redImgCon
   global blankImgCon
   global gridCon
   global turnLabelCon
   global turnCon
   global gameOverCon
   global delayCon
   delayCon=time.time() #This is to make sure peoples plays dont overlap, and for single player it makes sure dont play while ai is going
   gameOverCon=False #sets the game to not over
   turnCon = "Black" #black plays first
   master.bind("<ButtonRelease-1>", clickCon) #binds the click to the function causes pieces drop
   for widget in master.winfo_children():
      widget.destroy()
   turnLabelCon = tk.Label(master, bg = "#000000", fg="#fff", text=turnCon + "'s turn") #displays whos turn it is
   turnLabelCon.grid(row = 8, columnspan = 7)
   Label(master, bg = "#000000", fg="#fff", text="Connect4").grid(row = 0, column = 2, columnspan = 3)
   tk.Button(master, text = "Menu", height = 1, width = 10, fg = "#000000", bg="#fff", command = lambda: Connect4()).grid(row = 0, column = 0, columnspan = 2, sticky = "we")
   tk.Button(master, text = "How to Play", height = 1, width = 10, fg = "#000000", bg="#fff", command = lambda: howToPlayCon()).grid(row = 0, column = 5, columnspan = 2, sticky = "we")
   if screenWidth<screenHeight:
      pixelCon=(screenWidth//7)#width is 7 blocks
   else:
      pixelCon=(screenHeight//7) #height is 6 plus the top and bottom bars (7)
   blackImgCon = ImageTk.PhotoImage(Image.open("gameFiles/blackChec.png").resize((pixelCon, pixelCon), resample=0)) #imports images, black piece
   redImgCon = ImageTk.PhotoImage(Image.open("gameFiles/redChec.png").resize((pixelCon, pixelCon), resample=0)) #red piece
   blankImgCon = ImageTk.PhotoImage(Image.open("gameFiles/blankChec.png").resize((pixelCon, pixelCon), resample=0)) #blank piece
   frameCon=[[]]
   labelCon=[[]]
   gridCon=[[]]
   for r in range(6):
      if len(frameCon)==r:
         frameCon.append([]) #where labels go
         gridCon.append([]) #keeps track of which are empty and full
         labelCon.append([]) #labels
      for c in range(7):
         gridCon[r].append(" ") #all empty
         frameCon[r].append(tk.Frame(master, width = pixelCon, height = pixelCon))
         frameCon[r][c].grid(row=r+1, column=c, sticky="nsew")
         frameCon[r][c].propagate(False)
         labelCon[r].append(tk.Label(frameCon[r][c], image = blankImgCon, bg = "blue2")) #always get created with blank piece
         labelCon[r][c].pack(expand=True, fill="both")

def clickCon(event): #when user clicks, or ai choses a place
   master.unbind("<ButtonRelease-1>") #unbinds so user cannot click while this is happening
   global gridCon
   global labelCon
   global turnLabelCon
   global turnCon
   global delayCon
   if (time.time()-delayCon) > .25 and gameOverCon == False: #if game is not over and time is above .25 since last click
      for c in range(7): #for every column
         moveOn=False
         try:
            check = event - 1
            if c == event:
               moveOn=True
         except TypeError:
            if (master.winfo_pointerx() > (pixelCon*c) and master.winfo_pointerx() < (pixelCon*(c+1)) and master.winfo_pointery() > 20): #if clicked in that row, or if ai chose this column
               moveOn=True
         if moveOn == True:
            turnLabelCon.config(text="") #if single player this will get rid of bar for the rest of the game
            turnLabelCon.update() #updates instantly
            for f in range(6): #for the height of the column (starting at top)
               if gridCon[f][c] == " ": #if nothing is there
                  if f-1 >= 0: #if it is not the first in the list
                     labelCon[f-1][c].config(image = blankImgCon) #turn one before to blank
                  if turnCon == "Black": #if blacks turn
                     labelCon[f][c].config(image = blackImgCon) #make black
                  else: #else it is reds turn
                     labelCon[f][c].config(image = redImgCon) #make red
                  master.update_idletasks()
                  time.sleep(.03) #makes falling effect
                  if f == 5: #if bottom row
                     gridCon[f][c] = turnCon
                     if turnCon == "Black" and oneCon == False: #only in multiplayer
                        turnLabelCon.config(text= ("Red's turn")) #switches bottom message
                     elif turnCon == "Red" and oneCon == False:
                        turnLabelCon.config(text= ("Black's turn")) #switches message
                     checkCon(turnCon) #goes through checking for end game
                     if turnCon == "Black": #switches whos turn it is
                        turnCon = "Red"
                     elif turnCon == "Red":
                        turnCon = "Black"
                     master.update()
               else: #if something is there
                  if f-1 >= 0: #if not first in list
                     gridCon[f-1][c] = turnCon #sets the grid to know where everyone played
                     if turnCon == "Black" and oneCon == False: #same code as above for next few lines
                        turnLabelCon.config(text= ("Red's turn"))
                     elif turnCon == "Red" and oneCon == False:
                        turnLabelCon.config(text= ("Black's turn"))
                     checkCon(turnCon)
                     if turnCon == "Black":
                        turnCon = "Red"
                     elif turnCon == "Red":
                        turnCon = "Black"
                     master.update()
                  else: #if nothing could be dropped
                     turnLabelCon.config(text="You cannot play there.") #display error message
                  break #so more than one column can not be clicked with one click
            try: #if an integer number, therefore ai click ends here
               delayCon = time.time() - event #creative way to check if event = integer number, and to guarantee that you can click right after ai is triggered that you can click right after ai is triggered
            except TypeError: #if not an integer (user click)
               delayCon=time.time() #resets time so user does not spam
               if (oneCon == True) and (gameOverCon==False) and (f-1 >= 0): #if singleplayer, game is not over and the piece was able to be dropped
                  aiCon() #ai gets triggered
            break
   master.bind("<ButtonRelease-1>", clickCon) #rebinds so user can click again

def aiCon(): #decides where ai should place
   time.sleep(.5)
   whereDrop=11 #first checks for any possible winning situation
   for c in range(7): #up and down
      for x in range(3): #c and x change starting point
         playHere=True
         for r in range(3): #for 3 in a row
            if gridCon[-(r+x+1)][c] != "Red": #if any are not red
               playHere=False #then 3 are not in a row
               break
         if gridCon[-(x+4)][c] != " ": #checks to see if empty space
            playHere=False
         if playHere == True:
            whereDrop=c #this is the column to drop in
            break

   for r in range(6): #side to side
      for c in range(4): #r and c determine starting point
         playHere=True
         missing=10 #this is to check if more than 1 are missing
         for x in range(4): #for the 4 in a row
            if gridCon[-(r+1)][c+x] == " ": #goes across the columns
               if missing == 10: #if first time missing
                  missing=c+x #sets this spot as column
               else: #if not the first time
                  playHere=False #then its not 3 in a row
                  break
            elif gridCon[-(r+1)][c+x] == "Black": #if any are not red
               playHere=False #not 3 in a row
               break
         if playHere == True: #if 3 in a row
            if r == 0: #if on bottom row
               whereDrop=missing #play here
               break
            else: #if a higher row
               if gridCon[-(r)][missing] != " ": #then if piece underneath is filled
                  whereDrop=missing #play here
                  break

   for r in range(3): #/
      for c in range(4):
         playHere=True
         missingC=10
         for x in range(4): #this will change row and column
            if gridCon[-(r+x+1)][c+x] == " ": #row starts at bottom, column left to right
               if missingC == 10:
                  missingC=c+x #sets c for where to drop
                  missingR=-(r+x+1) #sets r for checking if block underneath is filled
               else:
                  playHere=False
                  break
            elif gridCon[-(r+x+1)][c+x] == "Black":
               playHere=False
               break
         if playHere == True:
            if missingR == -1: #if bottom row
               whereDrop=missingC
               break
            else:
               if gridCon[missingR+1][missingC] != " ":
                  whereDrop=missingC
                  break

   for r in range(3): #\
      for c in range(4):
         playHere=True
         missingC=10
         for x in range(4):
            if gridCon[-(r+x+1)][-(c+x+1)] == " ": #row starts bottom to top, column right to left
               if missingC == 10:
                  missingC=7-(c+x+1) #need to make a positive instead of a negative, 7-(the negative) does this
                  missingR=-(r+x+1)
               else:
                  playHere=False
                  break
            elif gridCon[-(r+x+1)][-(c+x+1)] == "Black":
               playHere=False
               break
         if playHere == True:
            if missingR == -1:
               whereDrop=missingC
               break
            else:
               if gridCon[missingR+1][missingC] != " ":
                  whereDrop=missingC
                  break
   
   if whereDrop < 10: #if a spot was chosen
      clickCon(whereDrop) #play here
      
   else: #if no winning way, checks for blocks, all same code as above but black becomes red and visa versa
      for c in range(7): #up and down
         for x in range(3):
            playHere=True
            for r in range(3):
               if gridCon[-(r+x+1)][c] != "Black":
                  playHere=False
                  break
            if gridCon[-(x+4)][c] != " ":
               playHere=False
            if playHere == True:
               whereDrop=c
               break

      for r in range(6): #side to side
         for c in range(4):
            playHere=True
            missing=10
            for x in range(4):
               if gridCon[-(r+1)][c+x] == " ":
                  if missing == 10:
                     missing=c+x
                  else:
                     playHere=False
                     break
               elif gridCon[-(r+1)][c+x] == "Red":
                  playHere=False
                  break
            if playHere == True:
               if r == 0:
                  whereDrop=missing
                  break
               else:
                  if gridCon[-(r)][missing] != " ":
                     whereDrop=missing
                     break

      for r in range(3): #/
         for c in range(4):
            playHere=True
            missingC=10
            for x in range(4):
               if gridCon[-(r+x+1)][c+x] == " ":
                  if missingC == 10:
                     missingC=c+x
                     missingR=-(r+x+1)
                  else:
                     playHere=False
                     break
               elif gridCon[-(r+x+1)][c+x] == "Red":
                  playHere=False
                  break
            if playHere == True:
               if missingR == -1:
                  whereDrop=missingC
                  break
               else:
                  if gridCon[missingR+1][missingC] != " ":
                     whereDrop=missingC
                     break

      for r in range(3): #\
         for c in range(4):
            playHere=True
            missingC=10
            for x in range(4):
               if gridCon[-(r+x+1)][-(c+x+1)] == " ":
                  if missingC == 10:
                     missingC=7-(c+x+1)
                     missingR=-(r+x+1)
                  else:
                     playHere=False
                     break
               elif gridCon[-(r+x+1)][-(c+x+1)] == "Red":
                  playHere=False
                  break
            if playHere == True:
               if missingR == -1:
                  whereDrop=missingC
                  break
               else:
                  if gridCon[missingR+1][missingC] != " ":
                     whereDrop=missingC
                     break
      
      if whereDrop < 10:
         clickCon(whereDrop)
      else: #if no 3 in a rows, random
         while True:
            c = random.randint(0, 6) #random column
            if gridCon[0][c] == " ": #if able to be placed
               clickCon(c) #places in that column
               break

def checkCon(turnCon): #checks for game over
   for c in range(7): #up-down check, goes column by column
      for x in range(3): #3 possible wins in each column
         gameWin=True #sets win to true
         for r in range(4): #for the length of the winning row
            if gridCon[r+x][c] != turnCon: #if not a 4 in a row
               gameWin=False #game not over
               break
         if gameWin == True: #if was winning
            endCon(turnCon) #end game with winner

   for r in range(6): #left-right check, goes row by row
      for x in range(4): #4 possible wins in each row
         gameWin=True
         for c in range(4): #rest is same as above
            if gridCon[r][c+x] != turnCon:
               gameWin=False
               break
         if gameWin == True:
            endCon(turnCon)

   for r in range(3): #\ check, 3 possible row wins
      for c in range(4): #4 possible column wins
         gameWin=True
         for x in range(4):
            if gridCon[r+x][c+x] != turnCon:
               gameWin=False
               break
         if gameWin == True:
            endCon(turnCon)

   for r in range(3): #/ check, 3 possible row wins
      for c in range(4): #4 possible column wins
         gameWin=True
         for x in range(4):
            if gridCon[-(r+1+x)][c+x] != turnCon:
               gameWin=False
               break
         if gameWin == True:
            endCon(turnCon)

   gameEnd=True #board full check
   for r in range(6): #for rows
      for c in range(7): #for columns
         if gridCon[r][c] == " ": #if empty
            gameEnd=False #not over
   if gameEnd == True:
      endCon("No one") #triggers end message saying no one won

def endCon(turnCon): #when game is over
   global turnLabelCon
   global gameOverCon
   gameOverCon=True #sets game to over
   if oneCon == True: #if single player
      if turnCon == "Black": #user is black
         turnLabelCon.config(text="You win!")
      elif turnCon == "Red": #ai is red
         turnLabelCon.config(text="You lose.")
      else: #tie
         turnLabelCon.config(text="It is a tie.")
   else: #if multiplayer
      turnLabelCon.config(text=turnCon + " wins!") #who evers turn it is wins, if a tie the turnCon is "no one"
   tk.Button(master, text = "Play Again", height = 1, width = 10, fg = "#000000", bg="#fff", command = lambda: boardCon()).grid(row = 0, column = 5, columnspan = 2, sticky = "we") #allows user to play again

#################################################################################################### Connect4 end

#################################################################################################### Threes start

#Sam Gunter
#Threes was finished 2:05am on the 31st of May, 2018
#This was created to create the threes game, similar to 2048
#

#Next steps are to 

#Threes: Global variables and functions normally have a "The" at the end incase another game uses similar variables later on (or earlier on).
#
#
#

#################################################################################################### Threes end

#################################################################################################### Checkers start

#Sam Gunter
#Checkers was finished 2:05am on the 31st of May, 2018
#This was created to play checkers either single player or against AI
#

#Next steps are to 

#Checkers: Global variables and functions normally have a "Chec" at the end incase another game uses similar variables later on or earlier on.
#
#
#

#################################################################################################### Checkers end

#################################################################################################### HangMan start

#Sam Gunter
#HangMan was finished 2:05am on the 31st of May, 2018
#This was created to play hang man either against another player or against the database
#

#Next steps are to 

#HangMan: Global variables and functions normally have a "Hang" at the end incase another game uses similar variables later on or earlier on.
#
#
#

#################################################################################################### HangMan end



master = Tk() #creates the window
master.title("2k's games")
master.overrideredirect(1) #gets rid of toolbar
master.geometry("%dx%d+0+0" % (master.winfo_screenwidth(), master.winfo_screenheight())) #makes it fill full screen
screenWidth = master.winfo_screenwidth()
screenHeight = master.winfo_screenheight()

def unbind(): #unbinds anything I have binded (from multiple games) and goes back to home screen.
   master.unbind("<Up>")
   master.unbind("<Down>")
   master.unbind("<Left>")
   master.unbind("<Right>")
   master.unbind("<Button-1>")
   master.unbind("<ButtonRelease-1>")
   master.unbind("<Button-3>")
   master.unbind("<Button-2>")
   master.unbind("<Return>")
   menu()

def menu():
   for widget in master.winfo_children(): #clears contents, but not frame meaning it can update without making a new window each time
      widget.destroy()
   master.configure(bg = "#000000") #Sets initial background colour to black
   Label(master, bg = "#000000", fg="#fff", text="2k's Games").grid(row = 0, columnspan = 3) #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(master, text = "Quit", height = 1, width = 10, bg = "#fff", command = master.destroy).grid(row = 4, columnspan = 3, sticky = "we")
   tk.Button(master, text = "TicTacToe2.0", height = 5, width = 20, bg = "#fff", command = lambda: TicTacToe()).grid(row = 1, column = 0, sticky = "we")
   tk.Button(master, text = "MineSweeper", height = 5, width = 20, bg = "#fff", command = lambda: MineSweeper(" ")).grid(row = 1, column = 1, sticky = "we")
   tk.Button(master, text = "2048", height = 5, width = 20, bg = "#fff", command = lambda: the2048()).grid(row = 1, column = 2, sticky = "we")
   tk.Button(master, text = "Sudoku", height = 5, width = 20, bg = "#fff", command = lambda: Sudoku()).grid(row = 2, column = 0, sticky = "we")
   tk.Button(master, text = "Connect4", height = 5, width = 20, bg = "#fff", command = lambda: Connect4()).grid(row = 2, column = 1, sticky = "we")
   tk.Button(master, text = "CheckersNF", height = 5, width = 20, bg = "#fff", command = lambda: Checkers()).grid(row = 2, column = 2, sticky = "we")
   tk.Button(master, text = "HangManNF", height = 5, width = 20, bg = "#fff", command = lambda: HangMan()).grid(row = 3, column = 0, sticky = "we")
   tk.Button(master, text = "ThreesNF", height = 5, width = 20, bg = "#fff", command = lambda: Threes()).grid(row = 3, column = 1, sticky = "we")
   tk.Button(master, text = "NF = Not Finished", height = 5, width = 20, bg = "#fff", command = lambda: printBlah()).grid(row = 3, column = 2, sticky = "we")

menu()
master.mainloop()
