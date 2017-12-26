
#p=<-1021,-2406,1428>, v=<11,24,-73>, a=<4,9,0>

import re
import itertools
import math

re_parseitem = re.compile(r'<([\-\d,]+)>')

particles = []    # particles[iparticle][0=pos,1=vel,2=accel][0=x,1=y,2=z]
with open('day20.dat') as datafile:
    for x in datafile.readlines():
        m1 = re_parseitem.findall(x)
        particles.append([ list(map(int,m1[0].split(","))), 
                           list(map(int,m1[1].split(","))), 
                           list(map(int,m1[2].split(","))) ])
#    particles = [ y.split(",") for x in datafile.readlines() for y in re_parseitem.findall(x)]


# find particle that says closest to origin "in the long run"
minaccelparticle = 0
minaccel = 1000000
for idx, aPart in enumerate(particles):
    accel_mag = sum(map(abs,aPart[2]))
    if (accel_mag <= minaccel):
        minaccel = accel_mag
        minaccelparticle = idx

print("Min index=", minaccelparticle)

# Part2:  move particles through time to find collisions
def tick():
    for aPart in particles:
        # increase velocity
        aPart[1][0] += aPart[2][0]
        aPart[1][1] += aPart[2][1]
        aPart[1][2] += aPart[2][2]
        # increase position
        aPart[0][0] += aPart[1][0]
        aPart[0][1] += aPart[1][1]
        aPart[0][2] += aPart[1][2]

for time in range(0,1000):
    if (time % 100)==0:
        print("Time=", time, " remaining particles=", len(particles))
    # do any positions match???
    itemstoremove = []
    for ida, pA in enumerate(particles):
        for idb in range(ida+1, len(particles)):
            pB = particles[idb]
            if pA[0][0] == pB[0][0] and pA[0][1] == pB[0][1] and pA[0][2] == pB[0][2]:
                # collision!!!
                print("   Time=",time,": Collision between ", ida, " and ", idb)
                itemstoremove.append(ida)
                itemstoremove.append(idb)
    # remove them
    for i in sorted(set(itemstoremove), reverse=True):
        del particles[i]
    # next
    tick()

print("Remaining particles=", len(particles))
                 
#for ida,pA in enumerate(particles):
#    for idb in range(ida+1,len(particles)):
#        pB = particles[idb]
#        timeinters = intersectionTime(pA,pB)
#        if timeinters != None and len(timeinters)>0:
#            intcount += 1
#            print("{} {} - intersections={}".format(ida,idb, timeinters))


#def intersectionTime(pa, pb):
#    tint = []
#    retval = []
#    for i in range(0,3):
#        a = (pa[2][i] - pb[2][i])**2 / 2
#        b = pa[1][i] - pb[1][i]
#        c = pa[0][i] - pb[1][i]
#        det = b**2 - 4*a*c
#        if a == 0:
#            # same acceleration!
#            if b != 0:
#                tint.append( [-c/b, -c/b] )
#                continue
#            else:
#                return None
#        if det < 0:
#            return None
#        sol1 = (-b+math.sqrt(det))/(2*a)
#        sol2 = (-b-math.sqrt(det))/(2*a)
#        tint.append( [sol1, sol2] )
#    # these times need to match, or there is no actual collision
#    for agroup in itertools.product(tint[0], tint[1], tint[2]):
#        if agroup[0] == agroup[1] and agroup[1] == agroup[2]:
#           if agroup[0] >= 0:
#               retval.append(agroup[0])
#    return retval

# This approach didn't really work very well
#intcount = 0
#for ida,pA in enumerate(particles):
#    for idb in range(ida+1,len(particles)):
#        pB = particles[idb]
#        timeinters = intersectionTime(pA,pB)
#        if timeinters != None and len(timeinters)>0:
#            intcount += 1
#            print("{} {} - intersections={}".format(ida,idb, timeinters))
#
#print("intersections=", intcount, " out of=", len(particles))
#print(intersectionTime(particles[0], particles[2]))





        

