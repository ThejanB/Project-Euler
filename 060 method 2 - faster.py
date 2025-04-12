# Hackerrank 50%

import sys
import math
from time import time

sys.setrecursionlimit(10000)

N, K = 10_000, 4    # set 10_000 and test 
s = time()

# ----------- Prime Generation using Sieve ----------
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]
    is_prime[2::2] = [False] * ((n + 1) // 2)  # Remove even numbers, we dont need 2 in this case
    for i in range(3, int(n**0.5) + 1, 2):
        if is_prime[i]:
            is_prime[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    return [i for i, val in enumerate(is_prime) if val]

# Use a higher sieve limit than N for safe concat-prime checks
prime_list = sieve(N*3)
prime_set = set(prime_list)

# ----------- Fast Prime Checker with Memoization ----------
from functools import lru_cache

@lru_cache(maxsize=None)
def is_prime(n):
    if n < 2:
        return False
    if n in prime_set:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

# ----------- Concatenation Prime Check with Memoization ----------
concat_prime_cache = {}

def are_concat_primes(p1, p2):
    key1, key2 = (p1, p2), (p2, p1)
    if key1 in concat_prime_cache:
        return concat_prime_cache[key1]
    concat1 = int(str(p1) + str(p2))
    concat2 = int(str(p2) + str(p1))
    result = is_prime(concat1) and is_prime(concat2)
    concat_prime_cache[key1] = result
    concat_prime_cache[key2] = result
    return result

# ----------- Recursive Search with Pruning ----------
def search(path, start):
    # print(f"Searching: {path}, Start: {start}")
    if len(path) == K:
        print(sum(path))
        # print(f"Found: {path}, Sum: {sum(path)}")
        # print("Execution Time:", time() - s, "seconds")
        # exit()  # Exit after finding the first valid combination
        return

    for i in range(start, len(prime_list)):
        p = prime_list[i]
        if p > N:
            break
        if all(are_concat_primes(p, other) for other in path):
            search(path + [p], i + 1)       # path + [p] returns a new list object, leaving the original path untouched

# ----------- Start Search ----------
search([], 0)

print("Execution Time:", time() - s, "seconds")
