#! python3.6

import pyperclip

before=pyperclip.paste()

newlist=before.split('\n')


while True:
    blah=False
    for length in range(len(newlist)):
        if len(newlist[length]) < 6:
            print(newlist[length])
            del newlist[length]
            print(length)
            blah=True
            break
    if blah == False:
        break
    
after='\n'.join(newlist)
pyperclip.copy(after)
