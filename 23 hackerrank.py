from itertools import combinations_with_replacement

### inputs
number_list = []
for _ in range(int(input())):
    number_list.append(int(input()))
limit = max(number_list)

### get the sum of proper divisors of each number below the limit separately
l = [1]*(limit+1)
l[0] = 0
for i in range(2,limit//2+1):
    for j in range(2*i,limit+1,i):
        l[j] = l[j]+i

### create a list of abundant numbers
abundants = [ i for i in range(1,limit) if i < l[i] ]

### finding all the positive integers which can be written as the sum of two abundant numbers
sum_of_2_abundants = set(i+j for i,j in combinations_with_replacement(abundants,2) if i+j<=limit)


for number in number_list:
    if number in sum_of_2_abundants:
        print('YES')
    else:
        print('NO')

