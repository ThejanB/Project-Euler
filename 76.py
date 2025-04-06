from time import time
start = time()

def ways(total,numbers):
    if not numbers:
        return 0
    count = 0
    n_1 = numbers[0]
    numbers = numbers[1::]
    if total%n_1 == 0:
        count += 1
    for total_2 in range(0,total,n_1):
        count += ways(total - total_2,numbers)
    return count

target  = 100
numbers = range(target-1,0,-1)

print(ways(target,numbers))

print(time()-start,"seconds")

'''
This question is very similar to Problem 31,77 and 78.
see them

get a reverse number list to sort the loop in def_ways

it takes about 240 secounds

Thejan -> 21-02-2021
'''
