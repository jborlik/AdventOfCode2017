
state ='A'
maxsteps = 12964419 

transitions = {
    'A': [  (1,1,'B'),  (0,1,'F') ],
    'B': [  (0,-1,'B'), (1,-1,'C') ],
    'C': [  (1,-1,'D'), (0,1,'C') ],
    'D': [  (1,-1,'E'), (1,1,'A') ],
    'E': [  (1,-1,'F'), (0,-1,'D')],
    'F': [  (1,1,'A'),  (0,-1,'E')]
}

DOTEST = False
if DOTEST:
    maxsteps = 6
    transitions = {
        'A': [ (1,1,'B'), (0,-1,'B') ],
        'B': [ (1,-1,'A'), (1,1,'A') ]
    }


tape = {}
cursor = 0
steps = 0

while steps < maxsteps:
    steps += 1
    locVal = tape.get(cursor, 0)
    action = transitions[state][locVal]
    tape[cursor] = action[0]
    cursor += action[1]
    state = action[2]

print("After {} steps, checksum={}".format(steps, sum(tape.values()) ))
