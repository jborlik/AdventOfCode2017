
import re

re_parseitem = re.compile(r'(\d+) <-> (.+)')

with open('day12.dat') as datafile:
    connections = { re_parseitem.findall(x)[0][0]: 
                        re_parseitem.findall(x)[0][1].split(", ")
                            for x in datafile.readlines() }

def walkList(nodeName, traveledList):
    traveledList.append(nodeName)
    for aChild in connections[nodeName]:
        if aChild not in traveledList:
            walkList(aChild, traveledList)

traveledList = []
walkList('0', traveledList)

print(traveledList)
print("Node 0 connects to ", len(traveledList), " items")

print("**** PART TWO *****")

def removeListFromDictionary(listOfKeys, aDictionary):
    for aKey in listOfKeys:
        aDictionary.pop(aKey, None)

groups = {}
groups['0'] = traveledList

removeListFromDictionary(traveledList, connections)

while len(connections) > 0:
    traveledList = []
    rootnode = list(connections.keys())[0]
    walkList(rootnode, traveledList)
    print("Node ", rootnode," connects to ", len(traveledList), " items")
    groups[rootnode] = traveledList
    removeListFromDictionary(traveledList, connections)

print("Total groups = ", len(groups))