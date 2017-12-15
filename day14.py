
import day10
import binascii
import bitarray

def bincharsFromHexchar(aChar):
    val = int(aChar,16)
    stval = '{0:04b}'.format(val)
    return stval

#puzzlekey = 'flqrgnkx'  # for testing
puzzlekey = 'oundnydw'

countones = 0
grid = []
for irow in range(0,128):
    rowstring = "{0}-{1}".format(puzzlekey,irow)
    hashed = day10.knotHash(rowstring)
    rowinbinary = ''.join([bincharsFromHexchar(c) for c in hashed])
    countones += rowinbinary.count('1')
    grid.append(rowinbinary)

print("Number of ones=", countones)

seen = set()
groups = 0

def dfs(i,j):
    if ((i,j)) in seen:
        return
    if not grid[i][j] == '1':
        return
    seen.add((i,j))
    if i > 0:
        dfs(i-1,j)
    if j > 0:
        dfs(i,j-1)
    if i < 127:
        dfs(i+1,j)
    if j < 127:
        dfs(i,j+1)

for i in range(128):
    for j in range(128):
        if (i,j) in seen:
            continue
        if not grid[i][j] == '1':
            continue
        groups += 1
        dfs(i,j)

print("Groups = ", groups)