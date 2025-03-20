from time import time
from itertools import combinations_with_replacement

start = time()

### inputs
limit = 28123       #given limit

### get the sum of proper divisors of each number below the limit separately
l = [1]*(limit+1)
l[0] = 0
for i in range(2,limit//2+1):
    for j in range(2*i,limit+1,i):
        l[j] = l[j]+i

### create a list of abundant numbers
abundants = [ i for i in range(1,limit+1) if i < l[i] ]

### finding all the positive integers which can be written as the sum of two abundant numbers
sum_of_2_abundants = set(i+j for i,j in combinations_with_replacement(abundants,2) if i+j<=limit)

### calculating the sum of all numbers below limit
tot = int( limit*(limit+1)/2 )    

### display the sum of all the positive integers which cannot be written as the sum of two abundant numbers
print( tot-sum(sum_of_2_abundants) )

print(time()-start , 'seconds')


''' Euler 23 - method 1
    this took 1.6s , not bad
    Completed on Sat, 21 Mar 2020
    _Mr.T_
'''