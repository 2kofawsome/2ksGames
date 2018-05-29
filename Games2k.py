import tkinter as tk
import random, time, os, gspread
from tkinter.font import Font
from PIL import ImageTk, Image
from oauth2client.service_account import ServiceAccountCredentials

print("LOADING...")
print("Please wait...")

#################################################################################################### TicTacToe2.0 start

#Sam Gunter
#TicTacToe2.14 was finished 5:50pm on the 18th of March, 2018.
#This was created to play TicTacToe either 2 player or against varying degrees of AI. The easy AI should be easy (duh) to win against and the hard should be impossible to beat.
#Unlike TicTacToe1.0 this has a GUI to make the experience better. The hard AI is much better and now not only gets lines and blocks lines, but sets up plays where it is a guaranteed win.
#I created this in functions and procedures instead of linear to allow both single player and multiplayer to use the same blocks of code. This is also so multiple games can be added together in one document.

#Next step is to add time tracker

#TicTacToe: Global variables and functions normally have a "Tic" at the end incase another game uses similar variables later on.
#First function is gamemode, then if single player was chosen difficulty, then a function to set difficulty.
#No matter if single or multiplayer the next function creates the tkinter window and then one of the turns happen either turnTic or one of the AI, ends with endTic. User can go back to menu or click again and the person starting alternates.
#It is always set up so the next function is last in the current function (using if and else statements).

