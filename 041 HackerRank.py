import itertools
from bisect import bisect_right

# Miller-Rabin primality test (deterministic for n < 3,317,444,400,000,000,000)
def is_prime(n):
    if n < 2: return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 3, 5, 7, 11]:
        x = pow(a, d, n)
        if x == 1 or x == n - 1: continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1: break
        else:
            return False
    return True

# Precompute all pandigital primes
pandigital_primes = []
for n in range(1, 10):
    digits = ''.join(str(i) for i in range(1, n + 1))
    for p in itertools.permutations(digits):
        num = int(''.join(p))
        if is_prime(num):
            pandigital_primes.append(num)

pandigital_primes.sort()

# Binary search to find largest pandigital prime <= N
def find_max_pandigital_prime(N):
    idx = bisect_right(pandigital_primes, N)
    if idx == 0:
        return -1
    return pandigital_primes[idx - 1]

import sys
input = sys.stdin.read
data = input().split()

T = int(data[0])
results = []
for i in range(1, T + 1):
    N = int(data[i])
    results.append(str(find_max_pandigital_prime(N)))

print('\n'.join(results))

