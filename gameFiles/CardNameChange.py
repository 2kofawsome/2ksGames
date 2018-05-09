#! python3.6

import os, shutil

directory = os.path.abspath('.')
print(directory)

for files in os.listdir("CardDeck"):
    oldFileName = os.path.join(directory, "CardDeck", files)

    newList=files.split('_of_')
    newString='-'.join(newList)

    if newString.endswith('s2.png'):
        newList=newString.split('s2')
        newString='s'.join(newList)

    if newString.startswith('ace'):
        newList=newString.split('ace')
        newString='1'.join(newList)

    if newString.startswith('queen'):
        newList=newString.split('queen')
        newString='11'.join(newList)

    if newString.startswith('ace'):
        newList=newString.split('ace')
        newString='12'.join(newList)

    if newString.startswith('king'):
        newList=newString.split('king')
        newString='13'.join(newList)
    
    newFileName = os.path.join(directory, "CardDeck", newString)

    shutil.move(oldFileName, newFileName)
