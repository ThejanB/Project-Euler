from time import time
from itertools import product,takewhile
start = time()

def primes(k):
    candidates = list(range(k+1))
    candidates[4::2] = [None]*(k//2 - 1)
    for i in range(3,int(k**.5 +1),2):
        if candidates[i]:
            candidates[i*2::i] = [None]*(k//i - 1)
    return [i for i in candidates[2:] if i]

limit = 5*10**7
prime_list = primes(int((limit)**.5))

square = takewhile(lambda x:x<limit , (prime**2 for prime in prime_list))
cube = takewhile(lambda x:x<limit , (prime**3 for prime in prime_list))
fourth_power = takewhile(lambda x:x<limit , (prime**4 for prime in prime_list))

print(len(set(i+j+k for (i,j,k) in product(square,cube,fourth_power ) if i+j+k < limit)))
print(time()-start,"seconds")
