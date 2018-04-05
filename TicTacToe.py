from tkinter import *
import tkinter as tk
import random, time
from tkinter.font import Font

master = Tk() #creates the window
master.title("2k's games")
master.overrideredirect(1) #gets rid of toolbar
master.geometry("%dx%d+0+0" % (master.winfo_screenwidth(), master.winfo_screenheight())) #makes it fill full screen
screenWidth = master.winfo_screenwidth()
screenHeight = master.winfo_screenheight()

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
   master.configure(bg = "#000000") #Sets intial background colour to black
   Label(master, bg = "#000000", fg="#fff", text="TicTacToe2.0").grid(row = 0, column = 1) #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = master.destroy).grid(row = 0, column = 0, sticky = "we") #right now ends the program, later will redirect
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

   
   Label(frameMine1, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//60) + " bold", text="""Click on an empty tile to place an X or an O.
If single player the AI will automatically put down an 0 right after your X.""").pack(expand=True, fill="both")

   Label(frameMine2, bg = "whitesmoke", font = "Helvetica " + str(pixelMine//60), text="""The goal of Tic Tac Toe is to beat your oppenent by being the first to score a row.
One player is 0's and another is X's and the players alternate putting down their letter.
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
         elif levelTic == 2: #triggers meidum ai
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

def hardTic(difficulty): #difficulty changes depending on whtehr medium or hard was clicked
   global levelTic
   if difficulty=="easy": #easy ai
      levelTic=1
      reloadTic()
   elif difficulty=="medium": #medium ai
      levelTic=2
      reloadTic()
   else: #the only other possbility is hard
      levelTic=3
      reloadTic()

def reloadTic():
   global playerTic
   global sizeTic
   global frameTic
   for widget in master.winfo_children():
      widget.destroy()
   Label(master, bg = "#000000", fg="#fff", text="TicTacToe2.0").grid(row = 0, column = 1)
   Label(master, bg = "#000000", fg="#fff", text=playerTic + "'s turn").grid(row = 4, column = 1) #to keep it constant has a blank label at the bottom with no words, this is where winner is displayed or where it tells you you cant play there
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
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(0)).pack(expand=True, fill="both") #drops it down a bit so the bold doesnt make the squre bigger than the other (57 instead of 60)
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
         if gridWinTic[r*3+c]==1: #the row number minus 1 multiplied by 3 added by the column gets the spot on the grid, the 1 was set by an ealier function if there was a winner, if the line contained these characetrs then they will be bold for player to see
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=winFont,  bg = "#fff").pack(expand=True, fill="both") #drops it down a bit so the bold doesnt make the squre bigger than the other (57 instead of 60)
         else:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont, bg = "#fff").pack(expand=True, fill="both") #normal text
      #once this is done it will sit and wait for user to click menu and restart


def turnTic(number): #number is whichever button was clicked
   global playerTic
   global gridWinTic
   global levelTic
   if gridTic[number] == " ": #if it is valid (if no one has played there yet)
      gridTic[number] = playerTic #grid gets relaced with the player, if going against ai it will always be X, if multiplayer it starts as X but switched later in this function
      for counter in range(0,3): #this is just to make less code, happens 3 times (0,1,2, ends when at 3)
         if gridTic[0+counter*3] == gridTic[1+counter*3] == gridTic[2+counter*3] == playerTic: #left to right wins
            gridWinTic[0+counter*3]=gridWinTic[1+counter*3]=gridWinTic[2+counter*3]=1 #sets these to 1 (they started as 0) so that theyw ill be bold at the end, and so program knows a winner was declaired
         if gridTic[0+counter] == gridTic[3+counter] == gridTic[6+counter] == playerTic: #up and down wins
            gridWinTic[0+counter]=gridWinTic[3+counter]=gridWinTic[6+counter]=1
      if gridTic[0] == gridTic[4] == gridTic[8] == playerTic: #cross and the enxt is cross otehr way
         gridWinTic[0]=gridWinTic[4]=gridWinTic[8]=1
      if gridTic[2] == gridTic[4] == gridTic[6] == playerTic:#Using only if statements here because it is possibel for more than one to make a row at the same time, elif would cancel out the rest afetr the first is found
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
      else: #if there was a winner (not all the earleir 3 were 0s)
         if levelTic==0: #multiplayer
            endTic("multi") #see endtic for explanation
         else: #against ai, player won
            endTic("player")
   else: #if it wasnt valid, the bottom label gets used and the user goes again      
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
      if number==-1: #if the middle wasnt open and no 2 in the rows, the numebr is still -1. Now go to second priorty
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
         if number==-1: #if the middle wasnt open and no 2 in the rows, the numebr is still -1. Now go to second priorty
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
            if number==-1: #I dont count this as a priority, because it is a very specific senario which can go anywhere in the code, just decided to put after the 2 ina  rows
               if difficulty==3:
                  if gridTic[4] == "O" and gridTic[0] == gridTic[8] == "X" and gridTic[1] == gridTic[2] == gridTic[3] == gridTic[5] == gridTic[6] == gridTic[7] == " ":
                     number=1
                  elif gridTic[4] == "O" and gridTic[2] == gridTic[6] == "X" and gridTic[1] == gridTic[0] == gridTic[3] == gridTic[5] == gridTic[8] == gridTic[7] == " ":
                     number=1
               if number==-1: #I dont count this as a priority, because it is a very specific senario which can go anywhere in the code, just decided to put after the 2 ina  rows
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
                              if gridTic[0] == gridTic[8] == " " == gridTic[1] == gridTic[3]: #checks for open opposite corners and adjacent open. this is used to make oppertunities when ai has the iddle, or to block opputunities when ai does nto have the middle
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


TicTacToe()
master.mainloop()
