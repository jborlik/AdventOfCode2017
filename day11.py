

with open('day11.dat') as datafile:
    instructions = datafile.readline().strip().split(',')

#instructions = 'ne,ne,ne'.split(',')  # test, 3 steps away
#instructions = 'ne,ne,sw,sw'.split(',') # test, 0 steps
#instructions = 'ne,ne,s,s'.split(',') # test, 2 steps
#instructions = 'se,sw,se,sw,sw'.split(',') # test, 3 steps

class Hex:
    def __init__(self, q, r, s=None):
        self.q = q
        self.r = r
        if s:
            self.s = s
        else:
            self.s = -q - r
    def length(self):
        return int( (abs(self.q) + abs(self.r) + abs(self.s)) / 2)

def hex_subtract(hex1:Hex, hex2:Hex):
    return Hex(hex1.q - hex2.q, hex1.r - hex2.r, hex1.s - hex2.s)

def hex_distance(hex1:Hex, hex2:Hex):
    return hex_subtract(hex1, hex2).length()

def hex_add(hex1:Hex, hex2:Hex):
    return Hex(hex1.q + hex2.q, hex1.r + hex2.r, hex1.s + hex2.s)

# 0=ne, 1=n, 2=nw, 3=sw, 4=s, 5=se
hex_directions = [Hex(1,0),Hex(1,-1),Hex(0,-1),Hex(-1,0),Hex(-1,1),Hex(0,1)]
hex_dirstring = ['ne','n','nw','sw','s','se']


# do it
location = Hex(0,0)
furthest = 0

for aStep in instructions:
    dirint = hex_dirstring.index(aStep)
    location = hex_add(location, hex_directions[dirint])
    if location.length() > furthest:
        furthest = location.length()

print("Final location: ", location, " distance=", location.length())

print("Greatest distance =", furthest)

