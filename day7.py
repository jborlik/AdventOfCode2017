
import re

re_parseprog = re.compile(r'(\w+) \((\w+)\)')

class Prog:
    def __init__(self, lineToParse):
        self.name = ''
        self.parent = ''
        self.weight = 0
        self.children = []
        self.weightWithChildren = 0
        locofarrow = lineToParse.find("->")
        if (locofarrow is not -1):
            # have children
            linechildren = lineToParse[locofarrow+3:]
            self.children = linechildren.split(', ')
        for m in re_parseprog.findall(lineToParse):
            self.name = m[0]
            self.weight = int(m[1])

    def __str__(self):
        return "{0} ({1}) parent={2} -> {3}\n".format(self.name, self.weight, self.parent, self.children)
    def __repr__(self):
        return "{0} ({1}) parent={2} -> {3}\n".format(self.name, self.weight, self.parent, self.children)



with open('day7.dat') as datafile:
    programs = {x.strip().split()[0]: Prog(x.strip()) for x in datafile.readlines()}

teststring = """pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)
"""
#programs = {x.strip().split()[0]: Prog(x.strip()) for x in teststring.splitlines()}

def determineParents(progDic):
    for k,v in progDic.items():
        for aChild in v.children:
            progDic[aChild].parent = k

determineParents(programs)
print(programs)

def findRoot(progDic):
    for k,v in progDic.items():
        if v.parent == "":
            return v
    return None

theRoot = findRoot(programs)
print("ROOT=", theRoot)  # part one

def findWeightWithChildren(prog, progDic):
    eachchildweighs = 0
    totweight = prog.weight
    firstchild = ''
    for aChild in prog.children:
        childweight = findWeightWithChildren(progDic[aChild], progDic)
        if eachchildweighs == 0:
            eachchildweighs = childweight
            firstchild = aChild
        if eachchildweighs != childweight:
            print("WARNING! {0} child {1} MISMATCH val={2} should be {3} from {4}".format(
                prog.name, aChild, childweight, eachchildweighs, firstchild))
            print("   ({2} discweight={3}, {0} discweight={1})".format(
                firstchild, progDic[firstchild].weight,
                aChild, progDic[aChild].weight
                ))    
        totweight = totweight + childweight
    prog.weightWithChildren = totweight
    return prog.weightWithChildren

findWeightWithChildren(theRoot, programs)



