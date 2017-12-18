
from collections import deque

stepsize = 380
#stepsize = 3  #test

currentposition = 0
state = [ 0 ]
nextval = 1

def spin():
    global currentposition, state, nextval
    newpos = (currentposition + stepsize) % len(state)
    state.insert(newpos+1, nextval)
    currentposition = newpos + 1
    nextval += 1

for i in range(0,2018):
    #print("Pos=",currentposition," state=",state)
    spin()

iloc = state.index(2017)
print("Location after 2017=",iloc+1)
print("Value after 2017=",state[iloc+1])


#  This approach had very poor performance
#for i in range(2018,50000000):
#    if i % 10000 == 0:
#        print(i, " val1=", state[1])
#    spin()
#print("Value after 0=",state[1])  # 665, 492690, 754184, 1139394

spinlock = deque([0])
for i in range(1,50000001):
    spinlock.rotate(-stepsize)
    spinlock.append(i)

print(spinlock[spinlock.index(0) + 1])