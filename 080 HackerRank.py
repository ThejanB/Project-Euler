# 100% HackerRank

from decimal import getcontext,Decimal

limit = int (input())
p = int (input())
ans = 0
getcontext().prec = p+10
for i in range(2,limit+1):
    x = str(Decimal(i).sqrt()).split(".")  

    if len(x) > 1:
        x = x[0]+x[1]
        ans += sum(int(i) for i in x[:p:])

print(ans)
