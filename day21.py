
import numpy as np
#    ##/## => .../.../.#.
#    .../.../... => #.#./.###/..##/#.##

# 1 2   3 4     2 1     3 1     4 3     2 4     1 3
# 3 4   1 2     4 3     4 2     2 1     1 3     2 4 

# 1 2 3     7 4 1   9 8 7   3 6 9
# 4 5 6     8 5 2   6 5 4   2 5 8
# 7 8 9     9 6 3   3 2 1   1 4 7
#
# 3 2 1     9 6 3   7 8 9   1 4 7
# 6 5 4     8 5 2   4 5 6   2 5 8
# 9 8 7     7 4 1   1 2 3   3 6 9
#
# 7 8 9     1 4 7   3 2 1   9 6 3  # all of these are repeats of above!
# 4 5 6     2 5 8   6 5 4   8 5 2
# 1 2 3     3 6 9   9 8 7   7 4 1


rotations2x2 = [ [1,2,3,4], [3,4,1,2], [2,1,4,3], [3,1,4,2], [4,3,2,1], [2,4,1,3], [1,3,2,4] ]
rotations3x3 = [ [1,2,3, 4,5,6, 7,8,9], [7,4,1, 8,5,2, 9,6,3],
                 [9,8,7, 6,5,4, 3,2,1], [3,6,9, 2,5,8, 1,4,7],
                 [3,2,1, 6,5,4, 9,8,7], [9,6,3, 8,5,2, 7,4,1],
                 [7,8,9, 4,5,6, 1,2,3], [1,4,7, 2,5,6, 3,6,9] ] 


rules2x2 = {}
rules3x3 = {}


def parseRule(inputstr, outputstr, rules2, rules3):
    inputrows = inputstr.split('/')
    istr = ''.join( c for c in inputstr if c not in '/')
    if len(inputrows)==2:
        for aRot in rotations2x2:
            astring = '{}{}/{}{}'.format(istr[aRot[0]-1], istr[aRot[1]-1], istr[aRot[2]-1], istr[aRot[3]-1])
            rules2x2[astring] = outputstr
    elif len(inputrows)==3:
        for aRot in rotations3x3:
            a = '{}{}{}/{}{}{}/{}{}{}'.format(istr[aRot[0]-1],istr[aRot[1]-1],istr[aRot[2]-1],
                                              istr[aRot[3]-1],istr[aRot[4]-1],istr[aRot[5]-1],
                                              istr[aRot[6]-1],istr[aRot[7]-1],istr[aRot[8]-1])
            rules3x3[a] = outputstr
    else:
        print("What?  len(inputrows)=",len(inputrows))
        return
    pass

def stringToArray(inputstr):
    inputrows = inputstr.split('/')
    outArr = np.zeros( (len(inputrows),len(inputrows)), dtype=int)
    for rowindex, aRow in enumerate(inputrows):
        for colindex, aChar in enumerate(aRow):
            if aChar == '#':
                outArr[rowindex,colindex] = 1
    return outArr

def arrayToString(inputArr):
    outStr = ''
    for irow in range(0,len(inputArr)):
        for icol in range(0,len(inputArr)):
            if inputArr[irow,icol] == 1:
                outStr += '#'
            else:
                outStr += '.'
        if irow != len(inputArr)-1: outStr += '/'
    return outStr

def reassemblyArrayFromListOfStrings(subarrstrs, numsubarrs, newxbyx):
    outArr = np.zeros( ( newxbyx*numsubarrs, newxbyx*numsubarrs ), dtype=int)

    for ibigrows in range(0,numsubarrs):
        # for this row of subarrays, get all the actual subarrays
        for ibigcol in range(0,numsubarrs):
            thissubarr = stringToArray(subarrstrs[ibigrows*numsubarrs+ibigcol])

            # ok fill it in
            for ilittlerow in range(0,newxbyx):
                for ilittlecol in range(0,newxbyx):
                    outArr[ibigrows*newxbyx+ilittlerow, ibigcol*newxbyx+ilittlecol] = thissubarr[ilittlerow,ilittlecol]
        
    return outArr


with open('day21.dat') as datafile:
    for x in datafile.readlines():
        io = x.strip().split(' => ')
        parseRule(io[0], io[1], rules2x2, rules3x3)

# test rules
DOTEST = False
if DOTEST:
    rules2x2 = {}
    rules3x3 = {}
    testruletext = ['../.# => ##./#../...', '.#./..#/### => #..#/..../..../#..#' ]
    for x in testruletext:
        io = x.strip().split(' => ')
        parseRule(io[0], io[1], rules2x2, rules3x3)

print("2x2 rules=====")
print(rules2x2)

print("ITERATION=========")
arrstr = '.#./..#/###'
arr = stringToArray(arrstr)

for iiter in range(0,18):
    isize = len(arr)
    xbyx = 2
    rules = rules2x2
    if (isize % 2)==0:
        # divide into 2x2
        xbyx = 2
    else:
        # divide into 3x3
        xbyx = 3
        rules = rules3x3

    numsubarrs = int(isize / xbyx)
    newsubarrs = []
    for irow in range(0,numsubarrs):
        for jcol in range(0,numsubarrs):
            thissubarr = arr[irow*xbyx:irow*xbyx+xbyx, jcol*xbyx:jcol*xbyx+xbyx]
            #print("[{},{}] is {} => ".format(irow*xbyx, jcol*xbyx, thissubarr), end='')
            newsubarrstr = rules[arrayToString(thissubarr)]
            #print(newsubarrstr)
            newsubarrs.append(newsubarrstr)

    arr = reassemblyArrayFromListOfStrings(newsubarrs, numsubarrs, xbyx+1)
    sumvals = np.sum(arr)
    print(arrayToString(arr))
    print("Iter {}.  Sum={}".format(iiter+1,sumvals))
    