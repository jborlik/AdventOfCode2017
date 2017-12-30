
pad = 500
with open('day22.dat') as datafile:
    knownservers = [ x.strip() for x in datafile.readlines() ]    #servers[row][col]

isPartTwo = True

#knownservers = [ '..#', '#..', '...']
maxsteps = 10001
states = [ '.', '#' ]
if isPartTwo:
    states = ['.', 'W', '#', 'F']
    maxsteps = 10000001


cleanrow = '.' * (pad+len(knownservers[0])+pad)
servers = []
for i in range(0,pad):
    servers.append(cleanrow)
for aknown in knownservers:
    servers.append( '.'*pad + aknown + '.'*pad )
for i in range(0,pad):
    servers.append(cleanrow)

position = [int(len(servers)/2), int(len(servers[0])/2)]
directions = [ [-1,0], [0,1], [1,0], [0,-1] ]  # n, e, s, w
currentdirection = 0  # start moving north

infectioncount = 0
for iburst in range(1,maxsteps):
    if iburst % 1000 == 0:
        print("{}: {}x{} moving {}".format(iburst, position[0], position[1], currentdirection))
    #print("\n".join(servers))
    aCurr = servers[position[0]][position[1]]
    if aCurr == '#':  # infected
        currentdirection = (currentdirection + 4 +1) % 4
        tmpstr = list(servers[position[0]])
        tmpstr[position[1]] = '.'
        if isPartTwo:
            tmpstr[position[1]] = 'F'
        servers[position[0]] = ''.join(tmpstr)
    elif aCurr == '.':  # clean
        currentdirection = (currentdirection + 4 -1) % 4
        tmpstr = list(servers[position[0]])
        tmpstr[position[1]] = '#'
        if isPartTwo:
            tmpstr[position[1]] = 'W'
        else:
            infectioncount += 1
        servers[position[0]] = ''.join(tmpstr)
    elif aCurr == 'W': # weakened
        currentdirection = (currentdirection + 4 +0) % 4
        tmpstr = list(servers[position[0]])
        tmpstr[position[1]] = '#'
        servers[position[0]] = ''.join(tmpstr)
        infectioncount += 1
    elif aCurr == 'F': # flagged
        currentdirection = (currentdirection + 4 +2) % 4
        tmpstr = list(servers[position[0]])
        tmpstr[position[1]] = '.'
        servers[position[0]] = ''.join(tmpstr)
    else:
        print("WAAA?? aCurr=",aCurr)
        continue
    # take a step in the new direction
    position[0] += directions[currentdirection][0]
    position[1] += directions[currentdirection][1]

print("infection count=",infectioncount)   # part one= 5352
