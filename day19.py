

with open('day19.dat') as datafile:
    map = datafile.readlines()    #map[row][col]

#map = [
#"     |          ",
#"     |  +--+    ",
#"     A  |  C    ",
#" F---|----E|--+ ",
#"     |  |  |  D ",
#"     +B-+  +--+ "
#]

# dirs: 0=N, 1=E, 2=S, 3=W
dirs = [ (-1,0), (0,1), (1,0), (0,-1)]
pipelook = [ '|', '-', '|', '-']

# starting point
rowloc = 0
colloc = map[0].find("|")
heading = 2 #dirs[2] # south

collected = ''
steps = 0

while rowloc>=0 and colloc>=0 and rowloc<len(map) and colloc<len(map[0]):
    aHere = map[rowloc][colloc]
    if aHere == "|" or aHere == "-":
        # continue on your way
        rowloc += dirs[heading][0]
        colloc += dirs[heading][1]
        steps += 1
    elif aHere == '+':
        # which direction to go next?
        m90dir = (heading+4-1) % 4
        im90row = rowloc + (dirs[ m90dir ][0])
        im90col = colloc + (dirs[ m90dir ][1])
        am90 = map[im90row][im90col]
        if am90.isalpha() or am90 == pipelook[ m90dir ]:
            # okay, next dir is that dir
            heading = m90dir
            rowloc += dirs[heading][0]
            colloc += dirs[heading][1]
            steps += 1
        else:
            p90dir = (heading+4+1) % 4
            ip90row = rowloc + (dirs[ p90dir ][0])
            ip90col = colloc + (dirs[ p90dir ][1])
            ap90 = map[ip90row][ip90col]
            if ap90.isalpha() or ap90 == pipelook[p90dir]:
                heading = p90dir
                rowloc += dirs[heading][0]
                colloc += dirs[heading][1]
                steps += 1
            else:
                print("HUHHH? ({},{})={}".format(rowloc,colloc,aHere))
                break
        pass
    elif aHere.isalpha():
        collected += aHere
        # continue
        rowloc += dirs[heading][0]
        colloc += dirs[heading][1]
        steps += 1
    else:
        print("Blank? (",aHere,"), terminating")
        break

print("Collected: ", collected)
print("Steps=",steps)