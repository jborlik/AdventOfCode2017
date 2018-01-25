import copy

with open('day24.dat') as datafile:
    components = [ tuple(map(int,x.strip().split('/'))) for x in datafile.readlines() ]

teststring = """0/2
2/2
2/3
3/4
3/5
0/1
10/1
9/10
"""

#components = [ tuple(map(int,x.strip().split('/'))) for x in teststring.splitlines() ]

print(components)

candidates = []

def findLinkableCandidate(matchInt, thisBridge, availableComponents):
    """Find any available component that matches the needed number, and append it to
        the candidate array.  Recursive (as it will try to find candidates that match the other
        number in the component). """
    for aComp in availableComponents:
        foundInt = -1
        if aComp[0]==matchInt:
            foundInt = 0
        elif aComp[1]==matchInt:
            foundInt = 1
        
        if foundInt >= 0:
            newBridge = copy.copy(thisBridge)
            newBridge.append(aComp)
            newAvailableComponents = copy.copy(availableComponents)
            newAvailableComponents.remove(aComp)
            candidates.append(newBridge)
            findLinkableCandidate(aComp[1-foundInt], newBridge, newAvailableComponents)

def countBridgeStrength(aBridge):
    return sum([x[0]+x[1] for x in aBridge])


findLinkableCandidate(0, [], components)

print("number of potential bridges:", len(candidates))

maxstrength = 0
maxbridge = []
for aCandidate in candidates:
    aStr = countBridgeStrength(aCandidate)
    if aStr > maxstrength:
        maxstrength = aStr
        maxbridge = aCandidate

print("Max strength=", maxstrength)
print("Max bridge=", maxbridge)