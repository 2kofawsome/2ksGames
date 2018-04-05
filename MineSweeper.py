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

def MineSweeper(errorCheck):
   master.bind("<Button-3>", flagMine)
   master.bind("<Button-2>", chordMine)
   global varSizeMine #this becomes a non var variable later (var is from tkinter)
   global varBombMine
   for widget in master.winfo_children():
      widget.destroy()
   master.configure(bg = "darkgrey") #Sets intial background colour to darkgrey
   Label(master, bg = "darkgrey", text="MineSweeper").grid(row = 0, column = 1) #just says the game name, bg means background (black) and fg means foreground (white)
   tk.Button(master, text = "Menu", height = 1, width = 10, bg = "#fff", command = lambda: menu()).grid(row = 0, column = 0, sticky = "we") #sticky we causes it to fill all availible space
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
Since Mine Sweeper knows that you can safely click all tiles around it, it automatically clicks them all for you. This is the reason a click can sometimes clear half the board.
Now go back to the 1 that was uncovered. If any of the tiles touching the 1 is a flag (therefore a bomb) you know that all the other boxes have no bombs (the 1 means only touching 1 bomb).
This means the other 7 tiles are safe to left click to uncover new numbers which will lead to new information about bombs.

Although you could click on each tile around the 1, there is a quicker way to complete the same task. A method called "chording".
If a number is uncovered (such as the 1) and the required amount of flags are touching that tile (meaning no other bombs possible), then you can chord.
Chording will automatically click every adjacent tile to the number that you chorded as long as there is no flag on the tile.
Be warned though, if you incorrectly placed your flags it could click on a spot with a bomb and end the game. To chord use the middle button on the mouse (not on all mouses).

