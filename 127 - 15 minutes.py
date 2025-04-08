# it took 902 seconds (15 minutes and 02 seconds)
from math import gcd
from time import time
start = time()

def rad(n):
    candidates = [1]*(n)
    candidates[0] = 0
    for i in range(2,n,2):
        candidates[i] *= 2
    for i in range(3,n,2):
        if candidates[i] == 1:
            for j in range(i,n,i):
                candidates[j] *= i
    return candidates

#input
limit = 120_000

rads = rad(limit)
ans = 0
for a in range(1,limit//2+1):
    for b in range(a+1,limit-a):   # a<b , a+b<limit
        c = a+b
        if rads[a]*rads[b]*rads[c] >= c:
            continue
        if gcd(a,b) != 1:
            continue
        ans += c

print(ans)
print(time()-start,"seconds")

'''
gcd(a,b) = 1 and a+b = c, so gcd(a,c) and gcd(b,c) must be 1 (no common facts)

gcd(a,b) = 1 , so rad(abc) = rad(a)*rad(b)*rad(c)

Thejan -> 2021-05-27
'''
