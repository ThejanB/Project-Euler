from time import time
start = time()

def prime(n): 
    candidates = list(range(n+1))
    for i in range(2,int(n**0.5)+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2::] if i]

primes = prime(20)
Max_n = 1       
for p in primes:
    Max_n *= p
    if Max_n >= 1000000:
        Max_n /= p
        print(int(Max_n))
        break

print(time()-start,"seconds ")

'''
To have maximum number of factors,
the number must be a product of smallest prime numbers

Thejan -> 2021-02-23
'''
