
def part1(thedata):
    len_st = len(thedata)

    totalcount = 0
    for index, c in enumerate(thedata):
        # print('index={}, c={}'.format(index,c))
        if index == len_st-1:
            nextchar = thedata[0]
        else:
            nextchar = thedata[index+1]
        if nextchar is c:
            totalcount = totalcount + int(c)
    return totalcount

def part2(thedata):
    len_data = len(thedata)
    totalcount = 0
    for index, c in enumerate(thedata):
        matchindex = 0
        if index < int(len_data/2):
            matchindex = index + int(len_data/2)
        else:
            matchindex = index - int(len_data/2)
        #print('index=',index,' matchindex=',matchindex)
        if c is thedata[matchindex]:
            totalcount = totalcount + int(c)
    return totalcount


with open('day1.txt') as datafile:
    alldata = datafile.readline().strip()



print("Sum of matches = ", part1(alldata))


print("Part 2!")

print("Trial1: ", part2('1212'))  # 6
print("Trial2: ", part2('1221'))  # 0
print("Trial3: ", part2('123425')) # 4
print("Trial4: ", part2('123123')) # 12
print("Part 2: ", part2(alldata))

