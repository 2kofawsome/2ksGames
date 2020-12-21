# 2ksGames


## Play
run the Games2k.py file after downloading the required pip package with
```bash
$ pip install pillow
```
or run the Games2k.exe file.

## Games

A collection of 2D turn based games that I have been creating from scratch, 

Games created are TicTacToe, MineSweeper, 2048, Sudoku, Connect 4, Hangman, BlackJack (21), and Checkers.


![All Games](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/mainScreen.png) 

<p align="center"><i>Homescreen with a sneakpeak of all games</i></p>

### TicTacToe 2.0

In this game, you are able to play TicTacToe against a friend (multi-player) or against various bot that play random/sub-optimal/optimal strategies.

This code was built using...

Check out the code on lines 9-500
```python
def TicTacToe():
   for widget in master.winfo_children():
      widget.destroy()
   delayTic=time.time()
...
      if gridWinTic[0] == gridWinTic[4] == gridWinTic[8] == 0: #if no winner, goes to player again
         reloadTic()
      else:
         endTic("ai") #if the ai won, endTic function
```

![TicTacToe Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/TicTacToeScreen.png) 

### MineSweeper

In this game, you are able to play MineSweeper with variable board sizes and bomb amounts.

Check out the code on lines 502-867
```python
def MineSweeper(errorCheck):
   master.bind("<Button-3>", flagMine)
   master.bind("<Button-2>", chordMine)
   global varSizeMine, varBombMine #this becomes a non var variable later (var is from tkinter)
...
   else: #if a number
      shownMine[row][column]=hiddenMine[row][column] #simply displays the number
      reliefMine[row][column]="sunken"
      updateMine(row, column) #then updates
```

![MineSweeper Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/MineSweeperScreen.png) 

### 2048

In this game, you are able to play 2048! The game I was playing on my phone at time I was deciding on my next game to code.

Check out the code on lines 869-1262
```python
def the2048():
   timeCount = time.time()
   delay2048=time.time()
   win2048="schrodinger"
...
         else:
            labelWho.config(text="Can't go\nthat way")
         reloadFull2048()
   delay2048 = time.time()
```

![2048 Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/2048Screen.png) 

### Sudoku

In this game, you are able to play Sudoku with starting boards of various "difficulties" meaning more/less starting numbers.

Check out the code CreateSudokuBoards.py and on lines 1264-1599
```python
def Sudoku():
   global timeCount
   timeCount = time.time()
   for widget in master.winfo_children():
...
      update(24+difficultySu, 1)
      update(23, time.time()-timeCount)
      buttonHow.config(text = "Play Again", command = lambda: Sudoku()) #allows the user to play again
      errorSu.config(text="You win!") #changes from preset error message (earlier) to winner message
```

![Sudoku Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/SudokuScreen.png) 

### Connect 4

In this game, you are able to play Connect 4 against a friend (multi-player) or against a bot that plays with sub-optimal strategy.

Check out the code on lines 1601-2052
```python
def Connect4():
   global oneCon
   oneCon = False #preset as multiplayer
   master.unbind("<ButtonRelease-1>")
...
   else: #if multiplayer
      turnLabelCon.config(text=turnCon + " wins!") #who evers turn it is wins, if a tie the turnCon is "no one"
   buttonHow.config(text = "Play Again", command = lambda: boardCon()) #allows user to play again
   update(27, time.time()-timeCount)
```

![Connect4 Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/Connect4Screen.png) 

### Hangman

In this game, you are able to play Hangman with a word inputted by a friend or against a dictionary of common English words.

Check out the code in UsedToCreateWords.py and on lines 2054-2330
```python
def HangMan():
   global alphabet
   alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'] #this is created now, and used later for creating buttons and checking for letters in the words
   for widget in master.winfo_children():
...
         frameWho.grid(row = 7, column = 1, rowspan = 20, columnspan = 20, sticky = "we")
         frameWho.propagate(False)
         turnLabelCon = tk.Label(frameWho, bg = "#000000", font = "Helvetica " + str((screenWidth-(screenHeight-screenHeight//17))//15), fg="#fff", text="You lose.\n\nThe word was\n"+wordHang) #creates a loser message with the word
         turnLabelCon.pack(expand=True, fill="both")
```

![Hangman Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/HangManScreen.png) 

### Blackjack (21)

In this game, you are able to play blackjack (21) against the house, but don't worry, the hosue doesn't ALWAYS win.

Check out the code on lines 2332-2666
```python
def BlackJack():
   global cardImg, hangImg, playerCard, dealerCard, comment, deck21, buttonHow, buttonStand, buttonHit, sideButton
   for widget in master.winfo_children():
      widget.destroy()
...
   sideButton.config(state = "normal") 
   buttonStand.config(state = "disabled") #disables all buttons until a new deal is made
   buttonHit.config(state = "disabled")
   update(34, time.time()-timeCount)
```

![BlackJack Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/BlackJackScreen.png) 

### Checkers

In this game, you are able to play checkers against a friend (multi-player) or against a bot that plays with sub-optimal strategy.

Check out the code on lines 2668-3190
```python
def Checkers():
   global oneChec #this will make game single player or multiplayer
   oneChec = False #preset to multiplayer
   for widget in master.winfo_children():
...
   else:
      spotChec[row][column] = ""
   buttonsChec[row][column].config(image = spotChec[row][column], bg = "LightSalmon4") #changes the colour back to how it was before for base
   master.update()
```

![Checkers Gameplay](https://raw.githubusercontent.com/2kofawsome/2ksGames/master/gameFiles/CheckersScreen.png) 


## Credits
- [Sam Gunter](https://github.com/2kofawsome)
