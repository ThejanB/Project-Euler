'''
-   To have minimum n/φ(n) ratio , n must have maximum number of relatively primes
-   To have maximum relatively primes , the number must be a prime
    but φ(n) cannot be a permutation of n ,  φ(n) = n-1 for primes

-   Then the answer must be a multiplication of 2 prime numbers to have maximum relatively primes and to be a permutation

{ φ(n) = Totients }

Thejan -> 2021-05-15
'''

from itertools import combinations
from time import time

def prime_list(n): 
    candidates = list(range(n+1))
    for i in range(2,int(n**0.5)+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return (i for i in candidates[2:] if i)

def main():
    primes      = prime_list(5000)
    prime_pairs = combinations(primes,2)
    ans         = (1000,0)                  # (n/φ(n) , n) 

    for n,Totients in ( (a*b , a*b-a-b+1) for a,b in prime_pairs if a*b < 10_000_000):
        if sorted(str(n)) == sorted(str(Totients)) and float(n)/Totients < ans[0]:
            ans = (float(n)/Totients,n)
    print(ans[1])

start = time()
main()
print(time()-start,"seconds")
