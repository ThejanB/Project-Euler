import random
from time import time
from itertools import product
S = time()

x = sorted([sum(i) for i in product([1,2,3,4], repeat=9)])
y = sorted([sum(i) for i in product([1,2,3,4,5,6], repeat=6)])

x_list = [0]*(x[-1]+1)
y_list = [0]*(y[-1]+1)

for i in range(9,x[-1]+1):
    x_list[i] = x.count(i)
for i in range(6,y[-1]+1):
    y_list[i] = y.count(i)

wins = 0
for i in range(len(y_list)):  
    for j in range(i+1,len(x_list)):    #i > j
        wins  += y_list[i]*x_list[j]

print(round(wins/(4**9*6**6),7))
print(round(time()-S,3),"seconds")
