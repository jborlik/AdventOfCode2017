"""
    This implements AoC Day 10, which is a "knot hash" algorithm.

"""


def twistRound(theCircle, theCurrPos, theSkipsize, theTwistLengths):

    circlesize = 256

    def wrapIndex(index):
        return index % circlesize

    for aTwist in theTwistLengths:
        cache = []
        for i in range(theCurrPos, theCurrPos+aTwist):
            cache.append(theCircle[wrapIndex(i)])
        cache.reverse()
        for i in range(0, aTwist):
            theCircle[wrapIndex(theCurrPos+i)] = cache[i]
        theCurrPos = wrapIndex(theCurrPos + aTwist + theSkipsize)
        theSkipsize += 1
    return (theCurrPos,theSkipsize)


def parseHashInputString(theInput):
    retval = []
    for aChar in theInput:
        retval.append( ord(aChar) )
    return retval


def knotHash(theInput):
    """
        Given a string argument, theInput, this function will
        implement a 256-bit hash scheme and return the result
        as a 32-character string of hexidecimal characters.
    """

    twistlengths = parseHashInputString(theInput)
    twistlengths.extend([17, 31, 73, 47, 23])

    circlesize = 256
    circle = list(range(0,circlesize))
    currentposition = 0
    skipsize = 0

    # 64 rounds
    for iround in range(0,64):
        (currentposition,skipsize) = twistRound(circle,currentposition,skipsize,twistlengths)
    # for test purposes:  circle[0:16] = [65,27,9,1,4,3,40,50,91,7,6,0,2,5,68,22]
    # sparse hash to dense hash
    densehash = []
    sparseindex = 0
    for ii in range(0,16):
        densehash.append(circle[sparseindex])
        sparseindex += 1
        for j in range(1,16):
            densehash[ii] = densehash[ii] ^ circle[sparseindex]
            sparseindex += 1

    return ''.join("{:02x}".format(c) for c in densehash)



if __name__ == "__main__":


    puzzleinput = '34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167'
    twistlengths = [int(x) for x in puzzleinput.split(',')]
    circlesize = 256

    #twistlengths = [int(x) for x in '3,4,1,5'.split(',')]
    #circlesize = 5

    circle = list(range(0,circlesize))
    currentposition = 0
    skipsize = 0
        
    twistRound(circle, currentposition, skipsize, twistlengths)

    print("Product of first two numbers: ", circle[0]*circle[1])

    ##=================================================================
    print("***** PART TWO *******")

    puzzleinput = '34,88,2,222,254,93,150,0,199,255,39,32,137,136,1,167'
    #puzzleinput = 'AoC 2017'


    # output hash in hex
    print("Hash value:", knotHash(puzzleinput))

