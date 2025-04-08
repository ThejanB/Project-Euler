from time import time
import math
start = time()

count = 0
for d in range(2,12000+1):
    for n in range(int(d/3),int(d/2+1)):
        if 1/3 < n/d < 1/2 and math.gcd(n,d) == 1:
            count += 1

print(count)
print(time()-start)

'''
the way to choose the range of n->
        1/3 < n/d
        d/3 < n

        n/d < 1/2
        n < d/2

Thejan -> 2021-05-15
'''
