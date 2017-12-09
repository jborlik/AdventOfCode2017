import itertools

def part1(thedata):
    checksum = 0
    for arow in thedata:
        # print('index={}, c={}'.format(index,c))
        cells = arow.split()
        max = 0
        min = 100000
        for acell in cells:
            if int(acell) > max:
                max = int(acell)
            if int(acell) < min:
                min = int(acell)
        #print('Row: max=', max, ' min=',min)
        checksum = checksum + (max-min)
    return checksum

def part2(thedata):
    checksum = 0
    for arow in thedata:
        cells = arow.split()
        for (c1,c2) in itertools.permutations(cells,2):
            (quot, remain) = divmod(int(c1), int(c2))
            if remain == 0:
                checksum = checksum + quot
#                print('c1={},c2={},quot={},remain={}'.format(c1,c2,quot,remain))
                break
    return checksum




with open('day2.dat') as datafile:
    alldata = [x.strip() for x in datafile.readlines()]

test1 = [ '5 1 9 5', '7 5 3', '2 4 6 8']   # should result in 9

print("Part 1!")

print("Checksum test1= ", part1(test1))
print("Checksum = ", part1(alldata))


print("Part 2!")

test2 = ['5 9 2 8', '9 4 7 3', '3 8 6 5']

print("Test2 checksum=", part2(test2))
print("Checksum = ", part2(alldata))