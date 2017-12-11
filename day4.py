
import itertools

ISPARTTWO = True

with open('day4.dat') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

goodcount = 0
for aPhrase in alldata:
    words = aPhrase.split()

    if ISPARTTWO:
        for i, aword in enumerate(words):
            words[i] = ''.join(sorted(aword))

    isokay = 1
    for (w1,w2) in itertools.permutations(words,2):
        if w1 == w2:
            isokay = 0
            break
    
    goodcount = goodcount + isokay

print("good passphrases = ", goodcount)

