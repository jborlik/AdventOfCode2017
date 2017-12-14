
depths = [0] * 100

with open('day13.dat') as datafile:
    for aline in datafile.readlines():
        pieces = aline.split(': ')
        depths[int(pieces[0])] = int(pieces[1])

#depths = [3, 2, 0, 0, 4, 0, 4]

def calculateSeverity(startTime):
    severity = 0
    iscaught = False
    for layer in range(0, len(depths)):
        # i'm at layer 'time', where is this depth's scanner?
        time = layer + startTime
        if depths[layer] != 0:
            loc = time % (depths[layer] + (depths[layer]-2))
            if loc == 0:
                # scanner got me!
                severity += depths[layer]*layer
                iscaught = True
    return severity, iscaught

print("Severity = ", calculateSeverity(0))


for startTime in range(0,11000000000):
    (isev,iscaught) = calculateSeverity(startTime)
    print("Delay ", startTime, " sev=", isev)
    if (isev == 0) and (iscaught == False):
        break

# 426840 too low