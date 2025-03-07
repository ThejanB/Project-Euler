from time import time
from itertools import permutations
start = time()

ans = 0

for a,b,c,d,e,f,g,h,i,j in permutations(['0','1','2','3','4','5','6','7','8','9'],10):
        if int(b+c+d)%2 == 0 and int(c+d+e)%3 == 0 and int(d+e+f)%5 == 0 and int(e+f+g)%7 == 0 and int(f+g+h)%11 == 0 and int(g+h+i)%13 == 0 and int(h+i+j)%17 == 0:
                ans += int(a+b+c+d+e+f+g+h+i+j)

print(ans)
print(time()-start , 'seconds')