def TicTacToe():
   for widget in master.winfo_children():
      widget.destroy()
   global gamesTic, levelTic, gridWinTic, gridTic, playerTic, sizeTic, screenWidth, screenHeight, delayTic #most of these variables only have to be called up in 1 or 2 functions
   delayTic=time.time()
   sizeTic=((screenHeight-screenHeight//16)//3)
   gamesTic=0 #if playing against ai this sets who plays first (alternates)
   levelTic=0 #default, if it stays as 0 multiplayer will run, if singleplayer is chosen this will change to 1 (random ai) or 2 (ai that knows how to win)
   gridTic=[' ', ' ', ' ', #this is the TicTacToe grid, only has 3 lines to make it easier to look at
        ' ', ' ', ' ',
        ' ', ' ', ' ']
   gridWinTic=[0, 0, 0, #0 means there have been no wins, will change to 1 when a winning line made
        0, 0, 0,
        0, 0, 0]
   playerTic="X" #default start is X, this will not matter if singleplayer is chosen

   frameSin=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameSin.grid(row = 1, column = 0, columnspan = 3, sticky = "we")
   frameSin.propagate(False)
   frameMul=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameMul.grid(row = 1, column = 3, columnspan = 3, sticky = "we")
   frameMul.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayTic()).pack(expand=True, fill="both") #right now ends the program, later will redirect
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both") #right now ends the program, later will redirect
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="TicTacToe2.0").pack(expand=True, fill="both") #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(frameSin, text = "Singleplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: singleplayerTic()).pack(expand=True, fill="both") #command=lambda stops the programs from running when the window is first created
   tk.Button(frameMul, text = "Multiplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: loadTic()).pack(expand=True, fill="both") #when clicked redirects to whichever function is command

def howToPlayTic(): #just tutorial on how to play
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="TicTacToe2.0").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", font = "Helvetica " + str(screenHeight//40), bg = "#fff", command = lambda: TicTacToe()).pack(expand=True, fill="both")

   frameTic1=tk.Frame(master, width = screenWidth, height = screenHeight/3) #a third of the screen, leaves room for top bar
   frameTic1.grid(row=1, columnspan=2, sticky="nsew")
   frameTic1.propagate(False)
   frameTic2=tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10)) #half the screen
   frameTic2.grid(row=2, columnspan=2, sticky="nsew")
   frameTic2.propagate(False)


   tk.Label(frameTic1, bg = "white smoke", font = "Helvetica " + str(screenHeight//37) + " bold", text="""

Program specific instructions

1. Click on an empty tile to place an X or an O.
2. If playing multiplayer, alternate with the other player.
3. If playing single player, the AI will automatically play instantly.""").pack(expand=True, fill="both") #game specfic instructions (buttons)

   tk.Label(frameTic2, bg = "white smoke", font = "Helvetica " + str(screenHeight//40), text="""Rules to Game:

The game is played on a grid that's 3 squares by 3 squares.
Players take turns putting their marks in empty squares.
The first player to get 3 marks in a row (up, down, across, or diagonally) is the winner.
If all 9 squares are full, the game is over.
If no player has 3 marks in a row, the game ends in a tie.""").pack(expand=True, fill="both") #how to play, taken from some website probably


def againTic(): #if the user wants to play again
   global gridWinTic, levelTic, gridTic, playerTic, gamesTic
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
         loadTic()
      else:
         playerTic="X"
         loadTic()
   else:
      if gamesTic % 2 == 0:
         loadTic() #player goes first
      else: #ai goes first
         if levelTic == 1: #tiggers easy ai
            loadTic()
            aiTic(1)
         elif levelTic == 2: #triggers medium ai
            loadTic()
            aiTic(2)
         elif levelTic == 3: #triggers hard ai
            loadTic()
            aiTic(3)

def singleplayerTic():
   for widget in master.winfo_children():
      widget.destroy()

   frameEasy=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameEasy.grid(row = 1, column = 0, columnspan = 2, sticky = "we")
   frameEasy.propagate(False)
   frameMedium=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameMedium.grid(row = 1, column = 2, columnspan = 2, sticky = "we")
   frameMedium.propagate(False)
   frameHard=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameHard.grid(row = 1, column = 4, columnspan = 2, sticky = "we")
   frameHard.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayTic()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//60), command = lambda: menu()).pack(expand=True, fill="both") #sends back to first TicTacToe screen
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="TicTacToe2.0").pack(expand=True, fill="both")
   tk.Button(frameEasy, text = "Easy", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: setTic("easy")).pack(expand=True, fill="both") #random ai
   tk.Button(frameMedium, text = "Medium", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: setTic("medium")).pack(expand=True, fill="both") #ai that knows how to win, user goes first
   tk.Button(frameHard, text = "Hard", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: setTic("hard")).pack(expand=True, fill="both") #same ai as above, user goes second

def setTic(difficulty): #difficulty changes depending on whether medium or hard was clicked
   global levelTic
   if difficulty=="easy": #easy ai
      levelTic=1
      loadTic()
   elif difficulty=="medium": #medium ai
      levelTic=2
      loadTic()
   else: #the only other possibility is hard
      levelTic=3
      loadTic()

def loadTic():
   global playerTic, sizeTic, frameTic, buttonTic, labelWho
   for widget in master.winfo_children():
      widget.destroy()
   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//16)
   frameTitle.grid(row = 0, column = 0, columnspan = 10, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//35), bg = "#000000", fg="#fff", text="TicTacToe2.0").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(sizeTic*3)), height = sizeTic//2)
   frameMenu.grid(row = 1, column = 3, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(sizeTic*3)), height = sizeTic//2)
   frameHow.grid(row = 2, column = 3, sticky = "we")
   frameHow.propagate(False)
   frameWho=tk.Frame(master, width = (screenWidth-(sizeTic*3)), height = sizeTic*2)
   frameWho.grid(row = 3, column = 3, rowspan = 4, sticky = "we")
   frameWho.propagate(False)
   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(sizeTic*3))//25), bg = "#fff", command = lambda: TicTacToe()).pack(expand=True, fill="both")
   tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(sizeTic*3))//25), bg = "#fff", command = lambda: howToPlayTic()).pack(expand=True, fill="both") #menu goes right back to start
   labelWho = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(sizeTic*3))//7), fg="#fff", text=playerTic + "'s\nturn")
   labelWho.pack(expand=True, fill="both") #to keep it constant has a blank label at the bottom with no words, this is where winner is displayed or where it tells you you can't play there
   frameTic=[]
   myFont=Font(family="Helvetica", size=((sizeTic//7)*4))
   buttonTic=[]
   for r in range(0, 3):
      for c in range(0,3): #r is the number of rows, c is the column number
         frameTic.append(tk.Frame(master, width = sizeTic, height = sizeTic))
         frameTic[r*3+c].grid(row=(r*2)+1, column=c, rowspan=2, sticky="nsew")
         frameTic[r*3+c].propagate(False)
         if r*3+c == 0:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(0)))
            buttonTic[0].pack(expand=True, fill="both") #drops it down a bit so the bold does not make the square bigger than the other (57 instead of 60)
         elif r*3+c == 1:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(1)))
            buttonTic[1].pack(expand=True, fill="both")
         elif r*3+c == 2:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(2)))
            buttonTic[2].pack(expand=True, fill="both")
         elif r*3+c == 3:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(3)))
            buttonTic[3].pack(expand=True, fill="both")
         elif r*3+c == 4:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(4)))
            buttonTic[4].pack(expand=True, fill="both")
         elif r*3+c == 5:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(5)))
            buttonTic[5].pack(expand=True, fill="both")
         elif r*3+c == 6:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(6)))
            buttonTic[6].pack(expand=True, fill="both")
         elif r*3+c == 7:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(7)))
            buttonTic[7].pack(expand=True, fill="both")
         elif r*3+c == 8:
            buttonTic.append(tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(8)))
            buttonTic[8].pack(expand=True, fill="both")
   if gridTic[0]!=" " and gridTic[1]!=" " and gridTic[2]!=" " and gridTic[3]!=" " and gridTic[4]!=" " and gridTic[5]!=" " and gridTic[6]!=" " and gridTic[7]!=" " and gridTic[8]!=" ": #This means everything is filled up
      endTic("tie") #putting "tie" tells the function it was a tie for the bottom label

def reloadTic():
   global playerTic, sizeTic, frameTic, buttonTic
   myFont=Font(family="Helvetica", size=((sizeTic//7)*4))
   if levelTic == 0:
      labelWho.config(font = "Helvetica " + str((screenWidth-(sizeTic*3))//6), text=playerTic + "'s\nturn")
   else:
      labelWho.config(font = "Helvetica " + str((screenWidth-(sizeTic*3))//6), text="")
   for r in range(0, 3):
      for c in range(0,3): #r is the number of rows, c is the column number
         if r*3+c == 0:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(0))
         elif r*3+c == 1:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(1))
         elif r*3+c == 2:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(2))
         elif r*3+c == 3:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(3))
         elif r*3+c == 4:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(4))
         elif r*3+c == 5:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(5))
         elif r*3+c == 6:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(6))
         elif r*3+c == 7:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(7))
         elif r*3+c == 8:
            buttonTic[r*3+c].config(text = gridTic[r*3+c], font=myFont,  bg = "#fff", command = lambda: turnTic(8))
   if gridTic[0]!=" " and gridTic[1]!=" " and gridTic[2]!=" " and gridTic[3]!=" " and gridTic[4]!=" " and gridTic[5]!=" " and gridTic[6]!=" " and gridTic[7]!=" " and gridTic[8]!=" ": #This means everything is filled up
      endTic("tie") #putting "tie" tells the function it was a tie for the bottom label

def endTic(result):
   global gridWinTic, playerTic, sizeTic, frameTic
   myFont=Font(family="Helvetica", size=((sizeTic//7)*4))
   winFont=Font(family="Helvetica", size=((sizeTic//5)*3), weight='bold') #different fonts for win or game in progress
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//16)
   frameTitle.grid(row = 0, column = 0, columnspan = 10, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//35), bg = "#000000", fg="#fff", text="TicTacToe2.0").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(sizeTic*3)), height = sizeTic//2)
   frameMenu.grid(row = 1, column = 3, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(sizeTic*3)), height = sizeTic//2)
   frameHow.grid(row = 2, column = 3, sticky = "we")
   frameHow.propagate(False)
   frameWho=tk.Frame(master, width = (screenWidth-(sizeTic*3)), height = sizeTic*2)
   frameWho.grid(row = 3, column = 3, rowspan = 4, sticky = "we")
   frameWho.propagate(False)

   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str(screenHeight//25), bg = "#fff", command = lambda: TicTacToe()).pack(expand=True, fill="both")
   tk.Button(frameHow, text = "Play Again", font = "Helvetica " + str(screenHeight//25), bg = "#fff", command = lambda: againTic()).pack(expand=True, fill="both")

   if result=="tie": #if it is a tie display this
      if levelTic > 0:
         update(1+(levelTic*3), 1)
      tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(sizeTic*3))//7), fg="#fff", text="It is\na Tie.").pack(expand=True, fill="both")
   elif result=="multi": #if multiplayer, the playerTic was the last one who played therefore the winner
      tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(sizeTic*3))//7), fg="#fff", text=playerTic+"\nwins!").pack(expand=True, fill="both")
   elif result=="player": #in player vs ai, player wins
      update((levelTic*3), 1)
      tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(sizeTic*3))//7), fg="#fff", text="You\nwin!").pack(expand=True, fill="both")
   elif result=="ai": #in player vs ai, ai wins
      update(2+(levelTic*3), 1)
      tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(sizeTic*3))//7), fg="#fff", text="You\nlose.").pack(expand=True, fill="both")
   frameTic=[]
   for r in range(0, 3): #THIS WHOLE THING IS ONLY TO MAKE THE CODE SHORTER, WAS AROUND 50 LINES FOR THIS BEFORE WITH IF, ELIF, ELSE STATEMENTS
      for c in range(0,3): #r is the number of rows, c is the column number
         frameTic.append(tk.Frame(master, width = sizeTic, height = sizeTic))
         frameTic[r*3+c].grid(row=(r*2)+1, column=c, rowspan = 2, sticky="nsew", padx = 0, pady = 0)
         frameTic[r*3+c].propagate(False)
         if gridWinTic[r*3+c]==1: #the row number minus 1 multiplied by 3 added by the column gets the spot on the grid, the 1 was set by an earlier function if there was a winner, if the line contained these characters then they will be bold for player to see
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=winFont,  bg = "#fff").pack(expand=True, fill="both") #drops it down a bit so the bold does not make the square bigger than the other (57 instead of 60)
         else:
            tk.Button(frameTic[r*3+c], text = gridTic[r*3+c], font=myFont, bg = "#fff").pack(expand=True, fill="both") #normal text
      #once this is done it will sit and wait for user to click menu and restart

def turnTic(number): #number is whichever button was clicked
   global playerTic, gridWinTic, levelTic, delayTic
   if (time.time()-delayTic)>.55:
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
               buttonTic[number].config(text = gridTic[number])
               master.update()
               delayTic=time.time()
               time.sleep(.5)
               aiTic(1)
            elif levelTic == 2: #triggers hard ai
               buttonTic[number].config(text = gridTic[number])
               master.update()
               delayTic=time.time()
               time.sleep(.5)
               aiTic(2)
            elif levelTic == 3: #triggers hard ai
               buttonTic[number].config(text = gridTic[number])
               master.update()
               delayTic=time.time()
               time.sleep(.5)
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
         labelWho.config(font = "Helvetica " + str((screenWidth-(sizeTic*3))//10), text="You cannot\nplay there.")

def aiTic(difficulty):
   global gridTic, GridWinTic
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

#Next step is to add time tracker

#MineSweeper: Global variables and functions normally have a "Mine" at the end incase another game uses similar variables later on (or earlier on).
#First function is MineSweeper(). Then choice of easy, medium or hard presets, or custom. If custom is out of range goes back to MineSweeper().
#Then creates the board, depending on the click either ends game or shows number and allows player to go again, first click will never be a bomb. Allows user to chose to play again.


def MineSweeper(errorCheck):
   master.bind("<Button-3>", flagMine)
   master.bind("<Button-2>", chordMine)
   global varSizeMine, varBombMine #this becomes a non var variable later (var is from tkinter)
   for widget in master.winfo_children():
      widget.destroy()
   master.configure(bg = "darkgrey") #Sets initial background colour to dark grey


   frameEasy=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameEasy.grid(row = 1, column = 0, columnspan = 2, sticky = "we")
   frameEasy.propagate(False)
   frameMedium=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameMedium.grid(row = 1, column = 2, columnspan = 2, sticky = "we")
   frameMedium.propagate(False)
   frameHard=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameHard.grid(row = 1, column = 4, columnspan = 2, sticky = "we")
   frameHard.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)
   frameSize=tk.Frame(master, width = screenWidth, height = screenHeight//5)
   frameSize.grid(row = 2, column = 0, columnspan = 6, sticky = "we")
   frameSize.propagate(False)
   frameBomb=tk.Frame(master, width = screenWidth, height = screenHeight//5)
   frameBomb.grid(row = 3, column = 0, columnspan = 6, sticky = "we")
   frameBomb.propagate(False)
   frameCus=tk.Frame(master, width = screenWidth, height = screenHeight//4)
   frameCus.grid(row = 4, column = 0, columnspan = 6, sticky = "we")
   frameCus.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "darkgrey", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayMine()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "darkgrey", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "darkgrey", font = "fixedsys " + str(screenHeight//35), fg="#000000", text="MineSweeper").pack(expand=True, fill="both")
   tk.Button(frameEasy, text = "Easy", bg = "darkgrey", font = "Helvetica " + str(screenHeight//20), command = lambda: gameSetMine(1)).pack(expand=True, fill="both")
   tk.Button(frameMedium, text = "Medium", bg = "darkgrey", font = "Helvetica " + str(screenHeight//20), command = lambda: gameSetMine(2)).pack(expand=True, fill="both")
   tk.Button(frameHard, text = "Hard", bg = "darkgrey", font = "Helvetica " + str(screenHeight//20), command = lambda: gameSetMine(3)).pack(expand=True, fill="both")

   varSizeMine=tk.IntVar() #declaired the var variables
   varBombMine=tk.IntVar()

   tk.Scale(frameSize, bg="#fff", from_=8, to=24, font = "Helvetica " + str(screenHeight//35), orient = "horizontal", variable=varSizeMine, label="The size of your grid (X by X)").pack(expand=True, fill="both") #this is a scale (slider) for custom games
   tk.Scale(frameBomb, bg="#fff", from_=8, to=99, font = "Helvetica " + str(screenHeight//35), orient = "horizontal", variable=varBombMine, label="The number of bombs").pack(expand=True, fill="both") #horizontal is side to side, from/to is range
   tk.Button(frameCus, text = "Custom Game: (The sliders)", font = "Helvetica " + str(screenHeight//30), bg = "darkgrey", command = lambda: gameSetMine(0)).pack(expand=True, fill="both") #command=lambda stops the programs from running when the window is first created
   if errorCheck=="True":
      tk.Label(master, bg = "darkgrey", fg = "darkred", text="You have too many bombs").grid(row = 9, columnspan = 3, sticky="we")

def howToPlayMine(): #see TicTacToe how to play, all others will have no comments
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="MineSweeper").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//40), command = lambda: MineSweeper(" ")).pack(expand=True, fill="both")

   frameMine1=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frameMine1.grid(row=1, columnspan=2, sticky="nsew")
   frameMine1.propagate(False)
   frameMine2=(tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10)))
   frameMine2.grid(row=2, columnspan=2, sticky="nsew")
   frameMine2.propagate(False)

   tk.Label(frameMine1, bg = "white smoke", font = "Helvetica " + str(screenHeight//35) + " bold", text="""

Program specific instructions

1. Left Click: Click on Tile
2. Right Click: Place flag
3. Middle Click: Chord""").pack(expand=True, fill="both")

   tk.Label(frameMine2, bg = "white smoke", font = "Helvetica " + str(screenHeight//40), text="""Rules to Game:

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
   global sizeMine, bombMine, difficultyMine
   difficultyMine = level
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
   global shownMine, frameMine, reliefMine, hiddenMine, myFont, pixelMine, statusMine, bombsLeftMine, buttonMine, flagImgMine, bombImgMine, labelMine, buttonHow #Similar to TicTacToe(), most of these are barely called again, but have to all be declared here as global
   bombsLeftMine=bombMine #keep track of flag counter in top corner
   statusMine="start"
   for widget in master.winfo_children(): #same as TicTacToe2.0 this delete all widgets onscreen
      widget.destroy()
   pixelMine=((screenHeight-screenHeight//18)//sizeMine)
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


   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//18)
   frameTitle.grid(row = 0, column = 0, columnspan = 25, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//35), bg = "darkgrey", fg="#000000", text="MineSweeper").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(pixelMine*sizeMine)), height = ((screenHeight-(screenHeight//18))//sizeMine)*(sizeMine//3))
   frameMenu.grid(row = 1, column = sizeMine, rowspan = sizeMine//3, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(pixelMine*sizeMine)), height = ((screenHeight-(screenHeight//18))//sizeMine)*(sizeMine//3))
   frameHow.grid(row = (sizeMine//3)+1, column = sizeMine, rowspan = sizeMine//3, sticky = "we")
   frameHow.propagate(False)
   frameWho=tk.Frame(master, width = (screenWidth-(pixelMine*sizeMine)), height = ((screenHeight-(screenHeight//18))//sizeMine)*(sizeMine-(sizeMine//3 + sizeMine//3)))
   frameWho.grid(row = (sizeMine//3 + sizeMine//3)+1, column = sizeMine, rowspan = sizeMine-(sizeMine//3 + sizeMine//3), sticky = "we")
   frameWho.propagate(False)
   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(pixelMine*sizeMine))//12), bg = "darkgrey", command = lambda: MineSweeper(" ")).pack(expand=True, fill="both")
   buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(pixelMine*sizeMine))//12), bg = "darkgrey", command = lambda: howToPlayMine())
   buttonHow.pack(expand=True, fill="both")
   labelMine = tk.Label(frameWho, font = "Helvetica " + str((screenWidth-(pixelMine*sizeMine))//10), bg = "darkgrey", text = str(bombsLeftMine)+" bombs left")#this label is named because it has to be edited later on
   labelMine.pack(expand=True, fill="both")


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
      global bombsLeftMine, shownMine, buttonMine #flagImgMine
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
         labelMine.config(text = str(bombsLeftMine)+" bombs left")
      else: #if negative it says too many flags
         labelMine.config(text = "Too many flags")

def chordMine(event):
   if statusMine!="end":
      global sizeMine, pixelMine
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
   buttonHow.config(text = "Again", command = lambda: createBoardMine()) #allows user to play again with the same specifications (board size and amount of bombs)
   global statusMine, buttonMine
   statusMine="end"
   if result == "lose":
      update(12+(difficultyMine*2), 1)
      labelMine.config(text = "You lose.")
   elif result == "win":
      update(11+(difficultyMine*2), 1)
      labelMine.config(text = "You win!")
   for r in range(sizeMine):
      for c in range(sizeMine):
         if hiddenMine[r][c] == "!" and result == "lose": #if lose
            buttonMine[r][c].config(image=bombImgMine, bg = "indianred")  #make bombs show as red
         elif hiddenMine[r][c] == "!" and result == "win": #if win
            buttonMine[r][c].config(image=flagImgMine, text = "?") #make bombs show as defused

def clickMine(row, column): #This is used 1 time to make sure the user doesn't get out 1st time
   global statusMine, sizeMine, hiddenMine
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

#Next step is to add time tracker

#2048: Global variables and functions normally have a 2048 at the end, main one is called the2048 because had to have letters.
#Creates board with 2 numbers inside it. Then user can click arrow or swipe mouse/finger across screen.
#All numbers move in that direction and combine if possible. Constantly checking for game end.

def the2048():
   global pixel2048, value2048, frame2048, label2048, win2048, delay2048, labelWho, buttonHow
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
   pixel2048=((screenHeight-screenHeight//17)//4)

   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//17)
   frameTitle.grid(row = 0, column = 0, columnspan = 10, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//40), bg = "#000000", fg="#fff", text="2048").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(pixel2048*4)), height = pixel2048)
   frameMenu.grid(row = 1, column = 4, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(pixel2048*4)), height = pixel2048)
   frameHow.grid(row = 2, column = 4, sticky = "we")
   frameHow.propagate(False)
   frameWho=tk.Frame(master, width = (screenWidth-(pixel2048*4)), height = pixel2048*2)
   frameWho.grid(row = 3, column = 4, rowspan = 4, sticky = "we")
   frameWho.propagate(False)

   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(pixel2048*3))//17), bg = "#fff", command = lambda: unbind()).pack(expand=True, fill="both")
   buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(pixel2048*3))//17), bg = "#fff", command = lambda: howToPlay2048())
   buttonHow.pack(expand=True, fill="both") #menu goes right back to start
   labelWho = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(pixel2048*3))//12), fg="#fff", text="")
   labelWho.pack(expand=True, fill="both")

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

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="2048").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//40), command = lambda: the2048()).pack(expand=True, fill="both")

   frame20481=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frame20481.grid(row=1, columnspan=2, sticky="nsew")
   frame20481.propagate(False)
   frame20482=(tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10)))
   frame20482.grid(row=2, columnspan=2, sticky="nsew")
   frame20482.propagate(False)


   tk.Label(frame20481, bg = "white smoke", font = "Helvetica " + str(screenHeight//37) + " bold", text="""

Program specific instructions

1.Use the arrow keys to go up, down, left or right.
2.You can also use your finger (or mouse)
to drag across the screen to shift the board.""").pack(expand=True, fill="both")

   tk.Label(frame20482, bg = "white smoke", font = "Helvetica " + str(screenHeight//35), text="""Rules to Game:

When two tiles with the same number touch they merge into one,
that means 2s become a 4, 4s a 8, 8s a 16 and so on.
You are attempting to try to get a block of 2048 (2^11),
which makes you win the game!""").pack(expand=True, fill="both")

def reloadFull2048():
   global win2048, label2048
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
      update(20, 1)
      labelWho.config(text="You\nWin!")
      buttonHow.config(text = "Play Again", font = "Helvetica " + str((screenWidth-(pixel2048*3))//17), command = lambda: the2048())
   elif win2048 == "False":
      update(21, 1)
      labelWho.config(text="You\nLose.")
      buttonHow.config(text = "Play Again", font = "Helvetica " + str((screenWidth-(pixel2048*3))//17), command = lambda: the2048())

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
   global x2048, y2048
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
            labelWho.config(text="")
            column = random.randint(0, 3) #random column
            for c in range(4): #makes it so it will check all fast and not just random
               if value2048[3][(column+c)%4] == " ": #if empty. % is modular so remainder
                  value2048[3][(column+c)%4] = 2 #put in a 2
                  break #then break, else do again with 1 higher
         else: #else, display a message saying no
            labelWho.config(text="Can't go\nthat way")
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
            labelWho.config(text="")
            column = random.randint(0, 3)
            for c in range(4):
               if value2048[0][(column+c)%4] == " ": #0 not 3
                  value2048[0][(column+c)%4] = 2
                  break
         else:
            labelWho.config(text="Can't go\nthat way")

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
            labelWho.config(text="")
            row = random.randint(0, 3)
            for r in range(4):
               if value2048[(row+r)%4][3] == " ":
                  value2048[(row+r)%4][3] = 2
                  break
         else:
            labelWho.config(text="Can't go\nthat way")

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
            labelWho.config(text="")
            row = random.randint(0, 3)
            for r in range(4):
               if value2048[(row+r)%4][0] == " ":
                  value2048[(row+r)%4][0] = 2
                  break
         else:
            labelWho.config(text="Can't go\nthat way")
         reloadFull2048()
   delay2048 = time.time()

#################################################################################################### 2048 end

#################################################################################################### Sudoku start

#Sam Gunter
#Sudoku was finished 1:03am on the 14th of April, 2018.
#This was created to allow the user to play sudoku on the computer.
#I have tried my best to add a random generator to make the games less static, but it came down to the tried and true method of "f--- it, it is good enough".

#Next step is to add time tracker

#Sudoku: Global variables and functions normally have a "Su" at the end incase another game uses similar variables later on (or earlier on).
#First function is Sudoku(). Then chocie of easy, medium or hard. Then triggers a board to be generated from one of the preset fully complete and semi-random tiles chosen to show.
#Next it loads the board, then when users click and type in numbers it saves, always checking for errors or to end the game. At the end you can play again.

def Sudoku():
   for widget in master.winfo_children():
      widget.destroy()

   frameEasy=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameEasy.grid(row = 1, column = 0, columnspan = 2, sticky = "we")
   frameEasy.propagate(False)
   frameMedium=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameMedium.grid(row = 1, column = 2, columnspan = 2, sticky = "we")
   frameMedium.propagate(False)
   frameHard=tk.Frame(master, width = screenWidth//3, height = screenHeight//4)
   frameHard.grid(row = 1, column = 4, columnspan = 2, sticky = "we")
   frameHard.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlaySu()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Sudoku").pack(expand=True, fill="both")
   tk.Button(frameEasy, text = "Easy", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: generateSu(20)).pack(expand=True, fill="both") #different difficulties are solely how many clues at the beginning
   tk.Button(frameMedium, text = "Medium", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: generateSu(15)).pack(expand=True, fill="both") #I wanted to improve this, but alas I could not
   tk.Button(frameHard, text = "Hard", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: generateSu(10)).pack(expand=True, fill="both")

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
   global shownSu, staticSu, hiddenSu, mistakeSu, difficultySu

   if difficulty == 10:
      difficultySu = 2
   elif difficulty == 15:
      difficultySu = 1
   elif difficulty == 20:
      difficultySu = 0

   fileSu = open(".\gameFiles\SudokuBoards.txt").readlines() #from a txt file, to add more to file and see more its working see "CreateBoardsSudoku.py"

   hiddenSu = solvedBoardSu(random.randint(0, (len(fileSu)-2))) #choses board from random number within the amount of boards

   patternSu = [[False, False, False, False, False, False, False, False, False], #sets pattern as non shown
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
   mistakeSu=[[]] #if numbers conflict, first made with no conflictions
   for r in range(9):
      if len(shownSu)==r:
         mistakeSu.append([])
         shownSu.append([])
         staticSu.append([])
      for c in range(9):
         mistakeSu[r].append(False) #all made with no conflictions
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

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Sudoku").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//40), command = lambda: loadBoardSu()).pack(expand=True, fill="both")

   frameSu1=tk.Frame(master, width = screenWidth, height = screenHeight/3)
   frameSu1.grid(row=1, columnspan=2, sticky="nsew")
   frameSu1.propagate(False)
   frameSu2=tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10))
   frameSu2.grid(row=2, columnspan=2, sticky="nsew")
   frameSu2.propagate(False)

   tk.Label(frameSu1, bg = "white smoke", font = "Helvetica " + str(screenHeight//37) + " bold", text="""

Program specific instructions

1. Click on a space you want to edit, then us your keyboard to type a number.
2. To save the number either click enter or click on another tile.
3. Leave a tile empty to delete.
4. Red squares mean that there are numbers that conflict.""").pack(expand=True, fill="both")

   tk.Label(frameSu2, bg = "white smoke", font = "Helvetica " + str(screenHeight//35), text="""Rules to Game:

The objective is to fill a 9x9 grid so that each column,
each row, and each of the nine 3x3 boxes (also called
blocks or regions) contains the digits from 1 to 9. """).pack(expand=True, fill="both")

def loadBoardSu():
   try:
      global myFont, pixelSu, buttonsSu, shownSu, frameSu, rowSu, columnSu, errorSu, mistakeSu, buttonHow
      master.bind("<Return>", enterSu)

      for widget in master.winfo_children():
         widget.destroy()
      rowSu=-1 #for clickSu() later on
      columnSu=-1
      pixelSu=((screenHeight-screenHeight//17)//9)
      myFont=Font(family="Helvetica", size=pixelSu//2)
      boldFont=Font(family="Helvetica", size=pixelSu//2, weight='bold')

      frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//17)
      frameTitle.grid(row = 0, column = 0, columnspan = 20, sticky = "we")
      frameTitle.propagate(False)
      tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//40), bg = "#000000", fg="#fff", text="Sudoku").pack(expand=True, fill="both")

      frameMenu=tk.Frame(master, width = (screenWidth-(pixelSu*9)), height = pixelSu*2)
      frameMenu.grid(row = 1, column = 10, rowspan = 2, sticky = "we")
      frameMenu.propagate(False)
      frameHow=tk.Frame(master, width = (screenWidth-(pixelSu*9)), height = pixelSu*2)
      frameHow.grid(row = 3, column = 10, rowspan = 2, sticky = "we")
      frameHow.propagate(False)
      frameWho=tk.Frame(master, width = (screenWidth-(pixelSu*9)), height = pixelSu*5)
      frameWho.grid(row = 5, column = 10, rowspan = 5, sticky = "we")
      frameWho.propagate(False)

      tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(pixelSu*9))//17), bg = "#fff", command = lambda: Sudoku()).pack(expand=True, fill="both")
      buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(pixelSu*9))//17), bg = "#fff", command = lambda: howToPlaySu())
      buttonHow.pack(expand=True, fill="both") #menu goes right back to start
      errorSu = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(pixelSu*9))//12), fg="#fff", text="")
      errorSu.pack(expand=True, fill="both")

      frameSu=[[]] #frames for size
      buttonsSu=[[]] #buttons in frames
      for r in range(9):
         if len(buttonsSu)==r:
            buttonsSu.append([])
            frameSu.append([])
         for c in range(9):
            frameSu[r].append(tk.Frame(master, width = pixelSu, height = pixelSu, borderwidth = "1")) #borderwidth of 1 gives it that nice look of slight lines between
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

            if (c//3 + r//3) % 2 == 0 and mistakeSu[r][c]==True:
               buttonsSu[r][c].config(bg='firebrick1')
            elif (c//3 + r//3) % 2 == 1 and mistakeSu[r][c]==True:
               buttonsSu[r][c].config(bg='firebrick3')
   except NameError: #if a game is not started, back to home screen
      Sudoku()

def clickSu(row, column):
   global buttonsSu, frameSu, shownSu, rowSu, columnSu, entry

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
   global shownSu, mistakeSu
   try: #tries to save the number and bring up button
      errorSu.config(text = "")
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
         errorSu.config(text = "Use numbers only!") #tell them they broke the game

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
      update(23+difficultySu, 1)
      buttonHow.config(text = "Play Again", command = lambda: Sudoku()) #allows the user to play again
      errorSu.config(text="You win!") #changes from preset error message (earlier) to winner message

#################################################################################################### Sudoku end

#################################################################################################### Connect4 start

#Sam Gunter
#Connect4 was finished 3:31am on the 28th of April, 2018
#This was created to play Connect 4 either against another player or against AI.
#AI checks for winning plays, blocking plays, but the rest is random. This allows the user to set up plays, but no easy wins.

#Next steps are to add different AIs and time tracker

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

   frameSin=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameSin.grid(row = 1, column = 0, columnspan = 3, sticky = "we")
   frameSin.propagate(False)
   frameMul=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameMul.grid(row = 1, column = 3, columnspan = 3, sticky = "we")
   frameMul.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayCon()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Connect 4").pack(expand=True, fill="both")
   tk.Button(frameSin, text = "Singleplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: singleCon()).pack(expand=True, fill="both")
   tk.Button(frameMul, text = "Multiplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: boardCon()).pack(expand=True, fill="both")

def howToPlayCon(): #see other how-to-plays
   master.unbind("<ButtonRelease-1>")
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Connect 4").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//40), command = lambda: Connect4()).pack(expand=True, fill="both")

   frameCon1=(tk.Frame(master, width = screenWidth, height = screenHeight/3))
   frameCon1.grid(row=1, columnspan=2, sticky="nsew")
   frameCon1.propagate(False)
   frameCon2=(tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10)))
   frameCon2.grid(row=2, columnspan=2, sticky="nsew")
   frameCon2.propagate(False)

   tk.Label(frameCon1, bg = "white smoke", font = "Helvetica " + str(screenHeight//37) + " bold", text="""

Program specific instructions

1.Click in any column to add a connect 4 piece.""").pack(expand=True, fill="both")

   tk.Label(frameCon2, bg = "white smoke", font = "Helvetica " + str(screenHeight//35), text="""Rules to Game:

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
   global frameCon, labelCon, pixelCon, blackImgCon, redImgCon, blankImgCon, gridCon, turnLabelCon, turnCon, gameOverCon, delayCon,  buttonHow

   delayCon=time.time() #This is to make sure peoples plays dont overlap, and for single player it makes sure dont play while ai is going
   gameOverCon=False #sets the game to not over
   turnCon = "Black" #black plays first
   master.bind("<ButtonRelease-1>", clickCon) #binds the click to the function causes pieces drop
   for widget in master.winfo_children():
      widget.destroy()

   pixelCon=((screenHeight-screenHeight//17)//6) #height is 6 plus the top and bottom bars (7)

   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//17)
   frameTitle.grid(row = 0, column = 0, columnspan = 20, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//40), bg = "#000000", fg="#fff", text="Connect 4").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(pixelCon*7)), height = (pixelCon*1.5)//1)
   frameMenu.grid(row = 1, column = 8, rowspan = 3, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(pixelCon*7)), height = (pixelCon*1.5)//1)
   frameHow.grid(row = 4, column = 8, rowspan = 3, sticky = "we")
   frameHow.propagate(False)
   frameWho=tk.Frame(master, width = (screenWidth-(pixelCon*7)), height = pixelCon*3)
   frameWho.grid(row = 7, column = 8, rowspan = 6, sticky = "we")
   frameWho.propagate(False)

   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(pixelCon*7))//17), bg = "#fff", command = lambda: Connect4()).pack(expand=True, fill="both")
   buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(pixelCon*7))//17), bg = "#fff", command = lambda: howToPlayCon())
   buttonHow.pack(expand=True, fill="both") #menu goes right back to start
   turnLabelCon = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(pixelCon*7))//12), fg="#fff", text=turnCon + "'s turn") #displays whos turn it is
   turnLabelCon.pack(expand=True, fill="both")

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
         frameCon[r][c].grid(row=(r*2)+1, rowspan = 2, column=c, sticky="nsew")
         frameCon[r][c].propagate(False)
         labelCon[r].append(tk.Label(frameCon[r][c], image = blankImgCon, bg = "blue2")) #always get created with blank piece
         labelCon[r][c].pack(expand=True, fill="both")

def clickCon(event): #when user clicks, or ai choses a place
   master.unbind("<ButtonRelease-1>") #unbinds so user cannot click while this is happening
   global gridCon, labelCon, turnLabelCon, turnCon, delayCon
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
   global turnLabelCon, gameOverCon
   gameOverCon=True #sets game to over
   if oneCon == True: #if single player
      if turnCon == "Black": #user is black
         update(27, 1)
         turnLabelCon.config(text="You win!")
      elif turnCon == "Red": #ai is red
         update(29, 1)
         turnLabelCon.config(text="You lose.")
      else: #tie
         update(28, 1)
         turnLabelCon.config(text="It is a tie.")
   else: #if multiplayer
      turnLabelCon.config(text=turnCon + " wins!") #who evers turn it is wins, if a tie the turnCon is "no one"
   buttonHow.config(text = "Play Again", command = lambda: boardCon()) #allows user to play again

#################################################################################################### Connect4 end

#################################################################################################### HangMan start

#Sam Gunter
#HangMan was finished 10:42pm on the 4th of May, 2018
#This was created to play hangman either against another player or against the database.
#Multiplayer is user chosen word, single player is from the database I made (see code in gameFiles for how).

#Next steps are to fix letters on weird screens and to add time tracker

#HangMan: Global variables and functions normally have a "Hang" at the end incase another game uses similar variables later on or earlier on.
#Starts with asking whether single or multi, this triggers a function to choose which word.
#Then creates the game, with _ for letters, with 26 buttons for each letter. When a button is clicked it fills in blanks.

def HangMan():
   global alphabet
   alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #this is created now, and used later for creating buttons and checking for letters in the words
   for widget in master.winfo_children():
      widget.destroy()

   frameSin=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameSin.grid(row = 1, column = 0, columnspan = 3, sticky = "we")
   frameSin.propagate(False)
   frameMul=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameMul.grid(row = 1, column = 3, columnspan = 3, sticky = "we")
   frameMul.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayHang()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Hangman").pack(expand=True, fill="both")
   tk.Button(frameSin, text = "Singleplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: singleHang()).pack(expand=True, fill="both")
   tk.Button(frameMul, text = "Multiplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: multiHang()).pack(expand=True, fill="both")

def singleHang(): #if singleplayer is chosen
   global wordHang, soloHang
   soloHang = True
   wordHang = open(".\gameFiles\HangmanWords.txt").readlines() #creates list of all words in the file
   wordHang = wordHang[random.randint(0, (len(wordHang)-1))] #decides on 1 word out of list
   wordHang = wordHang.upper() #makes capital
   wordHang = wordHang[:-1] #removes blank space at the end

   loadHang() #loads the board

def multiHang(): #if multiplayer is chosen
   global soloHang, entry, comment
   soloHang=False
   master.bind("<Return>", enterHang) #binds this so user can click enter to submit
   for widget in master.winfo_children():
      widget.destroy()

   frameEntry=tk.Frame(master, width = screenWidth, height = screenHeight//4)
   frameEntry.grid(row = 1, column = 0, columnspan = 6, sticky = "we")
   frameEntry.propagate(False)
   frameEnter=tk.Frame(master, width = screenWidth, height = screenHeight//4)
   frameEnter.grid(row = 2, column = 0, columnspan = 6, sticky = "we")
   frameEnter.propagate(False)
   frameComment=tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight//2+screenHeight//10))
   frameComment.grid(row = 3, column = 0, columnspan = 6, sticky = "we")
   frameComment.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)


   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayHang()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Hangman").pack(expand=True, fill="both")
   comment = tk.Label(frameComment, bg = "#000000", font = "Helvetica " + str(screenHeight//25), fg="#fff", text="You can only use\nletters and spaces.\nMaximum of 15 characters.") #this changes to be more specific if the user doesnt follow the rules
   comment.pack(expand=True, fill="both")

   entry = tk.Entry(frameEntry, bg = "white smoke", font = "Helvetica " + str(screenHeight//15), justify = "center") #Where the user puts in the word
   entry.pack(expand=True, fill="both")
   entry.focus_set() #puts user cursor here instantly
   tk.Button(frameEnter, text = "Enter", bg = "#fff", font = "Helvetica " + str(screenHeight//35), command = lambda: enterHang("blah")).pack(expand=True, fill="both") #User can click here or click enter to save/check word

def enterHang(event): #event is used when enter is clicked, not the button
   global wordHang
   wordHang = entry.get() #gets word from entry
   wordHang=wordHang.upper() #makes it capital
   allowed=True
   for n in range(len(wordHang)):
      if wordHang[n].isnumeric(): #if there is a number
         allowed=False
         comment.config(text="No numbers allowed! Only letters and spaces.") #prints no numbers allowed
         break
      if False==(wordHang[n]==" " or wordHang[n].isalpha()): #if something not normal
         allowed=False
         comment.config(text="No weird characters! Only letters and spaces.") #prints no funny buissness
         break
   if allowed == True: #if neither of the above were triggered
      if len(wordHang)>15: #checks length
         comment.config(text="Too long! Maximum of 15 characters") #prints that it is too long
      else:
         master.unbind("<Return>") #unbinds enter
         loadHang() #loads the board

def howToPlayHang():
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Hangman").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", font = "Helvetica " + str(screenHeight//40), bg = "#fff", command = lambda: HangMan()).pack(expand=True, fill="both")

   frameHang1 = tk.Frame(master, width = screenWidth, height = screenHeight/3)
   frameHang1.grid(row=1, columnspan=2, sticky="nsew")
   frameHang1.propagate(False)
   frameHang2 = tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10))
   frameHang2.grid(row=2, columnspan=2, sticky="nsew")
   frameHang2.propagate(False)

   tk.Label(frameHang1, bg = "white smoke", font = "Helvetica " + str(screenHeight//37) + " bold", text="""

Program specific instructions

1. Click the letters to the right to guess them.
2. If playing multiplayer, one player choses the word/phrase.
3. If playing single player, a word will be pulled from the database""").pack(expand=True, fill="both")

   tk.Label(frameHang2, bg = "white smoke", font = "Helvetica " + str(screenHeight//40), text="""Rules to Game:

The goal is to guess the word/phrase before your man gets hung! one letter at a time.
If the letter you guess is in the word, they will get filled in.
If the letter is not in the word, another part of the hangman is filled in.
As the game progresses, the man gets closer and closer to complete.
If you complete the word before the man is done, you win!
""").pack(expand=True, fill="both")

def loadHang():
   global buttonHow, hangImg, hangLabel, hangWord, shownWordHang, guessesHang, frameButtons, pixelHang, buttonsHang
   guessesHang=0 #sets guesses to 0

   for n in range(len(wordHang)): #creates the string that gets shown
      if n != 0: #any after the first
         if wordHang[n] == " ": #if it is a space
            shownWordHang = shownWordHang + "  " #puts in 2 spaces
         else:
            shownWordHang = shownWordHang + " _" #puts in a space and _
      else: #first one, no space before
         shownWordHang = "_"

   for widget in master.winfo_children():
      widget.destroy()

   pixelHang=((screenHeight-screenHeight//17)//14)

   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//17)
   frameTitle.grid(row = 0, column = 0, columnspan = 40, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//40), bg = "#000000", fg="#fff", text="Hangman").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = pixelHang*3)
   frameMenu.grid(row = 1, column = 1, columnspan = 40, rowspan = 3, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = pixelHang*3)
   frameHow.grid(row = 4, column = 1, columnspan = 40, rowspan = 3, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//17), bg = "#fff", command = lambda: HangMan()).pack(expand=True, fill="both")
   buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//17), bg = "#fff", command = lambda: howToPlayHang())
   buttonHow.pack(expand=True, fill="both")

   hangImg = [ImageTk.PhotoImage(Image.open("gameFiles/hangman0.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0))] #loads all of the hangman images in a list
   hangImg.append(ImageTk.PhotoImage(Image.open("gameFiles/hangman1.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0)))
   hangImg.append(ImageTk.PhotoImage(Image.open("gameFiles/hangman2.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0)))
   hangImg.append(ImageTk.PhotoImage(Image.open("gameFiles/hangman3.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0)))
   hangImg.append(ImageTk.PhotoImage(Image.open("gameFiles/hangman4.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0)))
   hangImg.append(ImageTk.PhotoImage(Image.open("gameFiles/hangman5.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0)))
   hangImg.append(ImageTk.PhotoImage(Image.open("gameFiles/hangman6.png").resize(((screenHeight-screenHeight//17), (screenHeight-screenHeight//4)), resample=0)))

   frameImg=tk.Frame(master, width = (screenHeight-screenHeight//17), height = (screenHeight-screenHeight//17))
   frameImg.grid(row = 1, column = 0, rowspan = 40, sticky = "we")
   frameImg.propagate(False)
   hangLabel = tk.Label(frameImg, image = hangImg[0], bg = "#000000", fg = "#fff", font = "Helvetica " + str((screenHeight-screenHeight//17)//25), text = shownWordHang, compound = "top") #image with the word uderneath
   hangLabel.pack(expand=True, fill="both")

   frameButtons=[]
   buttonsHang=[]

   for c in range(7): #this creates the grid of frames for letters
      frameButtons.append(tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17))//7, height = (screenWidth-(screenHeight-screenHeight//17))//7))
      frameButtons[c].grid(row = 7, column = 1+c, sticky = "we")
      frameButtons[c].propagate(False)
   for c in range(7): #it is many lines
      frameButtons.append(tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17))//7, height = (screenWidth-(screenHeight-screenHeight//17))//7))
      frameButtons[c+7].grid(row = 8, column = 1+(c%7), sticky = "we")
      frameButtons[c+7].propagate(False)
   for c in range(7): #it goes for 4 lines
      frameButtons.append(tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17))//7, height = (screenWidth-(screenHeight-screenHeight//17))//7))
      frameButtons[c+14].grid(row = 9, column = 1+(c%7), sticky = "we")
      frameButtons[c+14].propagate(False)
   for c in range(5): #with the 4th line the shortest
      frameButtons.append(tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17))//7, height = (screenWidth-(screenHeight-screenHeight//17))//7))
      frameButtons[c+21].grid(row = 10, column = 2+(c%7), sticky = "we")
      frameButtons[c+21].propagate(False)

   for t in range(26): #creates each button, each can be clicked to trigger that letter
      buttonsHang.append(tk.Button(frameButtons[t], bg = "#fff", bd = "3", font = "Helvetica " + str(((screenWidth-(screenHeight-screenHeight//17))//7)//5) , text = alphabet[t], command = lambda forCommand=[t]: letterHang(forCommand[0])))
      buttonsHang[t].pack(expand=True, fill="both")

def letterHang(letter): #when a letter is clicked
   buttonsHang[letter].config(state = "disabled", bg = "grey85") #disables button so it can not be clicked again
   global guessesHang, shownWordHang
   if alphabet[letter] in wordHang: #if the ltter is in the button
      spot=wordHang.index(alphabet[letter]) #finds that letter
      shownWordHang=shownWordHang[0:(spot*2)]+alphabet[letter]+shownWordHang[(spot*2+1):] #recreates shown word with letter filled in
      while alphabet[letter] in wordHang[spot+1:]: #while there is that letter repeating
         firstblank=shownWordHang[:(spot+1)] #first blank is before the 1st instance (used for counting)
         secondblank=shownWordHang[(spot+1):] #second blank is after the first letter (used to find next letter)
         firstblank=(firstblank+secondblank[:wordHang[(spot+1):].index(alphabet[letter])]) #first blank is recreated to g oright until next time that letter exists
         spot=len(firstblank) #marks where the letter is (simply all spots leading up to it)
         shownWordHang=shownWordHang[0:(spot*2)]+alphabet[letter]+shownWordHang[(spot*2+1):] #recrates shown word, it is *2 because of empty spaces between
         continue
      hangLabel.config(text = shownWordHang) #recreates label with new shown word
      gameWin = True
      for n in range(len(shownWordHang)): #for the length of the word
         if shownWordHang[n] == "_": #if a blank letter
            gameWin = False #the game is not over
      if gameWin == True: #if the game is over
         if soloHang == True:
            update(31, 1)
            buttonHow.config(text = "Play Again", command = lambda: singleHang()) #creates another single player game
         elif soloHang == False:
            buttonHow.config(text = "Play Again", command = lambda: multiHang()) #creates another multiplayer game
         for widget in frameButtons: #deletes all letters so they can not be clicked and mess thing sup (also to make more visually appealing)
            widget.destroy()
         frameWho=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = (screenHeight-screenHeight//17-pixelHang*6))
         frameWho.grid(row = 7, column = 1, columnspan = 20, sticky = "we")
         frameWho.propagate(False)
         turnLabelCon = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//10), fg="#fff", text="You Win!") #creates a winner message
         turnLabelCon.pack(expand=True, fill="both")
   else: #if the letter is not in the button
      guessesHang+=1 #adds 1 guess
      hangLabel.config(image = hangImg[guessesHang]) #changes image by 1
      if guessesHang == 6: #if the game is over
         if soloHang == True:
            update(32, 1)
            buttonHow.config(text = "Play Again", command = lambda: singleHang()) #creates play again
         elif soloHang == False:
            buttonHow.config(text = "Play Again", command = lambda: multiHang())
         for widget in frameButtons: #deletes the letters
            widget.destroy()
         frameWho=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = (screenHeight-screenHeight//17-pixelHang*6))
         frameWho.grid(row = 7, column = 1, rowspan = 20, columnspan = 20, sticky = "we")
         frameWho.propagate(False)
         turnLabelCon = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//15), fg="#fff", text="You lose.\n\nThe word was\n"+wordHang) #creates a loser message with the word
         turnLabelCon.pack(expand=True, fill="both")


#################################################################################################### HangMan end

#################################################################################################### BlackJack start

#Sam Gunter
#BlackJack was finished 9:54pm on the 13th of May, 2018
#This was created to play BlackJack (21) against a computer dealer
#Although this code deos not have all functions in real BlackJack, it can be played and that is what matters

#Next steps are to add time tracker and fix display

#BlackJack: Global variables and functions normally have a "21" at the end incase another game uses similar variables later on or earlier on.
#Starts with creating the board, this is actually a fairly slow block of code, but it makes good framework
#Then a loop of deal, hitting or standing and finally end screen

def BlackJack():
   global cardImg, hangImg, playerCard, dealerCard, middleLabel, deck21, buttonHow, buttonStand, buttonHit, sideButton
   for widget in master.winfo_children():
      widget.destroy()

   pixel21=((screenHeight-screenHeight//17)//12) #height of each text on side

   frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//17)
   frameTitle.grid(row = 0, column = 0, columnspan = 40, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//40), bg = "#000000", fg="#fff", text="BlackJack (21)").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = pixel21)
   frameMenu.grid(row = 1, column = 8, rowspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameHow=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = pixel21)
   frameHow.grid(row = 2, column = 8, rowspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//30), bg = "#fff", command = lambda: menu()).pack(expand=True, fill="both")
   buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//30), bg = "#fff", command = lambda: howToPlay21())
   buttonHow.pack(expand=True, fill="both")

   frameStand=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = pixel21*2)
   frameStand.grid(row = 3, column = 8, rowspan = 2, sticky = "we")
   frameStand.propagate(False)
   frameHit=tk.Frame(master, width = (screenWidth-(screenHeight-screenHeight//17)), height = pixel21*2)
   frameHit.grid(row = 5, column = 8, rowspan = 2, sticky = "we")
   frameHit.propagate(False)

   buttonStand = tk.Button(frameStand, state = "disabled", text = "Stand", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//17), bg = "#fff", command = lambda: stand21())
   buttonStand.pack(expand=True, fill="both")
   buttonHit = tk.Button(frameHit, state = "disabled", text = "Hit", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//17), bg = "#fff", command = lambda: hit21())
   buttonHit.pack(expand=True, fill="both")
   
   deck21=[]
   cardImg = {}
   for card in os.listdir("gameFiles\\CardDeck"): #this is all images in gameFiles
      deck21.append(card) #adds name to deck
      cardImg[card] = ImageTk.PhotoImage(Image.open("gameFiles\\CardDeck\\"+card).resize(((screenHeight-screenHeight//17)//8, (screenHeight-screenHeight//17)//4), resample=0)) #adds relative image to another list

   bigFrame=tk.Frame(master, bg = "#000000", width = screenHeight-screenHeight//17, height = screenHeight-screenHeight//17) #frame that holds the game (words are not in this frame)
   bigFrame.grid(row = 1, column = 0, rowspan = 12, sticky = "we")
   bigFrame.propagate(False)

   middleFrame=tk.Frame(bigFrame, width = screenHeight-screenHeight//17, height = ((screenHeight-screenHeight//17)//9)*4) #only here to stop propagation
   middleFrame.grid(row = 1, column = 0, columnspan = 1000, sticky = "we")
   middleFrame.propagate(False)
   middleLabel=tk.Label(middleFrame, bg = "#000000", fg = "#fff", font = "Helvetica " + str((screenHeight-screenHeight//17)//20))
   middleLabel.pack(expand=True, fill="both")
   sideFrame=tk.Frame(middleFrame, pady = "100", bg = "#000000", width = (screenHeight-screenHeight//17)//3, height = ((screenHeight-screenHeight//17)//9)*4)
   sideFrame.grid(row = 0, column = 0, sticky = "we")
   sideFrame.propagate(False)
   sideButton=tk.Button(sideFrame, text = "Deal Again", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//25), bg = "#fff", command = lambda: deal21())
   sideButton.pack(expand=True, fill="both")

   framePlayer=[]
   frameDealer=[] #top cards
   playerCard=[]
   dealerCard=[] #bottom cards

   for c in range(8):
      frameDealer.append(tk.Frame(bigFrame, width = (screenHeight-screenHeight//17)//8, height = (screenHeight-screenHeight//17)//4)) #8 of these cards side by side
      frameDealer[c].grid(row = 0, column = c, columnspan = 1, padx = 3, sticky = "we")
      frameDealer[c].propagate(False)
      framePlayer.append(tk.Frame(bigFrame, width = (screenHeight-screenHeight//17)//8, height = (screenHeight-screenHeight//17)//4))
      framePlayer[c].grid(row = 2, column = c, columnspan = 1, padx = 3, sticky = "we")
      framePlayer[c].propagate(False)
      dealerCard.append(tk.Label(frameDealer[c], bg = "#000000", fg = "#fff"))
      dealerCard[c].pack(expand=True, fill="both")
      playerCard.append(tk.Label(framePlayer[c], bg = "#000000", fg = "#fff"))
      playerCard[c].pack(expand=True, fill="both")

   deal21() #first deal of the game

def howToPlay21():
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="BlackJack (21)").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", font = "Helvetica " + str(screenHeight//40), bg = "#fff", command = lambda: BlackJack()).pack(expand=True, fill="both")

   frameHang1=tk.Frame(master, width = screenWidth, height = screenHeight/3)
   frameHang1.grid(row=1, columnspan=2, sticky="nsew")
   frameHang1.propagate(False)
   frameHang2=tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10))
   frameHang2.grid(row=2, columnspan=2, sticky="nsew")
   frameHang2.propagate(False)

   tk.Label(frameHang1, bg = "white smoke", font = "Helvetica " + str(screenHeight//37) + " bold", text="""

Program specific instructions

1. Click deal to deal out new cards
2. Click Stand once you are done getting cards
3. Click hit to get antoher card""").pack(expand=True, fill="both")

   tk.Label(frameHang2, bg = "white smoke", font = "Helvetica " + str(screenHeight//55), text="""Rules to Game:

The standard 52-card pack is used.
The player attempts to beat the dealer by getting a count as close to 21 as possible, without going over 21.
All face cards are 10 and any other card is its face value, with aces being an 11 or a 1 (whichever is better for you).
The combination of an ace with a card other than a ten-card is known as a "soft hand,"
because the player can count the ace as a 1 or 11, and either draw cards or not.
For example with a "soft 17" (an ace and a 6), the total is 7 or 17.

The player receives two cards face up, and the dealer receives one card face up and one card face down.
If the player's first two cards are an ace and a 10, giving him a count of 21 in two cards, the player wins by default.
The player may stand on the two cards originally dealt him, or he may ask the dealer for additional cards (hit),
until he either decides to stand on the total or goes "bust" (over 21).

Once the player has stood, the dealer turns up his card. If the total is a soft 17 or under,
he must draw until the total is 17 or more, at which point the dealer must stand. If the dealer has an ace,
and counting it as 11 would bring his total more than 17 (but not over 21), he must count the ace as 11 and stand. 
""").pack(expand=True, fill="both")

def deal21():
   global dealer21, player21, playerCard, dealerCard, hidden21, currentDeck21, buttonHow, middleLabel, buttonStand, buttonHit, sideButton

   for c in range(8): #these next few things only matter after first time
      dealerCard[c].config(image = "") #deletes any cards already there
      playerCard[c].config(image = "")
   sideButton.config(state = "disabled") #cant deal until done
   middleLabel.config(text = "") #takes out win or lose message
   currentDeck21 = deck21[:] #creates a new deck
   currentDeck21.remove("back.png") #removes the back or blank card
   dealer21 = [] #resets dealers and players hands
   player21 = []

   choice = random.randint(0, len(currentDeck21)-1) #random card in deck
   player21.append(currentDeck21[choice]) #add to players hand
   playerCard[3].config(image = cardImg[currentDeck21[choice]]) #add image
   del currentDeck21[choice] #take it out of the deck
   master.update()
   time.sleep(.3) #natural delay

   choice = random.randint(0, len(currentDeck21)-1) #saem as above but for dealer
   dealer21.append(currentDeck21[choice])
   dealerCard[3].config(image = cardImg["back.png"]) #blank instead of shown because dealer
   hidden21=currentDeck21[choice]
   del currentDeck21[choice]
   master.update()
   time.sleep(.3)

   choice = random.randint(0, len(currentDeck21)-1)
   player21.append(currentDeck21[choice])
   playerCard[4].config(image = cardImg[currentDeck21[choice]])
   del currentDeck21[choice]
   master.update()
   time.sleep(.3)

   choice = random.randint(0, len(currentDeck21)-1)
   dealer21.append(currentDeck21[choice])
   dealerCard[4].config(image = cardImg[currentDeck21[choice]])
   del currentDeck21[choice]

   buttonStand.config(state = "normal") #now the user can click these buttons
   buttonHit.config(state = "normal")

   playerSum=0 #this is to check is player has a natural black jack
   for card in player21: #for cards in hand
      try:
         check=int(card[:2]) #this is to trigger except if its not double digits
         playerSum+=10 #if double digits, add 10
      except ValueError:
         if int(card[:1]) == 1: #if it is an ace
            playerSum+=11 #add 11
         else: #else
            playerSum+= int(card[:1]) #add what ever it is
   if playerSum == 21: #if a natural
      end21("win") #end game with a win

def stand21(): #if the players stands
   global dealer21, buttonHow, middleLabel, currentDeck21
   
   playerSum=0 #checks players hand
   for card in player21: #this gets sum with aces as 11
      try:
         check=int(card[:2])
         playerSum+=10
      except ValueError:
         if int(card[:1]) == 1:
            playerSum+=11
         else:
            playerSum+= int(card[:1])
   aceCheck=0 #sets where to check aces
   while True:
      if playerSum > 21: #if over 21 (else no need to do this)
         for card in player21[aceCheck:]: #for every card not yet checked
            aceCheck+=1 #says that this has now been checked
            if card[:2] == "1-": #if an ace
               playerSum = playerSum - 10 #switches to a 1
               break #break current loop to check if still over 21
      else: #else end
         break
   
   dealerCard[3].config(image = cardImg[hidden21]) #turns up dealers card
   master.update()
   time.sleep(.4)
   dealerSum=0 #counts dealers cards
   for card in dealer21: #saem as for player, but for dealer
      try:
         check=int(card[:2])
         dealerSum+=10
      except ValueError:
         if int(card[:1]) == 1:
            dealerSum+=11
         else:
            dealerSum+= int(card[:1])
   aceCheck=0
   while True:
      if dealerSum < 17: #if under 17
         choice = random.randint(0, len(currentDeck21)-1) #add new card, run again
         dealer21.append(currentDeck21[choice])

         try:
            check=int(currentDeck21[choice][:2])
            dealerSum+=10
         except ValueError:
            if int(currentDeck21[choice][:1]) == 1:
               dealerSum+=11
            else:
               dealerSum+= int(currentDeck21[choice][:1])

         spot = (8-len(dealer21))//2 #this centers the cards
         for cards in dealer21:
            dealerCard[spot].config(image = cardImg[cards]) #creates all cards in new places
            spot+=1
         del currentDeck21[choice]
         
      elif dealerSum == 17 or dealerSum > 21: #if over 21, or soft 17
         end = True
         for card in dealer21[aceCheck:]:
            aceCheck+=1
            if card[:2] == "1-": #changes an ace to a 1, then runs again
               end = False
               dealerSum = dealerSum - 10
               break
         if end == True: #if no aces, that means out of hard 17, end
            break

      else: #between 17 and 21, end
         break

      master.update()
      time.sleep(.4)

   if playerSum <= dealerSum and dealerSum <= 21: #checks who has won
      end21("lose") #dealer
   else:
      end21("win") #player

def hit21():
   global currentDeck21, player21
   
   choice = random.randint(0, len(currentDeck21)-1) #players new card
   player21.append(currentDeck21[choice])

   spot = (8-len(player21))//2 #recenters players cards
   for cards in player21:
      playerCard[spot].config(image = cardImg[cards])
      spot+=1
   del currentDeck21[choice]

   playerSum=0 #next 2 blocks of code check for if game is over
   for card in player21:
      try:
         check=int(card[:2])
         playerSum+=10
      except ValueError:
         if int(card[:1]) == 1:
            playerSum+=11
         else:
            playerSum+= int(card[:1])

   aceCheck=0
   while True:
      if playerSum > 21:
         end = True
         for card in player21[aceCheck:]:
            aceCheck+=1
            if card[:2] == "1-":
               end = False
               playerSum = playerSum - 10
               break
         if end == True: #if they went over
            end21("lose") #they lose
            break
      else:
         break

   if playerSum == 21: #if a perfect blackjack
      end21("win") #they win

def end21(result):
   global buttonStand, buttonHit, sideButton
   if result == "lose": #if they lost
      update(35, 1)
      middleLabel.config(text = "You lose.") #lose message
   else: #else
      update(34, 1)
      middleLabel.config(text = "You Win!") #win message

   sideButton.config(state = "normal") 
   buttonStand.config(state = "disabled") #disables all buttons until a new deal is made
   buttonHit.config(state = "disabled")


#################################################################################################### BlackJack end

#################################################################################################### Checkers start

#Sam Gunter
#Checkers was finished 2:05am on the 31st of May, 2018.
#This was created to play checkers either multiplayer or against AI.
#The AI has been the biggest struggle of this game, it is seriously insane how much work I have done to make a AI that always loses.

#Next step is to add leaderboards (once got a slight error in single move AI (down-right near beginning), but have not been able to trigger it again).

#Checkers: Global variables and functions normally have a "Chec" at the end incase another game uses similar variables later on or earlier on.
#Starts with user picking single or multi, then creates board values, finally loads the board.
#When user clicks a spot, it is set as base. Next click is checked for if it works. Then switches to other person (multi) or to AI.
#AI looks for where pieces are, then single moves (checks for best ones), then jumps (checks for best one), then plays the move.

def Checkers():
   global oneChec #this will make game single player or multiplayer
   oneChec = False #preset to multiplayer
   for widget in master.winfo_children():
      widget.destroy()

   frameSin=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameSin.grid(row = 1, column = 0, columnspan = 3, sticky = "we")
   frameSin.propagate(False)
   frameMul=tk.Frame(master, width = screenWidth//2, height = screenHeight//4)
   frameMul.grid(row = 1, column = 3, columnspan = 3, sticky = "we")
   frameMul.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "How To Play", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: howToPlayChec()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: menu()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Checkers").pack(expand=True, fill="both")
   tk.Button(frameSin, text = "Singleplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: singleChec()).pack(expand=True, fill="both")
   tk.Button(frameMul, text = "Multiplayer", bg = "#fff", font = "Helvetica " + str(screenHeight//20), command = lambda: newGameChec()).pack(expand=True, fill="both")

def singleChec():
   global oneChec
   oneChec = True #if singleplayer was chosen, sets to singleplayer
   newGameChec()

def howToPlayChec():
   for widget in master.winfo_children():
      widget.destroy()

   frameTitle=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 0, sticky = "we")
   frameTitle.propagate(False)
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Checkers").pack(expand=True, fill="both")

   frameMenu=tk.Frame(master, width = screenWidth//2, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 1, sticky = "we")
   frameMenu.propagate(False)
   tk.Button(frameMenu, text = "Back", bg = "#fff", font = "Helvetica " + str(screenHeight//40), command = lambda: loadBoardChec()).pack(expand=True, fill="both")

   frameSu1=tk.Frame(master, width = screenWidth, height = screenHeight/3)
   frameSu1.grid(row=1, columnspan=2, sticky="nsew")
   frameSu1.propagate(False)
   frameSu2=tk.Frame(master, width = screenWidth, height = screenHeight-(screenHeight/3 + screenHeight//10))
   frameSu2.grid(row=2, columnspan=2, sticky="nsew")
   frameSu2.propagate(False)

   tk.Label(frameSu1, bg = "white smoke", font = "Helvetica " + str(screenHeight//40) + " bold", text="""

Program specific instructions

1. Click on the checker you want to move, then click here to move it.
2. Checkers automatically are taken off the board, and crowned at the end of the board.
3. If a second jump is available, then the game will automatically take it.""").pack(expand=True, fill="both")

   tk.Label(frameSu2, bg = "white smoke", font = "Helvetica " + str(screenHeight//55), text="""Rules to Game:

Checkers is played on a standard 64 square board. Only the 32 dark colored squares are used in play.
Each player begins the game with 12 pieces, or checkers, placed in the three rows closest to them. 
The object of the game is to capture all of the opponent’s checkers or position your pieces so that your opponent has no available moves. 

A checker can be moved one space diagonally forward. You can not move a checker backwards until it becomes a King, as described below.
If one of your opponent’s checkers is on a forward diagonal next to one of your checkers, and the next space beyond the opponent’s checker is empty,
then your checker can jump the opponent’s checker and land in the space beyond. Your opponent’s checker is captured and removed from the board. 

After making one jump, your checker might have another jump available from its new position. Your checker must take that jump too.
It must continue to jump until there are no more jumps available.

When one of your checkers reaches the opposite side of the board, it is crowned and becomes a King.
A King can move backward as well as forward along the diagonals, instead of just forward.""").pack(expand=True, fill="both")

def newGameChec():
   global locationChec, turnChec
   turnChec = "red" #makes red go first
   locationChec = [[]] #this keeps track of which piece is where
   for r in range(8):
      if len(locationChec)==r:
            locationChec.append([])
      for c in range(8):
         if r < 3 and (c + r) % 2 == 1:
            locationChec[r].append("black") #makes the black pieces
         elif r > 4 and (c + r) % 2 == 1:
            locationChec[r].append("red") #the red pieces
         elif (c + r) % 2 == 1:
            locationChec[r].append(" ") #an empty space
         else:
            locationChec[r].append("") #nothing can fill these spaces (light boxes)
   loadBoardChec()

def loadBoardChec():
   try: #this try is in place for the how to play to not reset the game
      global pixelChec, buttonsChec, frameChec, errorChec, buttonHow, spotChec, locationChec, redImgChec, blackImgChec, kingRedImgChec, kingBlackImgChec, baseChec
      baseChec = [-1, -1] #this will later keep track of the piece in play
      
      for widget in master.winfo_children():
         widget.destroy()
      pixelChec=((screenHeight-screenHeight//17)//8)

      redImgChec = ImageTk.PhotoImage(Image.open("gameFiles/redChec.png").resize((pixelChec-pixelChec//10, pixelChec-pixelChec//10), resample=0))
      blackImgChec = ImageTk.PhotoImage(Image.open("gameFiles/blackChec.png").resize((pixelChec-pixelChec//10, pixelChec-pixelChec//10), resample=0))
      kingRedImgChec = ImageTk.PhotoImage(Image.open("gameFiles/redChecKing.png").resize((pixelChec-pixelChec//10, pixelChec-pixelChec//10), resample=0))
      kingBlackImgChec = ImageTk.PhotoImage(Image.open("gameFiles/blackChecKing.png").resize((pixelChec-pixelChec//10, pixelChec-pixelChec//10), resample=0))

      frameTitle=tk.Frame(master, width = screenWidth, height = screenHeight//17)
      frameTitle.grid(row = 0, column = 0, columnspan = 20, sticky = "we")
      frameTitle.propagate(False)
      tk.Label(frameTitle, font = "fixedsys " + str(screenHeight//40), bg = "#000000", fg="#fff", text="Checkers").pack(expand=True, fill="both")

      frameMenu=tk.Frame(master, width = (screenWidth-(pixelChec*8)), height = pixelChec*2)
      frameMenu.grid(row = 1, column = 10, rowspan = 2, sticky = "we")
      frameMenu.propagate(False)
      frameHow=tk.Frame(master, width = (screenWidth-(pixelChec*8)), height = pixelChec*2)
      frameHow.grid(row = 3, column = 10, rowspan = 2, sticky = "we")
      frameHow.propagate(False)
      frameWho=tk.Frame(master, width = (screenWidth-(pixelChec*8)), height = pixelChec*4)
      frameWho.grid(row = 5, column = 10, rowspan = 10, sticky = "we")
      frameWho.propagate(False)

      tk.Button(frameMenu, text = "Menu", font = "Helvetica " + str((screenWidth-(pixelChec*8))//17), bg = "#fff", command = lambda: Checkers()).pack(expand=True, fill="both")
      buttonHow = tk.Button(frameHow, text = "How To Play", font = "Helvetica " + str((screenWidth-(pixelChec*8))//17), bg = "#fff", command = lambda: howToPlayChec())
      buttonHow.pack(expand=True, fill="both")
      errorChec = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(pixelChec*8))//12), fg="#fff", text="")
      errorChec.pack(expand=True, fill="both")

      spotChec=[[]] #keeps track of images
      frameChec=[[]]
      buttonsChec=[[]] #each button
      for r in range(8):
         if len(buttonsChec)==r:
            buttonsChec.append([])
            frameChec.append([])
            spotChec.append([])
         for c in range(8):
            if locationChec[r][c] == "red": #if red
               spotChec[r].append(redImgChec) #red image
            elif locationChec[r][c] == "black": #if black
               spotChec[r].append(blackImgChec) #black image
            elif locationChec[r][c] == "redKing": #etc
               spotChec[r].append(kingRedImgChec)
            elif locationChec[r][c] == "blackKing": #etc
               spotChec[r].append(kingBlackImgChec)
            else:
               spotChec[r].append("") #else, no image
            frameChec[r].append(tk.Frame(master, width = pixelChec, height = pixelChec, borderwidth = "0"))
            frameChec[r][c].grid(row=r+1, column=c, sticky="nsew")
            frameChec[r][c].propagate(False)
            if (r+c) % 2 == 1:
               buttonsChec[r].append(tk.Button(frameChec[r][c], overrelief = "groove", image = spotChec[r][c], relief = 'flat', activebackground = "LightSalmon3", bg = "LightSalmon4", borderwidth = "4", command = lambda forCommand=[r, c]: clickChec(forCommand[0], forCommand[1]))) #creates dark buttons with image
            elif (r+c) % 2 == 0:
               buttonsChec[r].append(tk.Label(frameChec[r][c], bg = "bisque", bd= '0')) #creates light labels always blank
            buttonsChec[r][c].pack(expand=True, fill="both")
   except NameError: #if how to play is ended with no game started
      Checkers() #main menu

def clickChec(row, column):
   global errorChec, baseChec, buttonsChec, turnChec
   if (locationChec[row][column] == turnChec or locationChec[row][column] == (turnChec+"King")) and baseChec[0] < 0: #if the right color and no base yet
      errorChec.config(text = "")
      buttonsChec[row][column].config(bg = "LightSalmon3")
      baseChec = [row, column] #makes it the base
   elif baseChec[0] < 0: #if wrong colours and no base
      errorChec.config(text = "It is "+turnChec+"'s turn.") #error message
   else: #if there is already a base
      #single move
      if locationChec[row][column] == " " and (((locationChec[baseChec[0]][baseChec[1]] == "red" or locationChec[baseChec[0]][baseChec[1]][-4:] == "King") and #if click is empty and the base is red (move up) or a king (move anywhere)
               row == baseChec[0] - 1 and (column == baseChec[1] - 1 or column == baseChec[1] + 1)) #and the difference is left or right up
            or ((locationChec[baseChec[0]][baseChec[1]] == "black" or locationChec[baseChec[0]][baseChec[1]][-4:] == "King") and #OR, if click is empty and the base is red (move up) or a king (move anywhere)
               row == baseChec[0] + 1 and (column == baseChec[1] - 1 or column == baseChec[1] + 1))): #and the difference is left or right up
         locationChec[row][column] = locationChec[baseChec[0]][baseChec[1]] #sets the new spot as old spot value
         locationChec[baseChec[0]][baseChec[1]] = " " #old spot as nothing
         reloadChec(baseChec[0], baseChec[1]) #reloads old
         reloadChec(row, column) #reloads new
         baseChec = [-1, -1]
         if turnChec == "red": #changes whos turn it is
            turnChec = "black"
         else:
            turnChec = "red"
            
      #jumping over
      elif locationChec[row][column] == " " and ((locationChec[baseChec[0]][baseChec[1]][:3] == "red" and
               (row == baseChec[0] - 2 or locationChec[baseChec[0]][baseChec[1]] == "redKing") and (column == baseChec[1] + 2 or column == baseChec[1] - 2) and
               locationChec[(baseChec[0]+row)//2][(baseChec[1]+column)//2][:5] == "black")
            or (locationChec[baseChec[0]][baseChec[1]][:5] == "black" and
               (row == baseChec[0] + 2 or locationChec[baseChec[0]][baseChec[1]] == "blackKing") and (column == baseChec[1] + 2 or column == baseChec[1] - 2) and
               locationChec[(baseChec[0]+row)//2][(baseChec[1]+column)//2][:3] == "red")):
         
         locationChec[row][column] = locationChec[baseChec[0]][baseChec[1]] #sets the new spot as old spot value
         locationChec[(baseChec[0]+row)//2][(baseChec[1]+column)//2] = " " #middle spot as nothing
         locationChec[baseChec[0]][baseChec[1]] = " " #old as nothing
         reloadChec(baseChec[0], baseChec[1]) #reloads old
         reloadChec(row, column) #reloads new
         time.sleep(.2) #pause
         reloadChec((baseChec[0]+row)//2, (baseChec[1]+column)//2) #reloads middle
         baseChec = [-1, -1]

         if turnChec == "red": #changes whos turn it is
            turnChec = "black"
         else:
            turnChec = "red"

         currentSpot = (row, column) #this is used in the while loop
         while True: #loop is used to check for any extra jumps
           
            if currentSpot[0]+2 < 8 and currentSpot[1]+2 < 8: #if its not going too far down or right
               if (locationChec[currentSpot[0]+2][currentSpot[1]+2] == " " and #if down-right is empty
                     (locationChec[currentSpot[0]][currentSpot[1]] == "black" or locationChec[currentSpot[0]][currentSpot[1]][-4:] == "King") and #and a black (down) or a king (all)
                     locationChec[currentSpot[0]+1][currentSpot[1]+1][:3] == turnChec[:3]): #and middle has a variant of opposition
                  locationChec[currentSpot[0]+2][currentSpot[1]+2] = locationChec[currentSpot[0]][currentSpot[1]] #same as above updating from jump
                  locationChec[currentSpot[0]+1][currentSpot[1]+1] = " "
                  locationChec[currentSpot[0]][currentSpot[1]] = " "
                  time.sleep(.2)
                  reloadChec(currentSpot[0]+2, currentSpot[1]+2)
                  reloadChec(currentSpot[0], currentSpot[1])
                  time.sleep(.2)
                  reloadChec(currentSpot[0]+1, currentSpot[1]+1)
                  currentSpot = (currentSpot[0]+2, currentSpot[1]+2) #sets new currentSpot
                  continue #goes back to loop (to stop from hitting break)

            if currentSpot[0]-2 > -1 and currentSpot[1]+2 < 8: #if its not going too far up or right
               if (locationChec[currentSpot[0]-2][currentSpot[1]+2] == " " and #if up-right is empty
                     (locationChec[currentSpot[0]][currentSpot[1]] == "red" or locationChec[currentSpot[0]][currentSpot[1]][-4:] == "King") and #and a red (up) or a king (all)
                     locationChec[currentSpot[0]-1][currentSpot[1]+1][:3] == turnChec[:3]): #and middle has a variant of opposition
                  locationChec[currentSpot[0]-2][currentSpot[1]+2] = locationChec[currentSpot[0]][currentSpot[1]] #rest is same as above
                  locationChec[currentSpot[0]-1][currentSpot[1]+1] = " "
                  locationChec[currentSpot[0]][currentSpot[1]] = " "
                  time.sleep(.2)
                  reloadChec(currentSpot[0]-2, currentSpot[1]+2)
                  reloadChec(currentSpot[0], currentSpot[1])
                  time.sleep(.2)
                  reloadChec(currentSpot[0]-1, currentSpot[1]+1)
                  currentSpot = (currentSpot[0]-2, currentSpot[1]+2)
                  continue

            if currentSpot[0]+2 < 8 and currentSpot[1]-2 > -1: #if its not going too far down or left
               if (locationChec[currentSpot[0]+2][currentSpot[1]-2] == " " and #if down-left is empty
                     (locationChec[currentSpot[0]][currentSpot[1]] == "black" or locationChec[currentSpot[0]][currentSpot[1]][-4:] == "King") and #and a black (down) or a king (all)
                     locationChec[currentSpot[0]+1][currentSpot[1]-1][:3] == turnChec[:3]): #and middle has a variant of opposition
                  locationChec[currentSpot[0]+2][currentSpot[1]-2] = locationChec[currentSpot[0]][currentSpot[1]]
                  locationChec[currentSpot[0]+1][currentSpot[1]-1] = " "
                  locationChec[currentSpot[0]][currentSpot[1]] = " "
                  time.sleep(.2)
                  reloadChec(currentSpot[0]+2, currentSpot[1]-2)
                  reloadChec(currentSpot[0], currentSpot[1])
                  time.sleep(.2)
                  reloadChec(currentSpot[0]+1, currentSpot[1]-1)
                  currentSpot = (currentSpot[0]+2, currentSpot[1]-2)
                  continue

            if currentSpot[0]-2 > -1 and currentSpot[1]-2 > -1: #if its not going too far up or left
               if (locationChec[currentSpot[0]-2][currentSpot[1]-2] == " " and #if up-left is empty
                     (locationChec[currentSpot[0]][currentSpot[1]] == "red" or locationChec[currentSpot[0]][currentSpot[1]][-4:] == "King") and #and a red (up) or a king (all)
                     locationChec[currentSpot[0]-1][currentSpot[1]-1][:3] == turnChec[:3]): #and middle has a variant of opposition
                  locationChec[currentSpot[0]-2][currentSpot[1]-2] = locationChec[currentSpot[0]][currentSpot[1]]
                  locationChec[currentSpot[0]-1][currentSpot[1]-1] = " "
                  locationChec[currentSpot[0]][currentSpot[1]] = " "
                  time.sleep(.2)
                  reloadChec(currentSpot[0]-2, currentSpot[1]-2)
                  reloadChec(currentSpot[0], currentSpot[1])
                  time.sleep(.2)
                  reloadChec(currentSpot[0]-1, currentSpot[1]-1)
                  currentSpot = (currentSpot[0]-2, currentSpot[1]-2)
                  continue
               
            break #end the loop
            
      elif row == baseChec[0] and column == baseChec[1]: #if clicked the base
         reloadChec(baseChec[0], baseChec[1]) #reloads the base
         baseChec = [-1, -1] #unclicks the base
         
      else:
         errorChec.config(text = "You cannot\nmove there.") #if a spot that is not in any of the above
         reloadChec(baseChec[0], baseChec[1]) #gets rid of base
         baseChec = [-1, -1] #unclicks the base

   blackEnd = True #checks for end game (black)
   for r in range(8):
      for c in range(8):
         if locationChec[r][c] == "black" or locationChec[r][c] == "blackKing": #if any black left
            blackEnd = False #no end
   if blackEnd == True: #if no black, red wins
      if oneChec == True:
         update(37, 1)
      errorChec.config(text = "Red wins!")
      buttonHow.config(text = "Play Again", command = lambda: newGameChec())
   else: #if red did not win
      if oneChec == True and turnChec == "black": #if single player
         aiChec() #trigger AI
         turnChec = "red" #changes to red
         
      redEnd = True #the checks for red
      for r in range(8):
         for c in range(8):
            if locationChec[r][c] == "red" or locationChec[r][c] == "redKing": #if any red left
               redEnd = False #no end
      if redEnd == True: #if black won
         if oneChec == True:
            update(38, 1)
         errorChec.config(text = "Black wins!")
         buttonHow.config(text = "Play Again", command = lambda: newGameChec())

def aiChec(): #this function does the play for AI
   global errorChec, buttonHow, locationChec
   
   blackSpots = [] #this is  alist of all black pieces
   for r in range(8):
      for c in range(8):
         if locationChec[r][c][:5] == "black": #if a black piece
            blackSpots.append(str(r)+str(c)) #add to the list (in a string)
   
   singleSpots = [] #checks for any single moves
   for checkers in blackSpots: #for every black piece
      if int(checkers[0]) < 7 and int(checkers[1]) < 7:
         if locationChec[int(checkers[0])+1][int(checkers[1])+1] == " ": #checks down right
            singleSpots.append(checkers+str(int(checkers[0])+1)+str(int(checkers[1])+1))
      if int(checkers[0]) < 7 and int(checkers[1]) > 0:
         if locationChec[int(checkers[0])+1][int(checkers[1])-1] == " ": #checks down left
            singleSpots.append(checkers+str(int(checkers[0])+1)+str(int(checkers[1])-1))
      if int(checkers[0]) > 0 and int(checkers[1]) < 7 and locationChec[int(checkers[0])][int(checkers[1])] == "blackKing": #if king
         if locationChec[int(checkers[0])-1][int(checkers[1])+1] == " ": #checks up right
            singleSpots.append(checkers+str(int(checkers[0])-1)+str(int(checkers[1])+1))
      if int(checkers[0]) > 0 and int(checkers[1]) > 0 and locationChec[int(checkers[0])][int(checkers[1])] == "blackKing": #if king
         if locationChec[int(checkers[0])-1][int(checkers[1])-1] == " ": #checks up left
            singleSpots.append(checkers+str(int(checkers[0])-1)+str(int(checkers[1])-1))

   betterSpots = [] #checks for spots where the black spots wont be destroyed
   for checkers in singleSpots:
      if int(checkers[2]) < 7 and int(checkers[3]) < 7 and int(checkers[2]) > 0 and int(checkers[3]) > 0: #checks if not touching a wall
         if ((locationChec[int(checkers[2])+1][int(checkers[3])+1][:3] == "red" and (locationChec[int(checkers[2])-1][int(checkers[3])-1] == " " or #if can be jumped up-down, right-left
                  (int(checkers[2])-1 == int(checkers[0]) and int(checkers[3])-1 == int(checkers[1])))) or
               (locationChec[int(checkers[2])-1][int(checkers[3])-1] == "redKing" and (locationChec[int(checkers[2])+1][int(checkers[3])+1] == " " or #or can be jumped down-up, left-right
                  (int(checkers[2])+1 == int(checkers[0]) and int(checkers[3])+1 == int(checkers[1])))) or
               (locationChec[int(checkers[2])-1][int(checkers[3])+1] == "redKing" and (locationChec[int(checkers[2])+1][int(checkers[3])-1] == " " or #or can be jumped down-up, right-left
                  (int(checkers[2])+1 == int(checkers[0]) and int(checkers[3])-1 == int(checkers[1])))) or
               (locationChec[int(checkers[2])+1][int(checkers[3])-1][:3] == "red" and (locationChec[int(checkers[2])-1][int(checkers[3])+1] == " " or #or can be jumped up-down, left-right
                  (int(checkers[2])-1 == int(checkers[0]) and int(checkers[3])+1 == int(checkers[1]))))):
            break #if any of these are True, do not add this one
      betterSpots.append(checkers) #else, add it to the list
   if False == (betterSpots == []): #if the list isnt empty
      singleSpots = betterSpots [:] #replace the singleSpots

   jumpSpots = [] #checks for any places where a piece can be taken
   for checkers in blackSpots: #goes through all black spots
      if int(checkers[0]) < 6 and int(checkers[1]) < 6:
         if locationChec[int(checkers[0])+2][int(checkers[1])+2] == " " and (locationChec[int(checkers[0])+1][int(checkers[1])+1] == "red" or locationChec[int(checkers[0])+1][int(checkers[1])+1] == "redKing"):
            jumpSpots.append(checkers+str(int(checkers[0])+2)+str(int(checkers[1])+2)) #add the jump (4 letter string) to the list
      if int(checkers[0]) < 6 and int(checkers[1]) > 1:
         if locationChec[int(checkers[0])+2][int(checkers[1])-2] == " " and (locationChec[int(checkers[0])+1][int(checkers[1])-1] == "red" or locationChec[int(checkers[0])+1][int(checkers[1])-1] == "redKing"):
            jumpSpots.append(checkers+str(int(checkers[0])+2)+str(int(checkers[1])-2))
      if int(checkers[0]) > 1 and int(checkers[1]) < 6 and locationChec[int(checkers[0])][int(checkers[1])] == "blackKing":
         if locationChec[int(checkers[0])-2][int(checkers[1])+2] == " " and (locationChec[int(checkers[0])-1][int(checkers[1])+1] == "red" or locationChec[int(checkers[0])-1][int(checkers[1])+1] == "redKing"):
            jumpSpots.append(checkers+str(int(checkers[0])-2)+str(int(checkers[1])+2))
      if int(checkers[0]) > 1 and int(checkers[1]) > 1 and locationChec[int(checkers[0])][int(checkers[1])] == "blackKing":
         if locationChec[int(checkers[0])-2][int(checkers[1])-2] == " " and (locationChec[int(checkers[0])-1][int(checkers[1])-1] == "red" or locationChec[int(checkers[0])-1][int(checkers[1])-1] == "redKing"):
            jumpSpots.append(checkers+str(int(checkers[0])-2)+str(int(checkers[1])-2))

   for checkers in jumpSpots: #for all possible 1 knockout jumps, checks for any more possible
      if int(checkers[2]) < 6 and int(checkers[3]) < 6:
         if locationChec[int(checkers[2])+2][int(checkers[3])+2] == " " and (locationChec[int(checkers[2])+1][int(checkers[3])+1] == "red" or locationChec[int(checkers[2])+1][int(checkers[3])+1] == "redKing"):
            if len(jumpSpots[0]) == 4: #if currently only single jumps
               jumpSpots = [] #reset all jumps
            jumpSpots.append(checkers+str(int(checkers[2])+2)+str(int(checkers[3])+2)) #add this double jump (letter string)
      if int(checkers[2]) < 6 and int(checkers[3]) > 1:
         if locationChec[int(checkers[2])+2][int(checkers[3])-2] == " " and (locationChec[int(checkers[2])+1][int(checkers[3])-1] == "red" or locationChec[int(checkers[2])+1][int(checkers[3])-1] == "redKing"):
            if len(jumpSpots[0]) == 4:
               jumpSpots = []
            jumpSpots.append(checkers+str(int(checkers[2])+2)+str(int(checkers[3])-2))
      if int(checkers[2]) > 1 and int(checkers[3]) < 6 and locationChec[int(checkers[0])][int(checkers[3])] == "blackKing":
         if locationChec[int(checkers[2])-2][int(checkers[3])+2] == " " and (locationChec[int(checkers[2])-1][int(checkers[3])+1] == "red" or locationChec[int(checkers[2])-1][int(checkers[3])+1] == "redKing"):
            if len(jumpSpots[0]) == 4:
               jumpSpots = []
            jumpSpots.append(checkers+str(int(checkers[2])-2)+str(int(checkers[3])+2))
      if int(checkers[2]) > 1 and int(checkers[3]) > 1 and locationChec[int(checkers[2])][int(checkers[3])] == "blackKing":
         if locationChec[int(checkers[2])-2][int(checkers[3])-2] == " " and (locationChec[int(checkers[2])-1][int(checkers[3])-1] == "red" or locationChec[int(checkers[2])-1][int(checkers[3])-1] == "redKing"):
            if len(jumpSpots[0]) == 4:
               jumpSpots = []
            jumpSpots.append(checkers+str(int(checkers[2])-2)+str(int(checkers[3])-2))
            
   betterSpots = [] #checks for better jump (or double jump) spots
   for checkers in jumpSpots:
      if int(checkers[2]) < 7 and int(checkers[3]) < 7 and int(checkers[2]) > 0 and int(checkers[3]) > 0: #same as above code, but...
         if ((locationChec[int(checkers[2])+1][int(checkers[3])+1][:3] == "red" and (locationChec[int(checkers[2])-1][int(checkers[3])-1] == " " or
                  (int(checkers[2])-1 == (int(checkers[0])+int(checkers[2]))//2 and int(checkers[3])-1 == (int(checkers[1])+int(checkers[3]))//2))) or #checks for middle of start and end, nstead of just start
               (locationChec[int(checkers[2])-1][int(checkers[3])-1] == "redKing" and (locationChec[int(checkers[2])+1][int(checkers[3])+1] == " " or #because now jumping (2 moves) instead of just sliding (1 spot)
                  (int(checkers[2])+1 == (int(checkers[0])+int(checkers[2]))//2 and int(checkers[3])+1 == (int(checkers[1])+int(checkers[3]))//2))) or
               (locationChec[int(checkers[2])-1][int(checkers[3])+1] == "redKing" and (locationChec[int(checkers[2])+1][int(checkers[3])-1] == " " or
                  (int(checkers[2])+1 == (int(checkers[0])+int(checkers[2]))//2 and int(checkers[3])-1 == (int(checkers[1])+int(checkers[3]))//2))) or
               (locationChec[int(checkers[2])+1][int(checkers[3])-1][:3] == "red" and (locationChec[int(checkers[2])-1][int(checkers[3])+1] == " " or
                  (int(checkers[2])-1 == (int(checkers[0])+int(checkers[2]))//2 and int(checkers[3])+1 == (int(checkers[1])+int(checkers[3]))//2)))):
            break
      betterSpots.append(checkers)
   if False == (betterSpots == []):
      jumpSpots = betterSpots [:]

   time.sleep(.35) #slight delay (to make it look like AI is thinking)
   if False == (jumpSpots == []): #if not empty (can jump over)
      pick = random.randint(0, len(jumpSpots)-1) #picks a random move out of the choices
      locationChec[int(jumpSpots[pick][2])][int(jumpSpots[pick][3])] = locationChec[int(jumpSpots[pick][0])][int(jumpSpots[pick][1])] #makes the play
      locationChec[int(jumpSpots[pick][0])][int(jumpSpots[pick][1])] = " "
      locationChec[(int(jumpSpots[pick][0])+int(jumpSpots[pick][2]))//2][(int(jumpSpots[pick][1])+int(jumpSpots[pick][3]))//2] = " "
      reloadChec(int(jumpSpots[pick][0]), int(jumpSpots[pick][1]))
      reloadChec(int(jumpSpots[pick][2]), int(jumpSpots[pick][3]))
      time.sleep(.2)
      reloadChec((int(jumpSpots[pick][0])+int(jumpSpots[pick][2]))//2, (int(jumpSpots[pick][1])+int(jumpSpots[pick][3]))//2)

      currentSpot = (int(jumpSpots[pick][2]), int(jumpSpots[pick][3])) #then loops for any other choices
      while True: #this is an identical loop to what is in the user function, just a bit smaller if statement
         if currentSpot[0]+2 < 8 and currentSpot[1]+2 < 8:
            if (locationChec[currentSpot[0]+2][currentSpot[1]+2] == " " and
                  locationChec[currentSpot[0]+1][currentSpot[1]+1][0:3] == "red"):
               locationChec[currentSpot[0]+2][currentSpot[1]+2] = locationChec[currentSpot[0]][currentSpot[1]]
               locationChec[currentSpot[0]+1][currentSpot[1]+1] = " "
               locationChec[currentSpot[0]][currentSpot[1]] = " "
               time.sleep(.2)
               reloadChec(currentSpot[0]+2, currentSpot[1]+2)
               reloadChec(currentSpot[0], currentSpot[1])
               time.sleep(.2)
               reloadChec(currentSpot[0]+1, currentSpot[1]+1)
               currentSpot = (currentSpot[0]+2, currentSpot[1]+2)
               continue

         if currentSpot[0]-2 > -1 and currentSpot[1]+2 < 8:
            if (locationChec[currentSpot[0]-2][currentSpot[1]+2] == " " and locationChec[currentSpot[0]][currentSpot[1]] == "blackKing" and
                  locationChec[currentSpot[0]-1][currentSpot[1]+1][0:3] == "red"):
               locationChec[currentSpot[0]-2][currentSpot[1]+2] = locationChec[currentSpot[0]][currentSpot[1]]
               locationChec[currentSpot[0]-1][currentSpot[1]+1] = " "
               locationChec[currentSpot[0]][currentSpot[1]] = " "
               time.sleep(.2)
               reloadChec(currentSpot[0]-2, currentSpot[1]+2)
               reloadChec(currentSpot[0], currentSpot[1])
               time.sleep(.2)
               reloadChec(currentSpot[0]-1, currentSpot[1]+1)
               currentSpot = (currentSpot[0]-2, currentSpot[1]+2)
               continue

         if currentSpot[0]+2 < 8 and currentSpot[1]-2 > -1:
            if (locationChec[currentSpot[0]+2][currentSpot[1]-2] == " " and
                  locationChec[currentSpot[0]+1][currentSpot[1]-1][0:3] == "red"):
               locationChec[currentSpot[0]+2][currentSpot[1]-2] = locationChec[currentSpot[0]][currentSpot[1]]
               locationChec[currentSpot[0]+1][currentSpot[1]-1] = " "
               locationChec[currentSpot[0]][currentSpot[1]] = " "
               time.sleep(.2)
               reloadChec(currentSpot[0]+2, currentSpot[1]-2)
               reloadChec(currentSpot[0], currentSpot[1])
               time.sleep(.2)
               reloadChec(currentSpot[0]+1, currentSpot[1]-1)
               currentSpot = (currentSpot[0]+2, currentSpot[1]-2)
               continue

         if currentSpot[0]-2 > -1 and currentSpot[1]-2 > -1:
            if (locationChec[currentSpot[0]-2][currentSpot[1]-2] == " " and locationChec[currentSpot[0]][currentSpot[1]] == "blackKing" and
                  locationChec[currentSpot[0]-1][currentSpot[1]-1][0:3] == "red"):
               locationChec[currentSpot[0]-2][currentSpot[1]-2] = locationChec[currentSpot[0]][currentSpot[1]]
               locationChec[currentSpot[0]-1][currentSpot[1]-1] = " "
               locationChec[currentSpot[0]][currentSpot[1]] = " "
               time.sleep(.2)
               reloadChec(currentSpot[0]-2, currentSpot[1]-2)
               reloadChec(currentSpot[0], currentSpot[1])
               time.sleep(.2)
               reloadChec(currentSpot[0]-1, currentSpot[1]-1)
               currentSpot = (currentSpot[0]-2, currentSpot[1]-2)
               continue
               
         break
      
   elif False == (singleSpots == []): #if not empty (single moves)
      pick = random.randint(0, len(singleSpots)-1) #choses a random spot in the list
      locationChec[int(singleSpots[pick][2])][int(singleSpots[pick][3])] = locationChec[int(singleSpots[pick][0])][int(singleSpots[pick][1])] #moves it
      locationChec[int(singleSpots[pick][0])][int(singleSpots[pick][1])] = " "
      reloadChec(int(singleSpots[pick][0]), int(singleSpots[pick][1]))
      reloadChec(int(singleSpots[pick][2]), int(singleSpots[pick][3]))
      
   else: #if no single moves
      errorChec.config(text = "Red wins!") #game is over
      update(37, 1)
      buttonHow.config(text = "Play Again", command = lambda: newGameChec())

def reloadChec(row, column): #reloads an individual space
   global buttonsChec, spotChec
   if row == 0 and locationChec[row][column] == "red": #if at the top, turn to king
      locationChec[row][column] = "redKing"
   if row == 7 and locationChec[row][column] == "black": #if at the bottom, turn to king
      locationChec[row][column] = "blackKing"
      
   if locationChec[row][column] == "red": #reloads with new images
      spotChec[row][column] = redImgChec
   elif locationChec[row][column] == "black":
      spotChec[row][column] = blackImgChec
   elif locationChec[row][column] == "redKing":
      spotChec[row][column] = kingRedImgChec
   elif locationChec[row][column] == "blackKing":
      spotChec[row][column] = kingBlackImgChec
   else:
      spotChec[row][column] = ""
   buttonsChec[row][column].config(image = spotChec[row][column], bg = "LightSalmon4") #changes the colour back to how it was before for base
   master.update()

#################################################################################################### Checkers end

def logIn():
   for widget in master.winfo_children():
         widget.destroy()
         
   frameUser=tk.Frame(master, width = screenWidth, height = screenHeight//5)
   frameUser.grid(row = 1, column = 0, columnspan = 6, sticky = "we")
   frameUser.propagate(False)
   framePass=tk.Frame(master, width = screenWidth, height = screenHeight//5)
   framePass.grid(row = 2, column = 0, columnspan = 6, sticky = "we")
   framePass.propagate(False)
   frameEnter=tk.Frame(master, width = screenWidth, height = screenHeight//6)
   frameEnter.grid(row = 3, column = 0, columnspan = 6, sticky = "we")
   frameEnter.propagate(False)
   frameComment=tk.Frame(master, width = screenWidth, height = screenHeight-(((screenHeight//5)*2)+(screenHeight//6)+screenHeight//10))
   frameComment.grid(row = 4, column = 0, columnspan = 6, sticky = "we")
   frameComment.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)


   tk.Button(frameHow, text = "Sign Up", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: signUp()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Quit", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: endLogIn()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Log In").pack(expand=True, fill="both")
   comment = tk.Label(frameComment, bg = "#000000", font = "Helvetica " + str(screenHeight//25), fg="#fff", text="")
   comment.pack(expand=True, fill="both")

   UserName = tk.Entry(frameUser, bg = "white smoke", font = "Helvetica " + str(screenHeight//20), justify = "center")
   UserName.pack(expand=True, fill="both")
   UserName.insert(0, "Username")
   UserName.focus_set()
   PassWord = tk.Entry(framePass, bg = "white smoke", font = "Helvetica " + str(screenHeight//20), justify = "center")
   PassWord.pack(expand=True, fill="both")
   PassWord.insert(0, "Password")
   tk.Button(frameEnter, text = "Enter", bg = "#fff", font = "Helvetica " + str(screenHeight//35), command = lambda: enterLog()).pack(expand=True, fill="both")

def signUp():
   for widget in master.winfo_children():
         widget.destroy()
         
   frameUser=tk.Frame(master, width = screenWidth, height = screenHeight//8)
   frameUser.grid(row = 1, column = 0, columnspan = 6, sticky = "we")
   frameUser.propagate(False)
   framePass=tk.Frame(master, width = screenWidth, height = screenHeight//8)
   framePass.grid(row = 2, column = 0, columnspan = 6, sticky = "we")
   framePass.propagate(False)
   framePass2=tk.Frame(master, width = screenWidth, height = screenHeight//8)
   framePass2.grid(row = 3, column = 0, columnspan = 6, sticky = "we")
   framePass2.propagate(False)
   frameEmail=tk.Frame(master, width = screenWidth, height = screenHeight//8)
   frameEmail.grid(row = 4, column = 0, columnspan = 6, sticky = "we")
   frameEmail.propagate(False)
   frameEnter=tk.Frame(master, width = screenWidth, height = screenHeight//8)
   frameEnter.grid(row = 5, column = 0, columnspan = 6, sticky = "we")
   frameEnter.propagate(False)
   frameComment=tk.Frame(master, width = screenWidth, height = screenHeight-(((screenHeight//8)*5)+screenHeight//10))
   frameComment.grid(row = 6, column = 0, columnspan = 6, sticky = "we")
   frameComment.propagate(False)
   frameMenu=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameMenu.grid(row = 0, column = 5, columnspan = 1, sticky = "we")
   frameMenu.propagate(False)
   frameTitle=tk.Frame(master, width = (screenWidth//3)*2, height = screenHeight//10)
   frameTitle.grid(row = 0, column = 1, columnspan = 4, sticky = "we")
   frameTitle.propagate(False)
   frameHow=tk.Frame(master, width = screenWidth//6, height = screenHeight//10)
   frameHow.grid(row = 0, column = 0, columnspan = 1, sticky = "we")
   frameHow.propagate(False)

   tk.Button(frameHow, text = "Log In", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: logIn()).pack(expand=True, fill="both")
   tk.Button(frameMenu, text = "Quit", bg = "#fff", font = "Helvetica " + str(screenHeight//50), command = lambda: endLogIn()).pack(expand=True, fill="both")
   tk.Label(frameTitle, bg = "#000000", font = "fixedsys " + str(screenHeight//35), fg="#fff", text="Sign Up").pack(expand=True, fill="both")
   comment = tk.Label(frameComment, bg = "#000000", font = "Helvetica " + str(screenHeight//25), fg="#fff", text="*Email is not required, I will only send\nemails when the game requires an update.")
   comment.pack(expand=True, fill="both")

   UserName = tk.Entry(frameUser, bg = "white smoke", font = "Helvetica " + str(screenHeight//25), justify = "center")
   UserName.pack(expand=True, fill="both")
   UserName.insert(0, "Username")
   UserName.focus_set()
   PassWord = tk.Entry(framePass, bg = "white smoke", font = "Helvetica " + str(screenHeight//25), justify = "center")
   PassWord.pack(expand=True, fill="both")
   PassWord.insert(0, "Password")
   PassWord2 = tk.Entry(framePass2, bg = "white smoke", font = "Helvetica " + str(screenHeight//25), justify = "center")
   PassWord2.pack(expand=True, fill="both")
   PassWord2.insert(0, "Password Again")
   Email = tk.Entry(frameEmail, bg = "white smoke", font = "Helvetica " + str(screenHeight//25), justify = "center")
   Email.pack(expand=True, fill="both")
   Email.insert(0, "Email*")
   tk.Button(frameEnter, text = "Enter", bg = "#fff", font = "Helvetica " + str(screenHeight//35), command = lambda: enterLog()).pack(expand=True, fill="both")

def endLogIn():
   global endGame
   endGame = True
   master.destroy()

endGame = False

client = gspread.authorize(ServiceAccountCredentials.from_json_keyfile_name("gameFiles\client_secret.json", ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']))       
sheet = client.open('2ksGames').sheet1

localData = open(".\gameFiles\CurrentStats.txt").read()
localData = localData.split("\n")

columnData = sheet.col_values(1)
match = False
for name in columnData:
   if name == localData[0]:
      match = True
      break
if match == False:
   master = tk.Tk()
   master.title("Log In")
   master.overrideredirect(1)
   master.geometry("%dx%d+0+0" % (master.winfo_screenwidth(), master.winfo_screenheight()))
   screenWidth = master.winfo_screenwidth()
   screenHeight = master.winfo_screenheight()

   logIn()
   master.mainloop()

   

def update(dataSet, increase):
   localData = open(".\gameFiles\CurrentStats.txt").read()
   localData = localData.split("\n")
   localData[dataSet] = str(int(localData[dataSet]) + increase)
   localData = '\n'.join(localData)
   
   localFile = open(".\gameFiles\CurrentStats.txt", 'w')
   localFile.write(localData)
   localFile.close()

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
   global TicTacToeImg, Connect4Img, MineSweeperImg, The2048Img, QuitImg, SudokuImg, HangManImg, BlackJackImg, CheckersImg, AccountImg
   pixelHeight=((screenHeight)//3)
   pixelWidth=((screenWidth)//3)
   SudokuImg = ImageTk.PhotoImage(Image.open("gameFiles/SudokuMenu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   The2048Img = ImageTk.PhotoImage(Image.open("gameFiles/2048Menu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   MineSweeperImg = ImageTk.PhotoImage(Image.open("gameFiles/MineSweeperMenu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   Connect4Img = ImageTk.PhotoImage(Image.open("gameFiles/Connect4Menu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   TicTacToeImg = ImageTk.PhotoImage(Image.open("gameFiles/TicTacToeMenu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   HangManImg = ImageTk.PhotoImage(Image.open("gameFiles/HangManMenu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   BlackJackImg = ImageTk.PhotoImage(Image.open("gameFiles/BlackJackMenu.jpeg").resize((pixelWidth, pixelHeight), resample=0))
   CheckersImg = ImageTk.PhotoImage(Image.open("gameFiles/CheckersMenu.jpeg").resize((pixelWidth, pixelHeight), resample=0))

   QuitImg = ImageTk.PhotoImage(Image.open("gameFiles/QuitMenu.jpeg").resize((pixelWidth, pixelHeight//2), resample=0))
   AccountImg = ImageTk.PhotoImage(Image.open("gameFiles/AccountMenu.jpeg").resize((pixelWidth, pixelHeight//2), resample=0))
   for widget in master.winfo_children(): #clears contents, but not frame meaning it can update without making a new window each time
      widget.destroy()
   master.configure(bg = "#000000") #Sets initial background colour to black

   frameTic=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameTic.grid(row = 1, column = 0, sticky = "we")
   frameTic.propagate(False)
   tk.Button(frameTic, image = TicTacToeImg, bg = "#fff", command = lambda: TicTacToe()).pack(expand=True, fill="both")
   frameMine=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameMine.grid(row = 1, column = 1, sticky = "we")
   frameMine.propagate(False)
   tk.Button(frameMine, image = MineSweeperImg, command = lambda: MineSweeper(" ")).pack(expand=True, fill="both")
   frame2048=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frame2048.grid(row = 2, column = 0, sticky = "we")
   frame2048.propagate(False)
   tk.Button(frame2048, image = The2048Img, command = lambda: the2048()).pack(expand=True, fill="both")
   frameSu=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameSu.grid(row = 2, column = 1, sticky = "we")
   frameSu.propagate(False)
   tk.Button(frameSu, image = SudokuImg, command = lambda: Sudoku()).pack(expand=True, fill="both")
   frameCon=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameCon.grid(row = 2, column = 2, sticky = "we")
   frameCon.propagate(False)
   tk.Button(frameCon, image = Connect4Img, command = lambda: Connect4()).pack(expand=True, fill="both")
   frameHang=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameHang.grid(row = 3, column = 0, sticky = "we")
   frameHang.propagate(False)
   tk.Button(frameHang, image = HangManImg, command = lambda: HangMan()).pack(expand=True, fill="both")
   frameJack=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameJack.grid(row = 3, column = 1, sticky = "we")
   frameJack.propagate(False)
   tk.Button(frameJack, image = BlackJackImg, command = lambda: BlackJack()).pack(expand=True, fill="both")
   frameChec=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameChec.grid(row = 3, column = 2, sticky = "we")
   frameChec.propagate(False)
   tk.Button(frameChec, image = CheckersImg, command = lambda: Checkers()).pack(expand=True, fill="both")
   
   frameStuff=tk.Frame(master, width = pixelWidth, height = pixelHeight)
   frameStuff.grid(row = 1, column = 2, sticky = "we")
   frameStuff.propagate(False)

   frameQuit=tk.Frame(frameStuff, width = pixelWidth, height = pixelHeight//2)
   frameQuit.grid(row = 0, column = 0, sticky = "we")
   frameQuit.propagate(False)
   frameAccount=tk.Frame(frameStuff, width = pixelWidth, height = pixelHeight//2)
   frameAccount.grid(row = 1, column = 0, sticky = "we")
   frameAccount.propagate(False)
   tk.Button(frameQuit, image = QuitImg, command = master.destroy).pack(expand=True, fill="both")
   tk.Button(frameAccount, image = AccountImg, command = lambda: Account()).pack(expand=True, fill="both")
   

if endGame == False:

   spot = 0
   for name in columnData:
      spot += 1
      if name == localData[0]:
         match = True
         break

   rowData = sheet.row_values(spot)

   for data in range(len(localData)-2):
      localData[data+2] = str(int(localData[data+2]) + int(rowData[data+2]))

   sheet.insert_row(localData, spot)
   sheet.delete_row(spot+1)


   for data in range(len(localData)-2):
      localData[data+2] = "0"
   localData = '\n'.join(localData)

   localFile = open(".\gameFiles\CurrentStats.txt", 'w')
   localFile.write(localData)
   localFile.close()

   master = tk.Tk() #creates the window
   master.title("2k's games")
   master.overrideredirect(1) #gets rid of toolbar
   master.geometry("%dx%d+0+0" % (master.winfo_screenwidth(), master.winfo_screenheight())) #makes it fill full screen
   screenWidth = master.winfo_screenwidth()
   screenHeight = master.winfo_screenheight()

   menu()
   master.mainloop()
