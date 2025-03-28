import math

def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, math.isqrt(limit) + 1):
        if sieve[i]:
            sieve[i*i::i] = [False] * len(sieve[i*i::i])
    return sieve

# Precompute primes up to 5*10^5
limit = 5 * 10**5
sieve_cache = sieve(limit)
primes = [i for i, is_prime in enumerate(sieve_cache) if is_prime]

T = int(input())
for _ in range(T):
    N = int(input())
    count = 0
    for p in primes:
        if p >= N:
            break
        remainder = N - p
        if remainder % 2 != 0:
            continue
        k_squared = remainder // 2
        if k_squared == 0:
            continue
        k = math.isqrt(k_squared)
        if k * k == k_squared:
            count += 1
    print(count)