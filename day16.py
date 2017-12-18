
with open('day16.dat') as datafile:
    instructions = datafile.readline().strip().split(',')

#instructions = ["s1", "x3/4", "pe/b"] # test

programs = "abcdefghijklmnop"
#programs = "abcde" # test
#programs = "padheomkgjfnblic"

previous = [ programs ]

def indexInPrevious(thisState, prevArray):
    retval = -1
    try:
        retval = prevArray.index(thisState)
    except:
        pass
    return retval

for icount in range(0,1000000000):

    for anInstruction in instructions:
        if anInstruction[0] == "s":
            # spin
            iSpins = int(anInstruction[1:])
            endprog = programs[-iSpins:]
            startprog = programs[0:len(programs)-iSpins]
            programs = "{}{}".format(endprog, startprog)
            pass
        elif anInstruction[0] == "x":
            # exchange by position
            indexes = [int(i) for i in anInstruction[1:].split("/")]
            plist = list(programs)
            spot = plist[indexes[0]]
            plist[indexes[0]] = plist[indexes[1]]
            plist[indexes[1]] = spot
            programs = ''.join(plist)
            pass
        elif anInstruction[0] == "p":
            # exchange by name
            names = anInstruction[1:].split("/")
            i1 = programs.find(names[0])
            i2 = programs.find(names[1])
            plist = list(programs)
            plist[i1] = programs[i2]
            plist[i2] = programs[i1]
            programs = ''.join(plist)
            pass

    lastOccurrance = indexInPrevious(programs,previous)
    if lastOccurrance != -1:
        print("REPEAT From iteration ", lastOccurrance)
        break

    print("Icount=",icount, " programs=", programs)
    previous.append(programs)


print("Result: ", programs, " at icount=", icount)

print("Cycle location of a billion: ", 1000000000 % (icount+1))
print("  programs=",previous[1000000000 % (icount+1)])