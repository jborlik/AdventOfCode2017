#  Day 3

import numpy as np

#  37  36  35  34  33  32  31
#  38  17  16  15  14  13  30
#  39  18   5   4   3  12  29
#  40  19   6   1   2  11  28
#  41  20   7   8   9  10  27
#  42  21  22  23  24  25  26
#  43  44  45  46  47  48  49  50

#  block 0 (1-1): 1x1
#  block 1 (2-9): 3x3
#  block 2 (10-25): 5x5
#  block 3 (26-49): 7x7
#  block 4 (50-81): 9x9

# squares:  min loc, max loc, length of side
squares = [( (2*a-1)**2+1, (2*a+1)**2, 2*a+1) for a in range(1,500) ]
squares.insert(0, (1,1,1))

puzzleinput = 368078

print(squares)

def findContainingSquare(theInput):
    containingSquare = ()
    containingIndex = 0
    for (whichSquare, aSquare) in enumerate(squares):
        if (theInput >= aSquare[0]) and (theInput <= aSquare[1]):
            containingSquare = aSquare
            containingIndex = whichSquare
            break
    return (containingIndex, containingSquare)

def findLocOnSquare(theInput, theSquare):
    (side, pos) = divmod(theInput - theSquare[0], theSquare[2]-1)
    #print("theInput=",theInput, " min=", theSquare[0], "side=", side, " pos=", pos)
    midpoint = (theSquare[2] - 1)/2 - 1
    #print("midpoint=", midpoint)
    diffToMid = int(abs(midpoint - pos))
    print("diff to mid=", diffToMid)
    return diffToMid

theInput = puzzleinput
(anIndex, conSquare) = findContainingSquare(theInput)
print ("Puzzleinput in square: ", anIndex, " ", conSquare)
diffToMid = findLocOnSquare(theInput,conSquare)
print("Steps = ", anIndex + diffToMid)

print("****Part2*****")

bsize = 20
borig = int((bsize-1)/2)
bigmatrix = np.zeros((bsize+1,bsize+1), dtype=int)
bigmatrix[borig,borig] = 1
ix = borig + 1
iy = borig
iindex = 2
isquare = 1
iloconsquare = 0
iside = 0
iloconside = 0
while (ix < bsize) and (iy < bsize):
    thissum = bigmatrix[ix-1,iy+1] + bigmatrix[ix,iy+1] + bigmatrix[ix+1,iy+1] + \
              bigmatrix[ix-1,iy] + bigmatrix[ix,iy] + bigmatrix[ix+1,iy] + \
              bigmatrix[ix-1,iy-1] + bigmatrix[ix,iy-1] + bigmatrix[ix+1,iy-1]
    bigmatrix[ix,iy] = thissum
    print("For ix=",ix," iy=",iy," thissum=", thissum," isquare=",isquare," iloconsquare=",iloconsquare," iside=",iside," iloconsize=",iloconside)
    if (thissum > puzzleinput):
        print("Thissum > puzzlinput", thissum)
        break
    #print(bigmatrix)
    # choose next
    thesquare = squares[isquare]
    maxloc = 4*(thesquare[2] - 1) - 1

    iindex = iindex + 1
    iloconsquare = iloconsquare + 1
    iloconside = iloconside + 1

    if (iloconsquare > maxloc):
        # new square
        print("new square, iloconsquare=",iloconsquare," maxloc=",maxloc," sidelen=",thesquare[2])
        isquare = isquare + 1
        iloconsquare = 0
        iside = 0
        iloconside = 0
        thesquare = squares[isquare]
        ix = ix + 1
        iy = iy
        continue # new square, we are done here

    if (iloconside >= (thesquare[2]-1)):
        iside = iside + 1
        iloconside = 0

    # okay now update 
    if (iside == 0):
        ix = ix
        iy = iy + 1
    elif (iside == 1):
        ix = ix - 1
        iy = iy
    elif (iside == 2):
        ix = ix
        iy = iy - 1
    elif (iside == 3):
        ix = ix + 1
        iy = iy
    else:
        # nothing?
        pass
    


        





