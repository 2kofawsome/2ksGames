from tkinter import *
import tkinter as tk
import random
from tkinter.font import Font

#Sam Gunter
#Sudoku was finished 2:52pm on the 15th of april, 2018
#This was created to allow the user to add new sudoku boards

#No next steps! Yay!

#Uses same Su variables as the sudoku game
#User simply adds in the numbers, boom if it works it gets saved
#See sudoku game for most of how this works, only comments on last function

def Sudoku():
   global myFont
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
   rowSu=-1
   columnSu=-1
   if screenWidth<screenHeight:
      pixelMine=(screenWidth//10)
   else:
      pixelMine=(screenHeight//10)
   myFont=Font(family="Helvetica", size=pixelMine//2)
   boldFont=Font(family="Helvetica", size=pixelMine//2, weight='bold')
   Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixelMine//5), text="Sudoku").grid(row = 0, columnspan = 9)
   tk.Button(master, text = "Exit", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = master.destroy).grid(row = 0, column = 0, columnspan=3, sticky = "we")
   tk.Button(master, text = "Save", font=("Helvetica", pixelMine//5), height = 1, bg = "#fff", command = lambda: saveSu()).grid(row = 0, column = 6, columnspan=3, sticky = "we")
   errorSu = tk.Label(master, bg = "#000000", fg = "#fff", font=("Helvetica", pixelMine//5), text="Use numbers only!")

   mistakeSu=[[]]
   for r in range(9):
      if len(mistakeSu)==r:
         mistakeSu.append([])
      for c in range(9):
         mistakeSu[r].append(False)

   shownSu=[[]]
   for r in range(9):
      if len(shownSu)==r:
         shownSu.append([])
      for c in range(9):
         shownSu[r].append(" ")
         
   frameSu=[[]]
   buttonsSu=[[]]
   for r in range(9):
      if len(buttonsSu)==r:
         buttonsSu.append([])
         frameSu.append([])
      for c in range(9):
         frameSu[r].append(tk.Frame(master, width = pixelMine, height = pixelMine, borderwidth = "1"))
         frameSu[r][c].grid(row=r+1, column=c, sticky="nsew") 
         frameSu[r][c].propagate(False)
         if shownSu[r][c]==" " and (r//3 + c//3) % 2 == 0:
            buttonsSu[r].append(tk.Button(frameSu[r][c], relief = 'flat', font=myFont, bg = "white", borderwidth = "0", text = shownSu[r][c], command = lambda forCommand=[r, c]: clickSu(forCommand[0], forCommand[1])))
         elif shownSu[r][c]==" " and (r//3 + c//3) % 2 == 1:
            buttonsSu[r].append(tk.Button(frameSu[r][c], relief= 'flat', font=myFont, bg = "light grey", borderwidth = "0", text = shownSu[r][c], command = lambda forCommand=[r, c]: clickSu(forCommand[0], forCommand[1])))
         elif (r//3 + c//3) % 2 == 0:
            buttonsSu[r].append(tk.Label(frameSu[r][c], text = shownSu[r][c], font=boldFont, bg = "white", ))
         elif (r//3 + c//3) % 2 == 1:
            buttonsSu[r].append(tk.Label(frameSu[r][c], text = shownSu[r][c], font=boldFont, bg = "light grey"))
         buttonsSu[r][c].pack(expand=True, fill="both")

def clickSu(row, column):
   global buttonsSu
   global frameSu
   global shownSu
   global rowSu
   global columnSu
   global entry

   try:
      enterSu("event")
   except:
      a=1
   
   if rowSu >= 0 and columnSu >=0:
      entry.pack_forget()
      buttonsSu[rowSu][columnSu].pack(expand=True, fill="both")
   rowSu=row
   columnSu=column
   buttonsSu[row][column].pack_forget()
   
   if (row//3 + column//3) % 2 == 0 and mistakeSu[row][column]==False:
      entry = tk.Entry(frameSu[row][column], bg = "white", font = myFont, justify = "center")
   elif (row//3 + column//3) % 2 == 1 and mistakeSu[row][column]==False:
      entry = tk.Entry(frameSu[row][column], bg = "light grey", font = myFont, justify = "center")
   elif (row//3 + column//3) % 2 == 0 and mistakeSu[row][column]==True:
      entry = tk.Entry(frameSu[row][column], bg = "firebrick1", font = myFont, justify = "center")
   elif (row//3 + column//3) % 2 == 1 and mistakeSu[row][column]==True:
      entry = tk.Entry(frameSu[row][column], bg = "firebrick3", font = myFont, justify = "center")
   entry.pack(expand=True, fill="both")
   entry.focus_set()

def enterSu(event):
   global shownSu
   global mistakeSu
   try:
      errorSu.grid_forget()
      shownSu[rowSu][columnSu]=int(entry.get()[-1])
      entry.pack_forget()
      buttonsSu[rowSu][columnSu].config(text = shownSu[rowSu][columnSu])
      buttonsSu[rowSu][columnSu].pack(expand=True, fill="both")
   except: 
      if str(entry.get()) == "" or str(entry.get()) == " ":
         shownSu[rowSu][columnSu] = " "
         entry.pack_forget()
         buttonsSu[rowSu][columnSu].config(text = shownSu[rowSu][columnSu])
         buttonsSu[rowSu][columnSu].pack(expand=True, fill="both")
      else:
         errorSu.config(text = "Use numbers only!")
         errorSu.grid(row = 10, columnspan = 9)

   for c in range(9):
      for r in range(9):
         mistakeSu[r][c]=False
         
   for c in range(9):
      for r in range(9):
         for n in range(8):
            if shownSu[r-(n+1)][c] == shownSu[r][c] and shownSu[r-(n+1)][c] != " ":
               for x in range(9):
                  mistakeSu[r-(x)][c]=True
               break
         for n in range(8):
            if shownSu[r][c-(n+1)] == shownSu[r][c] and shownSu[r][c-(n+1)] != " ":
               for x in range(9):
                  mistakeSu[r][c-(x)]=True
               break
         for n in range(3):
            for m in range(3):
               if shownSu[(r//3)*3+n][(c//3)*3+m] == shownSu[r][c] and shownSu[r][c] != " " and (r != (r//3)*3+n or c != (c//3)*3+m):
                  for x in range(3):
                     for y in range(3):
                        mistakeSu[(r//3)*3+x][(c//3)*3+y]=True
                  break
      
   for r in range(9):
      for c in range(9):
         if (c//3 + r//3) % 2 == 0 and mistakeSu[r][c]==False:
            buttonsSu[r][c].config(bg='white')
         elif (c//3 + r//3) % 2 == 1 and mistakeSu[r][c]==False:
            buttonsSu[r][c].config(bg='light grey')
         elif (c//3 + r//3) % 2 == 0 and mistakeSu[r][c]==True:
            buttonsSu[r][c].config(bg='firebrick1')
         elif (c//3 + r//3) % 2 == 1 and mistakeSu[r][c]==True:
            buttonsSu[r][c].config(bg='firebrick3')

def saveSu():
   filled=True #sets it to believe that all full
   for c in range(9):
      for r in range(9):
         if mistakeSu[r][c]==True: #if any mistakes, not good
            filled=False
         elif shownSu[r][c]==" ": #if any empty, not good
            filled=False
   if filled==True:

      for x in range(3): #makes it so one board turns into 9 boards through manipulation
         shownSu.append(shownSu[0]) #changes rows by 3
         shownSu.append(shownSu[1])
         shownSu.append(shownSu[2])
         del shownSu[0]
         del shownSu[0]
         del shownSu[0]
         for y in range(3):
            for r in range(9):
               shownSu[r].append(shownSu[r][0]) #changes columns by 3
               shownSu[r].append(shownSu[r][1])
               shownSu[r].append(shownSu[r][2])
               del shownSu[r][0]
               del shownSu[r][0]
               del shownSu[r][0]
            saveSu="" #string that goes into file
            for r in range(9):
               for c in range(9):
                  saveSu= saveSu + str(shownSu[r][c]) #adds in the number
                  if c == 8 and r != 8:
                     saveSu= saveSu + "|" #splits rows
                  elif c != 8:
                     saveSu= saveSu + " " #splits columns

            fileSu = open(".]gameFiles\SudokuBoards.txt").readlines() #opens in list form
            duplicate=False
            for n in range(len(fileSu)): #for length of the file
               if (saveSu+"\n") == fileSu[n]: #checks to see if already in the file
                  duplicate=True
            if duplicate == False: #if it is not in code
               helloFile = open(".\gameFiles\SudokuBoards.txt", 'a') #opens board in append mode
               helloFile.write(saveSu) #adds the board
               helloFile.write("\n") #clicks enter for next board
               helloFile.close()
            else: 
               errorSu.config(text = "Already have this one") #tells user to try again
               errorSu.grid(row = 10, columnspan = 9)
      
master = Tk() 
master.title("2k's games")
master.config(bg = "#000000")
master.overrideredirect(1)
master.geometry("%dx%d+0+0" % (master.winfo_screenwidth(), master.winfo_screenheight())) 
screenWidth = master.winfo_screenwidth()
screenHeight = master.winfo_screenheight()

Sudoku()
master.mainloop()
