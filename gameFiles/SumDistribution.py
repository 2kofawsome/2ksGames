#! python3.6

import random, time

runTime= time.time()
sums = {} #1 draw
Nsums = 0
Oversums = 0
deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10]

for a in range(len(deck)):
    drawn = deck[a]
    Nsums+=1
    if drawn > 16:
        Oversums +=1
    if str(drawn) in sums:
        sums[str(drawn)]+=1
    else:
        sums[str(drawn)]=1

print(time.time()-runTime)
print(Oversums)
print(Nsums)
print(Oversums / Nsums *100)
print(sums)
print("""


""")

runTime= time.time()
sums = {} #2 draw
Nsums = 0
Oversums = 0

for a in range(len(deck)):
    deck = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10]
    drawn = deck[a]
    del deck[a]
    for b in range(len(deck)):
        Nsums+=1
        newDrawn = drawn + deck[b]
        if newDrawn > 16:
            Oversums +=1
        if str(newDrawn) in sums:
            sums[str(newDrawn)]+=1
        else:
            sums[str(newDrawn)]=1

print(time.time()-runTime)
print(Oversums)
print(Nsums)
print(Oversums / Nsums *100)
print(sums)
print("""


""")



runTime= time.time()
sums = {} #3 draw
Nsums = 0
Oversums = 0
deck0 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10]

for a in range(len(deck0)):
    deck1 = deck0[:]
    drawn0 = deck1[a]
    del deck1[a]
    for b in range(len(deck1)):
        deck2 = deck1[:]
        drawn1 = drawn0 + deck2[b]
        del deck2[b]
        for c in range(len(deck2)):
            deck3 = deck2[:]
            drawn2 = drawn1 + deck3[c]
            
            Nsums+=1
            if drawn2 > 16:
                Oversums +=1
            if str(drawn2) in sums:
                sums[str(drawn2)]+=1
            else:
                sums[str(drawn2)]=1

print(time.time()-runTime)
print(Oversums)
print(Nsums)
print(Oversums / Nsums *100)
print(sums)
print("""


""")

runTime= time.time()
sums = {} #4 draw
Oversums = 0
deck0 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10]

for a in range(len(deck0)):
    deck1 = deck0[:]
    drawn0 = deck1[a]
    del deck1[a]
    for b in range(len(deck1)):
        deck2 = deck1[:]
        drawn1 = drawn0 + deck2[b]
        del deck2[b]
        for c in range(len(deck2)):
            deck3 = deck2[:]
            drawn2 = drawn1 + deck3[c]
            del deck3[c]
            for d in range(len(deck3)):
                deck4 = deck3[:]
                drawn3 = drawn2 + deck4[d]
                
                if drawn3 > 16:
                    Oversums +=1
                if str(drawn3) in sums:
                    sums[str(drawn3)]+=1
                else:
                    sums[str(drawn3)]=1

print(time.time()-runTime)
print(Oversums)
print(52 * 51 * 50 * 49)
print(Oversums / (52 * 51 * 50 * 49) *100)
print(sums)
print("""


""")




runTime= time.time()
sums = {} #5 draw
Oversums = 0
deck0 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10]

for a in range(len(deck)):
    print(time.time()-runTime)
    print(str(a*2) + "%")
    deck1 = deck0[:]
    drawn0 = deck1[a]
    del deck1[a]
    for b in range(len(deck1)):
        deck2 = deck1[:]
        drawn1 = drawn0 + deck2[b]
        del deck2[b]
        for c in range(len(deck2)):
            deck3 = deck2[:]
            drawn2 = drawn1 + deck3[c]
            del deck3[c]
            for d in range(len(deck3)):
                deck4 = deck3[:]
                drawn3 = drawn2 + deck4[d]
                del deck4[d]
                for e in range(len(deck4)):
                    drawn4 = drawn3 + deck4[e]
                    if drawn4 > 16:
                        Oversums +=1
                    if str(drawn4) in sums:
                        sums[str(drawn4)]+=1
                    else:
                        sums[str(drawn4)]=1

print(time.time()-runTime)
print(Oversums)
print(52 * 51 * 50 * 49 * 48)
print(Oversums / (52 * 51 * 50 * 49 * 48) *100)
print(sums)
print("""


""")

runTime= time.time()
sums = {} #6 draw
Oversums = 0
deck0 = [1, 1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6,
        7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, 10, 10, 10, 10,
        10, 10, 10, 10, 10, 10, 10, 10]

for a in range(len(deck)):
    print(time.time()-runTime)
    print(str(a*2) + "%")
    deck1 = deck0[:]
    drawn0 = deck1[a]
    del deck1[a]
    for b in range(len(deck1)):
        deck2 = deck1[:]
        drawn1 = drawn0 + deck2[b]
        del deck2[b]
        for c in range(len(deck2)):
            deck3 = deck2[:]
            drawn2 = drawn1 + deck3[c]
            del deck3[c]
            for d in range(len(deck3)):
                deck4 = deck3[:]
                drawn3 = drawn2 + deck4[d]
                del deck4[d]
                for e in range(len(deck4)):
                    deck5 = deck4[:]
                    drawn4 = drawn3 + deck5[e]
                    del deck5[e]
                    for f in range(len(deck5)):
                        drawn5 = drawn4 + deck5[f]
                        if drawn5 > 16:
                            Oversums +=1
                        if str(drawn5) in sums:
                            sums[str(drawn5)]+=1
                        else:
                            sums[str(drawn5)]=1

print(time.time()-runTime)
print(Oversums)
print(52 * 51 * 50 * 49 * 48 * 47)
print(Oversums / (52 * 51 * 50 * 49 * 48 * 47) *100)
print(sums)
print("""


""")
