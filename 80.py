from time import time
from decimal import getcontext,Decimal
start = time()

ans = 0
getcontext().prec = 102
for i in range(1,101):
    x = str(Decimal(i).sqrt()).split(".")   # a list

    if len(x) > 1:
        x = x[0]+x[1]
        ans += sum(int(i) for i in x[:100:])

print(ans)
print(time()-start,'seconds')
