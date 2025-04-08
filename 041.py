from time import time
from itertools import permutations
start = time()

for a,b,c,d,e,f,g in permutations(reversed(range(1,8)),7):
        if int(g)%2==0:
                continue
        no = int(str(a)+str(b)+str(c)+str(d)+str(e)+str(f)+str(g))
        for x in range(3,int(no**0.5)+1,2):
                if no%x==0:
                        break           #it will not break if no is a prime
        else:   
                break                   #if no is a prime it must be the max prime

print('Max prime =',no)
print(time()-start , 'seconds')

