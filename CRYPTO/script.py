import json
import math
from Crypto.Util.number import bytes_to_long, getPrime, long_to_bytes

flag = "YazuaCTF{}"
flag = bytes_to_long(flag.encode())

primes = [8412883, 8889941, 9251479, 9471269, 9503671, 9723401, 10092149, 10389901, 10551241, 10665527, 11099951]
shadows = [7832917, 8395798, 4599919, 154544, 3430534, 4694683, 123690, 5911445, 7380167, 10597668]
threshold = 11

def mul(x):
    m = 1
    for i in x:
        m *= i
    return m

pmin = mul(primes[-threshold + 1:])
pmax = mul(primes[:threshold])

print("pmin is ", pmin)
print("pmax is ", pmax)

j = 0
i = math.floor(pmin/primes[0])+ shadows[0]
while j <11:
    if ((i - shadows[j])%primes[j] != 0):
        print("testing ", i)
        i += primes[j]
    else:
        j+=1
        print("cleared index:  ", j)
    if j==11:
        print(" THE FLAG IS: ", i)
        break


#print(flag)
#flag = long_to_bytes(flag)
#print(flag)
