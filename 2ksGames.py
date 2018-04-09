from tkinter import *
import tkinter as tk
import random, time
from tkinter.font import Font

#################################################################################################### TicTacToe2.0 start


#Sam Gunter
#TicTacToe2.14 was finished 5:50pm on the 18th of march, 2018
#This was created to play TicTacToe either 2 player or against varying degrees of AI. The easy Ai should be easy (duh) to win against and the hard should be impossible to beat.
#Unlike TicTacToe1.0 this has a GUI to make the experience better. The hard ai is much better and now not only gets lines and blocks lines, but sets up plays where it is a guaranteed win.
#I created this in functions and procedures instead of linear to allow both single player and multiplayer to use the same blocks of code. This is also so multiple games can be added together in one document.

#Next step is to add a leaderboard document (will have to learn how to do file manipulation).

#TicTacToe: Global variables and functions normally have a "Tic" at the end incase another game uses similar variables later on.
#First function is gamemode, then if single player was chosen difficulty, then a function to set difficulty.
#No matter if single or multiplayer the next function creates the tkinter window and then one of the turns happen either turnTic or one of the ai, ends with endTic. User can go back to menu or click again and the person starting alternates
#It is always set up so the next function is last in the current function (using if and else statements)

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

def howToPlayTic():
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "#000000", fg = "#fff", text="TicTacToe2.0").grid(row = 0, column = 1)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: TicTacToe()).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/5))
   frameMine1.grid(row=2, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=3, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   
   Label(frameMine1, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//45) + " bold", text="""Click on an empty tile to place an X or an O.
If single player the AI will automatically put down an 0 right after your X.""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//45), text="""The goal of Tic Tac Toe is to beat your opponent by being the first to score a row.
One player is O's and another is X's and the players alternate putting down their letter.
If one player is able to get 3 of their letter in a row (up to down, left to right, or diagonal) then they win.""").pack(expand=True, fill="both")


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
   tk.Button(master, text = "Easy", height = 5, width = 20, bg = "#fff", command = lambda: hardTic("easy")).grid(row = 1, column = 0) #random ai
   tk.Button(master, text = "Medium", height = 5, width = 20, bg = "#fff", command = lambda: hardTic("medium")).grid(row = 1, column = 1) #ai that knows how to win, user goes first
   tk.Button(master, text = "Hard", height = 5, width = 20, bg = "#fff", command = lambda: hardTic("hard")).grid(row = 1, column = 2) #same ai as above, user goes second

def hardTic(difficulty): #difficulty changes depending on whether medium or hard was clicked
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
   winFont=Font(family="Helvetica", size=((sizeTic//5)*3), weight='bold')
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
#MineSweeper was finished 2:05am on the 31st of march, 2018
#This was created to copy the microsoft minesweeper game that we know and love
#I have tried my best to make it as efficient as possible with my (I admit) limited knowledge of programming, but on some computer it does have severe lag

#Next steps are to speed up the program, add images for bombs and flags and add a leaderboard document.

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then choice of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper()
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first click will never be a bomb. Allows user to chose to play again


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

def howToPlayMine():
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "darkgrey", text="MineSweeper").grid(row = 0, column = 1)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: MineSweeper(" ")).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/5))
   frameMine1.grid(row=2, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=3, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   
   Label(frameMine1, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//60) + " bold", text="""Left Click: Click on Tile

Right Click: Place flag

Middle Click: Chord""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//60), text="""The goal of Mine Sweeper is to clear every single tile that has no bomb (!) in it, while placing flags (?) on all tiles with bombs.
This can be achieved by paying close attention to the numbers on all tiles that have been clicked.
The different numbers in each clicked (sunken) tile show how many bombs that tile is touching (above, below, side or diagonal) with a maximum of 8.
For example, a 1 means that 7 of the adjacent tiles are safe, while an 8 means all of the touching tiles have bombs.
In the case of the 8 you would need to flag (?) every tile touching the 8, you can put down a flag (?) by right clicking on the mouse.

When you click on a tile that has no number assigned to it this means that no bombs are touching that tile.
Since Minesweeper knows that you can safely click all tiles around it, it automatically clicks them all for you. This is the reason a click can sometimes clear half the board.
Now go back to the 1 that was uncovered. If any of the tiles touching the 1 is a flag (therefore a bomb) you know that all the other boxes have no bombs (the 1 means only touching 1 bomb).
This means the other 7 tiles are safe to left click to uncover new numbers which will lead to new information about bombs.

Although you could click on each tile around the 1, there is a quicker way to complete the same task. A method called "chording".
If a number is uncovered (such as the 1) and the required amount of flags are touching that tile (meaning no other bombs possible), then you can chord.
Chording will automatically click every adjacent tile to the number that you chorded as long as there is no flag on the tile.
Be warned though, if you incorrectly placed your flags it could click on a spot with a bomb and end the game. To chord use the middle button on the mouse (not on all mouses).

The first click is guaranteed to be safe, but after that you must make choices for yourself, good luck!""").pack(expand=True, fill="both")
   
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
   global shownMine #Similar to TicTacToe(), most of these are barely called again, but have to all be declared her as global
   global frameMine
   global reliefMine
   global hiddenMine
   global myFont
   global pixelMine
   global flagsMine
   global statusMine
   global bombsLeftMine
   bombsLeftMine=bombMine #keep track of flag counter in top corner
   statusMine="start"
   for widget in master.winfo_children(): #same as TicTacToe2.0 this delete all widgets onscreen
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth//(sizeMine+1))
   else:
      pixelMine=(screenHeight//(sizeMine+1))
   
   hiddenMine=[[]] #this will be the minesweeper board fully filled up and user can not see it
   for r in range(sizeMine): #for the rows, which is the variable
      if len(hiddenMine)==r: #if if maxed out make a new list
         hiddenMine.append([])
      for c in range(sizeMine): #for columns which si the same variable (square)
         hiddenMine[r].append(" ") #adds an empty space, this is solely to make the list of lists
   shownMine=[[]] #what the user gets shown
   for r in range(sizeMine):
      if len(shownMine)==r:
         shownMine.append([])
      for c in range(sizeMine):
         shownMine[r].append("") #adds nothing this time instead of  a space so later on the program can see the difference between shown and hidden values
   reliefMine=[[]] #same as both lists of lists above, but is to set the buttons as raised so they can be changed to appear pushed down later on when they are clicked
   for r in range(sizeMine):
      if len(reliefMine)==r:
         reliefMine.append([])
      for c in range(sizeMine):
         reliefMine[r].append("raised")
   flagsMine=[[]] #same as all lists above, but for flags
   for r in range(sizeMine):
      if len(flagsMine)==r:
         flagsMine.append([])
      for c in range(sizeMine):
         flagsMine[r].append(" ")

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
         tk.Button(frameMine[r*sizeMine+c], text = shownMine[r][c], font=myFont, activebackground = "grey", bg = "lightgrey", command = lambda forCommand=[r, c]: clickMine(forCommand[0], forCommand[1])).pack(expand=True, fill="both") #adds teh button into the frame, these act as each square in minesweeper with a predefined textsize, background, etc

def flagMine(event): #This might be one of the most complicated codes I have created, so many numbers together all of which are variables and most of which are pixels related to screen
   if statusMine!="end": #makes it so this code doesn't run if bomb has been triggered
      global sizeMine
      global pixelMine
      global bombsLeftMine
      global flagsMine
      for r in range(sizeMine):
         for c in range(sizeMine):
            if frameMine[r*sizeMine+c].winfo_y() < master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_y()+pixelMine > master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_x() < master.winfo_pointerx() and frameMine[r*sizeMine+c].winfo_x()+pixelMine > master.winfo_pointerx() and reliefMine[r][c]=="raised": #long thing to see if the cursor is within frame window and if it is still raised (not checked yet)
               for widget in frameMine[r*sizeMine+c].winfo_children():
                  widget.destroy()
               if flagsMine[r][c] == "?": #if already a flag
                  bombsLeftMine+=1 #adds 1 bomb (because 1 less flag)
                  flagsMine[r][c]=" " #turns off flag
                  tk.Button(frameMine[r*sizeMine+c], text = shownMine[r][c], font=myFont, activebackground = "grey", bg = "lightgrey", command = lambda forCommand=[r, c]: clickMine(forCommand[0], forCommand[1])).pack(expand=True, fill="both") #creates button as normal
               else:
                  bombsLeftMine-=1 #takes a away 1 bomb from counter
                  flagsMine[r][c]="?" #makes a flag
                  tk.Button(frameMine[r*sizeMine+c], text = flagsMine[r][c], font=myFont, activebackground = "grey", bg = "lightgrey").pack(expand=True, fill="both") #button that has no command, just to display question mark until clicked again
      if bombsLeftMine>=0: #if not negative it will display bombs left
         button1=tk.Button(master, text = str(bombsLeftMine)+" bombs left", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff").grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we")
      else: #if negative it says too many flags
         button1=tk.Button(master, text = "Too many flags", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff").grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we")

def chordMine(event):
   if statusMine!="end":
      global sizeMine
      global pixelMine
      global flagsMine
      for r in range(sizeMine):
         for c in range(sizeMine):
            if frameMine[r*sizeMine+c].winfo_y() < master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_y()+pixelMine > master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_x() < master.winfo_pointerx() and frameMine[r*sizeMine+c].winfo_x()+pixelMine > master.winfo_pointerx() and reliefMine[r][c]=="sunken":
               chording=0 #this variable checks to see if all flags around the number have been declared
               if r-1>=0 and c-1>=0 and flagsMine[r-1][c-1] == "?": #if it exists and is a ?
                  chording+=1 #add 1 to chord
               if c-1>=0 and flagsMine[r][c-1] == "?":
                  chording+=1
               if r+1<sizeMine and c-1>=0 and flagsMine[r+1][c-1] == "?":
                  chording+=1          
               if r-1>=0 and flagsMine[r-1][c] == "?":
                  chording+=1            
               if r+1<sizeMine and flagsMine[r+1][c] == "?":
                  chording+=1
               if r-1>=0 and c+1<sizeMine and flagsMine[r-1][c+1] == "?":
                  chording+=1           
               if c+1<sizeMine and flagsMine[r][c+1] == "?":
                  chording+=1           
               if r+1<sizeMine and c+1<sizeMine and flagsMine[r+1][c+1] == "?":
                  chording+=1
               if chording == hiddenMine[r][c]: #if there are the same amount of flags as the number
                  if r-1>=0 and c-1>=0 and flagsMine[r-1][c-1] == " ": #clicks on every open spot around it
                     checkMine(r-1, c-1)
                  if c-1>=0 and flagsMine[r][c-1] == " ":
                     checkMine(r, c-1)            
                  if r+1<sizeMine and c-1>=0 and flagsMine[r+1][c-1] == " ":
                     checkMine(r+1, c-1)            
                  if r-1>=0 and flagsMine[r-1][c] == " ":
                     checkMine(r-1, c)            
                  if r+1<sizeMine and flagsMine[r+1][c] == " ":
                     checkMine(r+1, c)
                  if r-1>=0 and c+1<sizeMine and flagsMine[r-1][c+1] == " ":
                     checkMine(r-1, c+1)            
                  if c+1<sizeMine and flagsMine[r][c+1] == " ":
                     checkMine(r, c+1)            
                  if r+1<sizeMine and c+1<sizeMine and flagsMine[r+1][c+1] == " ":
                     checkMine(r+1, c+1)

def updateMine(row, column): #this updates only 1 square, before it was updating all of them but that make a slight lag (less than a second) which was not good
   for widget in frameMine[row*sizeMine+column].winfo_children(): #deletes all buttons in the frame (there will only be 1 button in the frame)
      widget.destroy()
   if shownMine[row][column] == " " or shownMine[row][column] == 1:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", activeforeground = "navy", bg = "lightgrey", fg = "blue").pack(expand=True, fill="both") #makes a new button which is the same as the last, but with new value
   elif shownMine[row][column] == 2:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", activeforeground = "dark green", bg = "lightgrey", fg = "green4").pack(expand=True, fill="both")
   elif shownMine[row][column] == 3:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", activeforeground = "red4", bg = "lightgrey", fg = "red").pack(expand=True, fill="both")
   elif shownMine[row][column] == 4:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", activeforeground = "midnight blue", bg = "lightgrey", fg = "navy").pack(expand=True, fill="both")
   elif shownMine[row][column] == 5:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", activeforeground = "brown4", bg = "lightgrey", fg = "crimson").pack(expand=True, fill="both")
   elif shownMine[row][column] == 6:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", activeforeground = "dark slate grey", bg = "lightgrey", fg = "darkcyan").pack(expand=True, fill="both")
   elif shownMine[row][column] == 7:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "black" ).pack(expand=True, fill="both")
   elif shownMine[row][column] == 8:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "silver").pack(expand=True, fill="both")
   else:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "black").pack(expand=True, fill="both")

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
   statusMine="end"
   for r in range(sizeMine):
      for c in range(sizeMine):
         for widget in frameMine[r*sizeMine+c].winfo_children():
            widget.destroy()
         if hiddenMine[r][c] == "!" and result == "lose": #if lose
            tk.Button(frameMine[r*sizeMine+c], text = hiddenMine[r][c], font=myFont, bg = "indianred").pack(expand=True, fill="both") #makes bombs show as red
         elif hiddenMine[r][c] == "!" and result == "win": #if win
            tk.Button(frameMine[r*sizeMine+c], text = "?", font=myFont).pack(expand=True, fill="both") #make bombs show as defused
         elif shownMine[r][c] == " " or shownMine[r][c] == 1:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "blue").pack(expand=True, fill="both") #all the rest just display their hidden numbers some of which were already shown
         elif shownMine[r][c] == 2:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "green").pack(expand=True, fill="both")
         elif shownMine[r][c] == 3:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "red").pack(expand=True, fill="both")
         elif shownMine[r][c] == 4:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "navy").pack(expand=True, fill="both")
         elif shownMine[r][c] == 5:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "crimson").pack(expand=True, fill="both")
         elif shownMine[r][c] == 6:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "darkcyan").pack(expand=True, fill="both")
         elif shownMine[r][c] == 7:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "black" ).pack(expand=True, fill="both")
         elif shownMine[r][c] == 8:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "silver").pack(expand=True, fill="both")
         else:
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "black").pack(expand=True, fill="both")


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
   else:
      checkMine(row, column) #after the first time just goes through this function instantly everytime

def checkMine(row, column): #when a button is clicked
   if hiddenMine[row][column]=="!": #if a bomb
      endMine("lose") #triggers lose
      for widget in frameMine[row*sizeMine+column].winfo_children():
         widget.destroy()
      tk.Button(frameMine[row*sizeMine+column], text = hiddenMine[row][column], font=myFont, bg = "darkred").pack(expand=True, fill="both") #dark red to make them know it was the bomb that killed them
      
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

#################################################################################################### Sudoku start

#Sam Gunter
#MineSweeper was finished 2:05am on the 31st of march, 2018
#This was created to copy the microsoft minesweeper game that we know and love
#I have tried my best to make it as efficient as possible with my (I admit) limited knowledge of programming, but on some computer it does have severe lag

#Next steps are to speed up the program, add images for bombs and flags and add a leaderboard document.

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then chocie of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper()
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first clickw ill never be a bomb. Allows user to chose to play again

def generateSu():
   global shownSu
   global hiddenSu
   hiddenSu=[[9, 4, 5, 6, 2, 7, 8, 3, 1],
             [2, 8, 7, 1, 5, 3, 6, 9, 4],
             [1, 3, 6, 8, 4, 9, 2, 7, 5],
             [6, 2, 4, 3, 7, 8, 1, 5, 9],
             [5, 1, 8, 4, 9, 2, 3, 6, 7],
             [7, 9, 3, 5, 6, 1, 4, 2, 8],
             [4, 6, 1, 7, 3, 5, 9, 8, 2],
             [3, 5, 9, 2, 8, 4, 7, 1, 6],
             [8, 7, 2, 9, 1, 6, 5, 4, 3]]
   
   shownSu= [[9, 4, " ", 6, " ", 7, " ", " ", 1],
             [2, " ", 7, " ", " ", " ", " ", 9, 4],
             [1, " ", 6, " ", 4, 9, " ", " ", " "],
             [" ", 2, " ", 3, 7, 8, " ", " ", 9],
             [" ", 1, " ", 4, " ", 2, " ", 6, " "],
             [7, " ", " ", 5, 6, 1, " ", 2, " "],
             [" ", " ", " ", 7, 3, " ", 9, " ", 2],
             [3, 5, " ", " ", " ", " ", 7, " ", 6],
             [8, " ", " ", 9, " ", 6, " ", 4, 3]]
   Sudoku()

def Sudoku():
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth//10)
   else:
      pixelMine=(screenHeight//10)
   myFont=Font(family="Helvetica", size=pixelMine//2)
   Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixelMine//5), text="Sudoku").grid(row = 0, columnspan = 9)
   tk.Button(master, text = "Menu", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: menu()).grid(row = 0, column = 0, columnspan=3, sticky = "we")
   frameSu=[]

   for r in range(9):
      for c in range(9):
         frameSu.append(tk.Frame(master, width = pixelMine, height = pixelMine))
         frameSu[r*9+c].grid(row=r+1, column=c, sticky="nsew") 
         frameSu[r*9+c].propagate(False)
         if shownSu[r][c]==" ":
            tk.Entry(frameSu[r*9+c], font=myFont, bg = "#fff").pack(expand=True, fill="both")
         else:
            tk.Label(frameSu[r*9+c], text = shownSu[r][c], font=myFont, fg = "#000000", bg = "#fff").pack(expand=True, fill="both")

#get()
#Entry not button

#################################################################################################### Sudoku end

#################################################################################################### 2048 start

#Sam Gunter
#2048 was finished 2:18pm on the 6th of april, 2018
#This was created to play 2048. The hardest and longest part was making the program appear fluid, not a sudden movement where the entire screen refreshes,
#but making it refresh one by one as the label moves. If the entire screen reloaded it would be too slow, so I had to completely change how I made frames on tkinter.

#Next step is to make user be able to slide cursor, add how to play and add a leaderboard document (will have to learn how to do file manipulation).

#2048: Global variables and functions normally have a 2048 at the end, main one is called the2048 because had to have letters.
#First function is gamemode, then if single player was chosen difficulty, then a function to set difficulty.
#No matter if single or multiplayer the next function creates the tkinter window and then one of the turns happen either turnTic or one of the ai, ends with endTic. User can go back to menu or click again and the person starting alternates
#It is always set up so the next function is last in the current function (using if and else statements)

def the2048():
   global pixel2048
   global value2048
   global frame2048
   global win2048
   win2048="schrodinger"
   master.bind("<Up>", up2048) #binds the up, down, left, right arrows on keyboard
   master.bind("<Down>", down2048)
   master.bind("<Left>", left2048)
   master.bind("<Right>", right2048)
   master.bind("<Button-1>", buttonclick2048)
   master.bind("<ButtonRelease-1>", buttonrelease2048)
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixel2048=(screenWidth//5)
   else:
      pixel2048=(screenHeight//5)
   Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//6), text="2048").grid(row = 0, column=1, columnspan = 2)
   tk.Button(master, text = "Menu", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: unbind()).grid(row = 0, column = 0, sticky = "we")
   tk.Button(master, text = "How To Play", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: howToPlay2048()).grid(row = 0, column = 3, sticky = "we")

   frame2048=[[]] #same as all lists above, but for flags
   for r in range(4):
      if len(frame2048)==r:
         frame2048.append([])
      for c in range(4):
         frame2048[r].append(tk.Frame(master, bd = 2, width = pixel2048, height = pixel2048))
         frame2048[r][c].grid(row=r+1, column=c, sticky="nsew") 
         frame2048[r][c].propagate(False)

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

   
   reloadFull2048()

def howToPlay2048():
   for widget in master.winfo_children():
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth)
   else:
      pixelMine=(screenHeight)
   Label(master, bg = "#000000", fg = "#fff", text="2048").grid(row = 0, column = 1)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: the2048()).grid(row = 0, column = 0, sticky = "we")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/5))
   frameMine1.grid(row=2, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight/2))
   frameMine2.grid(row=3, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   
   Label(frameMine1, bg = "silver", font = "Helvetica " + str(pixelMine//45) + " bold", text="""Use the arrow keys to go up, down, left or right.
You can also use your finger (or mouse) and drag across the screen to shift the board.""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "silver", font = "Helvetica " + str(pixelMine//45), text="""The goal of 2048 is to get a tile containing the number "2048".
To achieve this goal you must merge numbers together to create larger numbers.
When you shift the board ALL numbers on the board move as far as they can over.
If 2 numbers are the same they will merge to create the sum of those numbers (2s become 4, 4s  become 8 and so on.
Everytime you shift the board a new 2 will appear at the opposite end of the board.""").pack(expand=True, fill="both")


def reloadFull2048():
   global win2048
   win2048="False"
   for r in range(4):
      for c in range(4):
         if value2048[r][c] == " ":
            win2048="schrodinger"
         if r>0:
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
         for widget in frame2048[r][c].winfo_children(): #deletes all
            widget.destroy()
         if value2048[r][c] == " ":
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "grey").pack(expand=True, fill="both")
         elif value2048[r][c] == 2:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "white").pack(expand=True, fill="both")
         elif value2048[r][c] == 4:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "lemonchiffon").pack(expand=True, fill="both")
         elif value2048[r][c] == 8:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "sandybrown").pack(expand=True, fill="both")
         elif value2048[r][c] == 16:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "chocolate").pack(expand=True, fill="both")
         elif value2048[r][c] == 32:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "salmon").pack(expand=True, fill="both")
         elif value2048[r][c] == 64:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "tomato").pack(expand=True, fill="both")
         elif value2048[r][c] == 128:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//3), fg = "#000000", bg = "khaki").pack(expand=True, fill="both")
         elif value2048[r][c] == 256:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//3), fg = "#000000", bg = "yellow").pack(expand=True, fill="both")
         elif value2048[r][c] == 512:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//3), fg = "#000000", bg = "gold").pack(expand=True, fill="both")
         elif value2048[r][c] == 1024:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//4), fg = "#000000", bg = "orange").pack(expand=True, fill="both")
         elif value2048[r][c] == 2048:
            tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//4), fg = "#000000", bg = "goldenrod").pack(expand=True, fill="both")
   if win2048 == "True":
      Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="You Win!").grid(row = 5, columnspan = 4, sticky = "we")
      tk.Button(master, text = "Play Again", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: the2048()).grid(row = 0, column = 3, sticky = "we")
   if win2048 == "False":
      Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixel2048//10), text="You Lose").grid(row = 5, columnspan = 4, sticky = "we")
      tk.Button(master, text = "Play Again", font=("Helvetica", pixel2048//9), height = 1, bg = "#fff", command = lambda: the2048()).grid(row = 0, column = 3, sticky = "we")

   
def reload2048(r, c):
   for widget in frame2048[r][c].winfo_children(): #deletes one
      widget.destroy()
   if value2048[r][c] == " ":
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "grey").pack(expand=True, fill="both")
   elif value2048[r][c] == 2:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "white").pack(expand=True, fill="both")
   elif value2048[r][c] == 4:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "lemonchiffon").pack(expand=True, fill="both")
   elif value2048[r][c] == 8:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "sandybrown").pack(expand=True, fill="both")
   elif value2048[r][c] == 16:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "chocolate").pack(expand=True, fill="both")
   elif value2048[r][c] == 32:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "salmon").pack(expand=True, fill="both")
   elif value2048[r][c] == 64:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//2), fg = "#000000", bg = "tomato").pack(expand=True, fill="both")
   elif value2048[r][c] == 128:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//3), fg = "#000000", bg = "khaki").pack(expand=True, fill="both")
   elif value2048[r][c] == 256:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//3), fg = "#000000", bg = "yellow").pack(expand=True, fill="both")
   elif value2048[r][c] == 512:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//3), fg = "#000000", bg = "gold").pack(expand=True, fill="both")
   elif value2048[r][c] == 1024:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//4), fg = "#000000", bg = "orange").pack(expand=True, fill="both")
   elif value2048[r][c] == 2048:
      tk.Label(frame2048[r][c], text = value2048[r][c], font=("Helvetica", pixel2048//4), fg = "#000000", bg = "goldenrod").pack(expand=True, fill="both")

def buttonclick2048(event): #checks x and y value with first click
   global x2048
   global y2048
   x2048=master.winfo_pointerx()
   y2048=master.winfo_pointery()

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
                  time.sleep(.01)
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


def down2048(event):
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
                  time.sleep(.01)
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

def left2048(event): #this is the same code as up2048, but r and c is switched throughout it
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
                  time.sleep(.01)
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
      
def right2048(event): #this is the same code as down,2048 but r and c are switched throughout it
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
                  time.sleep(.01)
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
      
#################################################################################################### 2048 end

#################################################################################################### Threes start

#Sam Gunter
#MineSweeper was finished 2:05am on the 31st of march, 2018
#This was created to copy the microsoft minesweeper game that we know and love
#I have tried my best to make it as efficient as possible with my (I admit) limited knowledge of programming, but on some computer it does have severe lag

#Next steps are to speed up the program, add images for bombs and flags and add a leaderboard document.

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then chocie of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper()
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first clickw ill never be a bomb. Allows user to chose to play again

#################################################################################################### Threes end

#################################################################################################### Checkers start

#Sam Gunter
#MineSweeper was finished 2:05am on the 31st of march, 2018
#This was created to copy the microsoft minesweeper game that we know and love
#I have tried my best to make it as efficient as possible with my (I admit) limited knowledge of programming, but on some computer it does have severe lag

#Next steps are to speed up the program, add images for bombs and flags and add a leaderboard document.

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then chocie of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper()
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first clickw ill never be a bomb. Allows user to chose to play again

#################################################################################################### Checkers end

#################################################################################################### HangMan start

#Sam Gunter
#MineSweeper was finished 2:05am on the 31st of march, 2018
#This was created to copy the microsoft minesweeper game that we know and love
#I have tried my best to make it as efficient as possible with my (I admit) limited knowledge of programming, but on some computer it does have severe lag

#Next steps are to speed up the program, add images for bombs and flags and add a leaderboard document.

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then chocie of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper()
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first clickw ill never be a bomb. Allows user to chose to play again

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
   menu()

def menu():
   for widget in master.winfo_children(): #clears contents, but not frame meaning it can update without making a new window each time
      widget.destroy()
   master.configure(bg = "#000000") #Sets initial background colour to black
   Label(master, bg = "#000000", fg="#fff", text="2k's Games").grid(row = 0, columnspan = 3) #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(master, text = "Quit", height = 1, width = 10, bg = "#fff", command = master.destroy).grid(row = 4, columnspan = 3, sticky = "we")
   tk.Button(master, text = "TicTacToe2.0", height = 5, width = 20, bg = "#fff", command = lambda: TicTacToe()).grid(row = 1, column = 0, sticky = "we")
   tk.Button(master, text = "MineSweeper", height = 5, width = 20, bg = "#fff", command = lambda: MineSweeper(" ")).grid(row = 1, column = 1, sticky = "we")
   tk.Button(master, text = "SudokuNF", height = 5, width = 20, bg = "#fff", command = lambda: generateSu()).grid(row = 1, column = 2, sticky = "we")
   tk.Button(master, text = "2048", height = 5, width = 20, bg = "#fff", command = lambda: the2048()).grid(row = 2, column = 0, sticky = "we")
   tk.Button(master, text = "ThreesNF", height = 5, width = 20, bg = "#fff", command = lambda: Threes()).grid(row = 2, column = 1, sticky = "we")
   tk.Button(master, text = "CheckersNF", height = 5, width = 20, bg = "#fff", command = lambda: Checkers()).grid(row = 2, column = 2, sticky = "we")
   tk.Button(master, text = "HangManNF", height = 5, width = 20, bg = "#fff", command = lambda: HangMan()).grid(row = 3, column = 0, sticky = "we")
   tk.Button(master, text = "Connect4NF", height = 5, width = 20, bg = "#fff", command = lambda: Connect4()).grid(row = 3, column = 1, sticky = "we")
   tk.Button(master, text = "NF = Not Finished", height = 5, width = 20, bg = "#fff", command = lambda: Connect4()).grid(row = 3, column = 2, sticky = "we")

menu()
master.mainloop()