The first click is guarenteed to be safe, but after that you must make choices for yourself, good luck!""").pack(expand=True, fill="both")
   
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
   global shownMine #Similar to TicTacToe(), most of these are barely called again, but ahve to all be declaired her as global
   global frameMine
   global reliefMine
   global hiddenMine
   global myFont
   global pixelMine
   global flagsMine
   global statusMine
   global bombsLeftMine
   bombsLeftMine=bombMine #keep track fo flag counter in top corner
   statusMine="start"
   for widget in master.winfo_children(): #same as TicTacToe2.0 this delets all widgets ons creen
      widget.destroy()
   if screenWidth<screenHeight:
      pixelMine=(screenWidth//(sizeMine+1))
   else:
      pixelMine=(screenHeight//(sizeMine+1))
   
   hiddenMine=[[]] #this will be the minesweeper board fully filled up and user can not see it
   for r in range(sizeMine): #for the rows, which is the avriable
      if len(hiddenMine)==r: #if if maxed out amke a new list
         hiddenMine.append([])
      for c in range(sizeMine): #for columns which si the same variable (square)
         hiddenMine[r].append(" ") #adds an empty space, this is solely to make the list of lists
   shownMine=[[]] #what the user gets shown
   for r in range(sizeMine):
      if len(shownMine)==r:
         shownMine.append([])
      for c in range(sizeMine):
         shownMine[r].append("") #adds nothing this time instead of  a space so later on the program can see the difference between shown and hidden values
   reliefMine=[[]] #same as both lists of lists above, but is to set the buttons as raised so they can be chaged to appear pushed down later on when they are clicked
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

   myFont=Font(family="Helvetica", size=pixelMine//2) #fotn seems to work if it is half the siz eof the block, needs more testing on different monitors
   Label(master, bg = "darkgrey", font=("Helvetica", pixelMine//5), text="MineSweeper").grid(row = 0, columnspan = sizeMine) #column span makes it take up more lines
   tk.Button(master, text = "Menu", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: MineSweeper(" ")).grid(row = 0, column = 0, columnspan=3, sticky = "we")
   button1=tk.Button(master, text = str(bombsLeftMine)+" bombs left", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff").grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we") #this button is named because it has to be edited later on
   frameMine=[] #sets the frames, this is needed to specify the amount of pixels each box should be
   for r in range(sizeMine):
      for c in range(sizeMine):
         frameMine.append(tk.Frame(master, width = pixelMine, height = pixelMine)) #makes frame with the pixel by pixel value
         frameMine[r*sizeMine+c].grid(row=r+1, column=c, sticky="nsew") #makes it so button inside takes up whole frame
         frameMine[r*sizeMine+c].propagate(False) #makes it so frame doesntr get smaller
         tk.Button(frameMine[r*sizeMine+c], text = shownMine[r][c], font=myFont, activebackground = "grey", bg = "lightgrey", command = lambda forCommand=[r, c]: clickMine(forCommand[0], forCommand[1])).pack(expand=True, fill="both") #adds teh button into the frame, these act as each sqaure in minesweeper with a predefined textsize, background, etc

def flagMine(event): #This might be one of the msot complicated codes I have created, so many numbers togetehr all of which are variables and most of which are pixels related to screen
   if statusMine!="end": #makes it so this code oesnt run if bomb has been triggered
      global sizeMine
      global pixelMine
      global bombsLeftMine
      global flagsMine
      for r in range(sizeMine):
         for c in range(sizeMine):
            if frameMine[r*sizeMine+c].winfo_y() < master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_y()+pixelMine > master.winfo_pointery() and frameMine[r*sizeMine+c].winfo_x() < master.winfo_pointerx() and frameMine[r*sizeMine+c].winfo_x()+pixelMine > master.winfo_pointerx() and reliefMine[r][c]=="raised": #long thing to see if the cusor is within frame window and if it is still rasied (not clicked yet)
               for widget in frameMine[r*sizeMine+c].winfo_children():
                  widget.destroy()
               if flagsMine[r][c] == "?": #if already a flag
                  bombsLeftMine+=1 #adds 1 bomb (because 1 less flag)
                  flagsMine[r][c]=" " #turns off flag
                  tk.Button(frameMine[r*sizeMine+c], text = shownMine[r][c], font=myFont, activebackground = "grey", bg = "lightgrey", command = lambda forCommand=[r, c]: clickMine(forCommand[0], forCommand[1])).pack(expand=True, fill="both") #creaes button as normal
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
               chording=0 #this variable checks to see if all flags around the number have been declaired
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
               if chording == hiddenMine[r][c]: #if there are the saem amount of flags as the number
                  if r-1>=0 and c-1>=0 and flagsMine[r-1][c-1] == " ": #clicks on every open spot aorund it
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

def updateMine(row, column): #this updates only 1 sqaure, before it was updating all of them but that make a slight lag (less than a second) which was not good
   for widget in frameMine[row*sizeMine+column].winfo_children(): #deletes all buttons in the frame (there will only be 1 button in the frame)
      widget.destroy()
   if shownMine[row][column] == " " or shownMine[row][column] == 1:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "blue").pack(expand=True, fill="both") #makes a new button which is the same as the last, but with new value
   elif shownMine[row][column] == 2:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "green").pack(expand=True, fill="both")
   elif shownMine[row][column] == 3:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "red").pack(expand=True, fill="both")
   elif shownMine[row][column] == 4:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "navy").pack(expand=True, fill="both")
   elif shownMine[row][column] == 5:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "crimson").pack(expand=True, fill="both")
   elif shownMine[row][column] == 6:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "darkcyan").pack(expand=True, fill="both")
   elif shownMine[row][column] == 7:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "black" ).pack(expand=True, fill="both")
   elif shownMine[row][column] == 8:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "silver").pack(expand=True, fill="both")
   else:
      tk.Button(frameMine[row*sizeMine+column], relief = reliefMine[row][column], text = shownMine[row][column], font=myFont,
      activebackground = "grey", bg = "lightgrey", fg = "black").pack(expand=True, fill="both")

   win="True" #starts as the person asummed one
   for r in range(sizeMine):
      for c in range(sizeMine):
         if reliefMine[r][c] == "raised" and hiddenMine[r][c] != "!": #if a block is raised (therefore not clicked) and it is not a bomb
            win="False" #makes them not wn yet
   if win == "True": #if that wasnt triggered
      endMine("win") #triggers end game won

def endMine(result): #end game
   button1=tk.Button(master, text = "Again", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: createBoardMine()).grid(row = 0, column = sizeMine-3, columnspan=3, sticky = "we") #allows user to play again witht he same specifications (baord size and amount of bombs)
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
            tk.Button(frameMine[r*sizeMine+c], relief = reliefMine[r][c], text = shownMine[r][c], font=myFont, bg = "lightgrey", fg = "blue").pack(expand=True, fill="both") #all the rest just display their hidden numbers some of which were already shwon
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


def clickMine(row, column): #This is used 1 time to make sure the user doesnt get out 1st time
   global statusMine
   global sizeMine
   global hiddenMine
   if statusMine == "start": #if this function hasnt been triggered yet
      for b in range(bombMine): #to adds bombs to hidden list
         while True:
            rowLocation=random.randint(0, sizeMine-1) #random row in range
            columnLocation=random.randint(0, sizeMine-1) #random column in range
            if hiddenMine[rowLocation][columnLocation] == " " and (rowLocation != row or columnLocation != column): #if nothing is there and it isnt the match of either row or column to where the user clicked
               hiddenMine[rowLocation][columnLocation]="!" #sets bomb, other wise the while loop makes new random row and column
               break
      for r in range(sizeMine):
         for c in range(sizeMine):
            if  hiddenMine[r][c] == " ":
               touching=0 #sets how many it is touchign to 0
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
                  hiddenMine[r][c]=" " #if it is 0 (because we dont want to display 0s)
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
      tk.Button(frameMine[row*sizeMine+column], text = hiddenMine[row][column], font=myFont, bg = "darkred").pack(expand=True, fill="both") #darkred to make them know it was the bomb that killed them
      
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

MineSweeper(" ")
master.mainloop()
