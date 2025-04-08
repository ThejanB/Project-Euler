# this will take lot of time to give the result

from time import time
start = time()

#input
limit = 10_000

def calc(n):
    co = list(range(2,n-1))
    for c in co[::-1]:
        if (c*c)%n == 1 and (n/c)%1 != 0:return c
    return 1

ans = 0
for n in range(3,limit):
    ans += calc(n)
print(ans)

print(time()-start,"seconds")
