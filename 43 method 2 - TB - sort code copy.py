from time import time
from itertools import permutations
start = time()

def is_valid(num):
    primes = [2, 3, 5, 7, 11, 13, 17]
    for i, prime in enumerate(primes):
        if int(num[i+1:i+4]) % prime != 0:
            return False
    return True

def sum_pandigital_numbers():
    total = 0
    for perm in permutations("0123456789"):
        num = "".join(perm)
        if is_valid(num):
            total += int(num)
    return total

# Compute and print the result
result = sum_pandigital_numbers()
print("Sum of all valid pandigital numbers:", result)
print(time()-start , 'seconds')
