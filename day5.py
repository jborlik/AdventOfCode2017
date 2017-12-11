

with open('day5.dat') as datafile:
    instructions = [int(x.strip()) for x in datafile.readlines()]

ISPARTTWO = True

location = 0
maxlocation = len(instructions)
jumps = 0
while (location < maxlocation) and (location >= 0):

    myinstruction = instructions[location]

    if ISPARTTWO:
        if myinstruction >= 3:
            instructions[location] = instructions[location] - 1
        else:
            instructions[location] = instructions[location] + 1
    else:
        instructions[location] = instructions[location] + 1

    location = location + myinstruction
    jumps = jumps + 1

print("Jumps til out of list: ",jumps)



