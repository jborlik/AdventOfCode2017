

# instructions tuple:
# 0: register
# 1: inc/dec
# 2: amount
# 3---if
# 4: test register
# 5: >, <, >=, <=, ==, !=
# 6: test amount   

with open('day8.dat') as datafile:
    instructions = [x.split() for x in datafile.readlines()]

#instructions = [ ['b', 'inc', '5', 'if', 'a', '>', '1'], # test
#                ['a', 'inc', '1', 'if', 'b', '<', '5'], 
#                ['c', 'dec', '-10', 'if', 'a', '>=', '1'], 
#                ['c', 'inc', '-20', 'if', 'c', '==', '10']]

for i,v in enumerate(instructions):
    instructions[i][2] = int(v[2])
    instructions[i][6] = int(v[6])
    if v[1] == 'dec':
        instructions[i][2] = -1*instructions[i][2]

registers = {}
maxatanytime = 0

def getOrMakeRegisterValue(aName, registerDict):
    if aName in registerDict:
        return registerDict[aName]
    registerDict[aName] = 0
    return 0
def incrementRegisterValue(aName, iInc, registerDict):
    if aName not in registerDict:
        registerDict[aName] = 0
    registerDict[aName] = registerDict[aName] + iInc
    return registerDict[aName]

for aInstruction in instructions:
    testVal = getOrMakeRegisterValue(aInstruction[4], registers)
    bTest = False
    newval = 0
    if (aInstruction[5] == '>'):
        if testVal > aInstruction[6]:
            bTest = True
    elif (aInstruction[5] == '<'):
        if testVal < aInstruction[6]:
            bTest = True
    elif (aInstruction[5] == '>='):
        if testVal >= aInstruction[6]:
            bTest = True
    elif (aInstruction[5] == '<='):
        if testVal <= aInstruction[6]:
            bTest = True
    elif (aInstruction[5] == '=='):
        if testVal == aInstruction[6]:
            bTest = True
    elif (aInstruction[5] == '!='):
        if testVal != aInstruction[6]:
            bTest = True
    if bTest:
        newval = incrementRegisterValue(aInstruction[0], aInstruction[2], registers)
    if newval > maxatanytime:
        maxatanytime = newval

print(registers)

print("Max ending value=", max(registers.values()), " for key=", max(registers, key=registers.get))

print("Max at anytime=", maxatanytime)
