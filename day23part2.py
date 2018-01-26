
a = b = c = d = e = f = g = h = 0

a = 1  # part 2
b = 65
c = b
if a != 0:
    b *= 100
    b -= -100000
    c = b
    c -= -17000

while True:
    f = 1  # line9   jnz 1 -23
    d = 2

    while True:
        e = d #b / d  # jnz g -13, formerly e=2 or d
#        if e < d:
#            break

        while True:
            t = d * e
            if t >= b:
                if t == b:
                    f = 0
                break
            e += 1

        if f == 0:
            break   # if f=0, d doesn't matter

        d += 1

        if d == b:
            g = 0
            break

    if f==0:
        h -= -1    

    if b == c:
        g = 0
        break
    b -= -17


print("H=",h)