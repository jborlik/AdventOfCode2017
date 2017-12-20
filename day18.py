

with open('day18.dat') as datafile:
    instructions = [ x.strip().split(' ') for x in datafile.readlines()]

registers = {}
currentline = 0
lastsound = 0

def representsInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def getRegisterOrNumber(regString):
    if representsInt(regString):
        return int(regString)
    # ok, a register name.  get it (or initialize to zero)
    if regString in registers:
        return registers[regString]
    else:
        registers[regString] = 0
        return 0


while (currentline >= 0) and (currentline < len(instructions)):
    anInstruction = instructions[currentline]
    if anInstruction[0] == 'snd':
        lastsound = getRegisterOrNumber(anInstruction[1])
        pass
    elif anInstruction[0] == 'set':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[2])
        pass
    elif anInstruction[0] == 'add':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[1]) + getRegisterOrNumber(anInstruction[2])
        pass
    elif anInstruction[0] == 'mul':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[1]) * getRegisterOrNumber(anInstruction[2])
        pass
    elif anInstruction[0] == 'mod':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[1]) % getRegisterOrNumber(anInstruction[2])
        pass
    elif anInstruction[0] == 'rcv':
        if getRegisterOrNumber(anInstruction[1]) != 0:
            print("RECOVERED SOUND ", lastsound)
            break
        pass
    elif anInstruction[0] == 'jgz':
        if getRegisterOrNumber(anInstruction[1]) > 0:
            currentline += getRegisterOrNumber(anInstruction[2])
            continue
        pass

    currentline += 1



