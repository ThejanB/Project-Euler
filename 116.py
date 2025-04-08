from time import time
from math import factorial
start = time()

def nCr(n,r):
    return factorial(n) // factorial(r) // factorial(n-r)

length = 50
red_length,green_length,blue_length = 2,3,4
ans = 0

def calc(tile_length):
    global length,ans
    for i in range(1,length//tile_length+1):
        ans += nCr(length-i*(tile_length-1),i)

calc(red_length)
calc(green_length)
calc(blue_length)

print(ans)
print(time()-start,'seconds')
