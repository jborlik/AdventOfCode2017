

with open('day6.dat') as datafile:
    banks = [int(x) for x in datafile.readline().strip().split()]

#banks = [0, 2, 7, 0]  # test

def realloccycle(thebanks):
    maxii = thebanks.index(max(thebanks))
    # distribute this to the others
    amounttorealloc = thebanks[maxii]
    thebanks[maxii] = 0
    theindex = maxii + 1
    while amounttorealloc > 0:
        if theindex > len(thebanks)-1:
            theindex=0
        thebanks[theindex] = thebanks[theindex] + 1
        amounttorealloc = amounttorealloc - 1
        theindex =theindex + 1

print("Cycle 0: banks=", banks)
memory = []
memory.append(' '.join(str(x) for x in banks))

for i in range(1,1000000):
    realloccycle(banks)
    print("Cycle ", i, ": banks=", banks)
    thisstate = ' '.join(str(x) for x in banks)
    try:
        locinmemory = memory.index(thisstate)
        print("FOUND LOOP FROM LOC: ", locinmemory, " to step: ", i, " len=",i-locinmemory)
        break
    except (ValueError):
        memory.append(thisstate)
        pass # no loop





    

