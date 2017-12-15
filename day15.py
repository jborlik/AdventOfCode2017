
factor_gen_a = 16807
factor_gen_b = 48271
gen_divisor = 2147483647

initialvalue_gen_a = 618
initialvalue_gen_b = 814
#initialvalue_gen_a = 65 # test
#initialvalue_gen_b = 8921 # test, results in 588

value_gen_a = initialvalue_gen_a
value_gen_b = initialvalue_gen_b

okmultiple_a = 1
okmultiple_b = 1

maxpairs = 40000000

isparttwo = True

if isparttwo:
    maxpairs = 5000000
    okmultiple_a = 4
    okmultiple_b = 8

def getGenValue(iv, factor, divisor, okmultiple):
    value = iv
    first = True
    while first or (value % okmultiple != 0):
        first = False
        value = (value* factor) % divisor
    return value

count_lower = 0
for i in range(0,maxpairs):
#for i in range(0,5):
    value_gen_a = getGenValue(value_gen_a,factor_gen_a,gen_divisor,okmultiple_a)
    value_gen_b = getGenValue(value_gen_b,factor_gen_b,gen_divisor,okmultiple_b)

    lower_a = value_gen_a & 65535
    lower_b = value_gen_b & 65535
    #print("---- a=",lower_a,"  b=",lower_b)
    if lower_a == lower_b:
        count_lower += 1
    
print("Count of low matches=", count_lower)

