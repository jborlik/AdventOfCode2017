

with open('day18.dat') as datafile:
    instructions = [ x.strip().split(' ') for x in datafile.readlines()]

#instructions = [ ['snd', '1'], 
#    ['snd', '2'],
#    ['snd', 'p'],
#    ['rcv', 'a'],
#    ['rcv', 'b'],
#    ['rcv', 'c'],
#    ['rcv', 'd']]

registers = [ {'p': 0}, {'p':1} ]
currentline = [ 0, 0 ]
sndqueue = [ [], [] ]
activeregister = 0
isrunning = [True, True]
isblocked = [False, False]

sndcount = 0

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def getRegisterOrNumber(regString, whichregister):
    if representsInt(regString):
        return int(regString)
    # ok, a register name.  get it (or initialize to zero)
    if regString in registers[whichregister]:
        return registers[whichregister][regString]
    else:
        registers[whichregister][regString] = 0
        return 0


while (isrunning[0] == True) or (isrunning[1] == True):
    anInstruction = instructions[currentline[activeregister]]
    #print("Thread ", activeregister, " line=", currentline[activeregister], " ins=", anInstruction[0])
    if anInstruction[0] == 'snd':
        snd = getRegisterOrNumber(anInstruction[1],activeregister)
        sndqueue[1-activeregister].append(snd)  # add it to the other register's queue
        #print("Sending from thread ", activeregister," value=",snd)
        if activeregister == 1:
            sndcount += 1
        pass
    elif anInstruction[0] == 'set':
        registers[activeregister][anInstruction[1]] = getRegisterOrNumber(anInstruction[2],activeregister)
        pass
    elif anInstruction[0] == 'add':
        registers[activeregister][anInstruction[1]] = getRegisterOrNumber(anInstruction[1],activeregister) +  \
                                                        getRegisterOrNumber(anInstruction[2],activeregister)
        pass
    elif anInstruction[0] == 'mul':
        registers[activeregister][anInstruction[1]] = getRegisterOrNumber(anInstruction[1],activeregister) * \
                                                        getRegisterOrNumber(anInstruction[2],activeregister)
        pass
    elif anInstruction[0] == 'mod':
        registers[activeregister][anInstruction[1]] = getRegisterOrNumber(anInstruction[1],activeregister) % \
                                                        getRegisterOrNumber(anInstruction[2],activeregister)
        pass
    elif anInstruction[0] == 'rcv':
        #if getRegisterOrNumber(anInstruction[1],activeregister) != 0:
        #    print("RECOVERED SOUND ", lastsound)
        #    break
        if len(sndqueue[activeregister]) > 0:
            theval = sndqueue[activeregister].pop(0)
            registers[activeregister][anInstruction[1]] = theval
            pass
        else:
            # nothing queued, so check for deadlock or switch to other thread
            #if isrunning[1-activeregister] and sndqueue[1-activeregister]
            if not isrunning[1-activeregister]:
                # other thread can't help
                print("Thread ",activeregister," waiting on terminated thread")
                isrunning[activeregister] = False
                continue
            elif isblocked[1-activeregister] and len(sndqueue[1-activeregister])==0:
                print("DEADLOCK")
                isrunning[activeregister] = False
                isblocked[1-activeregister] = False
                activeregister = 1 - activeregister
                continue
            else:
                #print("switching from thread ", activeregister, ", q1=",len(sndqueue[0]),", q2=",len(sndqueue[1]))
                isblocked[activeregister] = True
                isblocked[1-activeregister] = False
                activeregister = 1 - activeregister
                #break
                continue
            pass
        pass
    elif anInstruction[0] == 'jgz':
        if getRegisterOrNumber(anInstruction[1],activeregister) > 0:
            currentline[activeregister] += getRegisterOrNumber(anInstruction[2],activeregister)
            if currentline[activeregister] < 0 or currentline[activeregister] >= len(instructions):
                # this thread is finished
                print("Thread ", activeregister, " terminated by jump")
                isrunning[activeregister] = False
                # switch to other
                isblocked[1-activeregister] = False
                activeregister = 1-activeregister
            continue
        pass

    currentline[activeregister] += 1
    if currentline[activeregister] >= len(instructions):
        # thread is finished
        print("Thread ", activeregister, " terminated by exhaustion")
        isrunning[activeregister] = False
        isblocked[1-activeregister] = False
        activeregister = 1-activeregister



print("Sends from thread 1=", sndcount)
print("Registers for prog 0: ", registers[0])
print("Registers for prog 1: ", registers[1])