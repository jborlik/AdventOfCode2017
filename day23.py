
with open('day23.dat') as datafile:
    instructions = [ x.strip().split(' ') for x in datafile.readlines()]

#instructions = [ ['snd', '1'], 
#    ['snd', '2'],
#    ['snd', 'p'],
#    ['rcv', 'a'],
#    ['rcv', 'b'],
#    ['rcv', 'c'],
#    ['rcv', 'd']]
isPartTwo = False

registers = {'a': 0, 'h': 0}
if isPartTwo:
    registers['a'] = 1
currentline = 0
isrunning = True

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

multimes = 0

execcount = 0

while isrunning:
    anInstruction = instructions[currentline]
    execcount += 1
    if execcount % 10000 == 0:
        print("Line ", currentline," instruction: ", anInstruction, " h=", registers['h'])

    if anInstruction[0] == 'set':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[2])
        pass
    elif anInstruction[0] == 'sub':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[1]) -  \
                                            getRegisterOrNumber(anInstruction[2])
        pass
    elif anInstruction[0] == 'mul':
        registers[anInstruction[1]] = getRegisterOrNumber(anInstruction[1]) * \
                                                        getRegisterOrNumber(anInstruction[2])
        multimes += 1
        pass
    elif anInstruction[0] == 'jnz':
        if getRegisterOrNumber(anInstruction[1]) != 0:
            currentline += getRegisterOrNumber(anInstruction[2])
            if currentline < 0 or currentline >= len(instructions):
                # this thread is finished
                print("Thread terminated by jump")
                isrunning = False
            continue
        pass
    else:
        print("WHAAAA???")
    
    currentline += 1
    if currentline >= len(instructions):
        # thread is finished
        print("Thread terminated by exhaustion")
        isrunning = False

print("Times mul called=", multimes)
print(registers)