
import re

def cleanText(theText):
    # remove commented chars
    text_uncomments = re.sub(r'\!.', '', theText)
    # now remove garbage and extra text
    resultText = ''
    ingarbage = False
    garbageChars = 0
    for aChar in text_uncomments:
        if ingarbage:
            if aChar == '>':
                ingarbage = False
                continue
            garbageChars += 1
        else:
            if aChar == '<':
                ingarbage = True
                continue
            if (aChar=='{') or (aChar=='}'): #or (aChar==","):
                resultText += aChar
    return (resultText, garbageChars)

def scoreText(theText):
    totalScore = 0
    currentDepth = 1
    for aChar in theText:
        if aChar == '{':
            totalScore += currentDepth
            currentDepth += 1
        elif aChar == '}':
            currentDepth -= 1
    return totalScore


with open('day9.dat') as datafile:
    puzzleinput = datafile.readline().strip()

test1 = '{}' #, score of 1.
print(scoreText(cleanText(test1)[0]))
test1 = '{{{}}}' #, score of 1 + 2 + 3 = 6.
print(scoreText(cleanText(test1)[0]))
test1 = '{{},{}}' #, score of 1 + 2 + 2 = 5.
print(scoreText(cleanText(test1)[0]))
test1 = '{{{},{},{{}}}}' #, score of 1 + 2 + 3 + 3 + 3 + 4 = 16.
print(scoreText(cleanText(test1)[0]))
test1 = '{<a>,<a>,<a>,<a>}' #, score of 1.
print(scoreText(cleanText(test1)[0]))
test1 = '{{<ab>},{<ab>},{<ab>},{<ab>}}' #, score of 1 + 2 + 2 + 2 + 2 = 9.
print(scoreText(cleanText(test1)[0]))
test1 = '{{<!!>},{<!!>},{<!!>},{<!!>}}' #, score of 1 + 2 + 2 + 2 + 2 = 9.
print(scoreText(cleanText(test1)[0]))
test1 = '{{<a!>},{<a!>},{<a!>},{<ab>}}' #, score of 1 + 2 = 3.
print(scoreText(cleanText(test1)[0]))

print("Puzzle score: ", scoreText(cleanText(puzzleinput)[0]))
print("Garbage removed: ", cleanText(puzzleinput)[1])