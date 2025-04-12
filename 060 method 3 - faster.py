# Hackerrank 57.14%

import sys
import math
from functools import lru_cache
from time import time

N, K = map (int, input().split())   # set 10_000, 5 for Project Euler 60
s = time()

# ---------- Prime generation ----------
def sieve(n):
    is_prime = [True] * (n+1)
    is_prime[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if is_prime[i]:
            is_prime[i*i:n+1:i] = [False] * len(range(i*i, n+1, i))
    return [i for i, val in enumerate(is_prime) if val]

base_primes = sieve(N)
prime_set = set(base_primes)

# ---------- Fast primality check ----------
@lru_cache(maxsize=None)
def is_prime(x):
    if x < 2:
        return False
    if x in prime_set:
        return True
    if x % 2 == 0:
        return False
    for i in range(3, int(math.isqrt(x)) + 1, 2):
        if x % i == 0:
            return False
    return True

# ---------- Build adjacency list ----------
adj = {}
for i in range(len(base_primes)):
    a = base_primes[i]
    if a > N:
        break
    adj[a] = []
    for j in range(i+1, len(base_primes)):
        b = base_primes[j]
        if b > N:
            break
        ab = int(str(a) + str(b))
        ba = int(str(b) + str(a))
        if is_prime(ab) and is_prime(ba):
            adj[a].append(b)

# ---------- DFS to find cliques of size K ----------
results = []

def dfs(path):
    if len(path) == K:
        results.append(sum(path))
        # print(path, "Sum:", sum(path))
        # exit()
        return
    last = path[-1]
    for neighbor in adj.get(last, []):
        if all(neighbor in adj.get(p, []) for p in path):
            dfs(path + [neighbor])

# Start DFS from each prime
for p in base_primes:
    if p > N:
        break
    dfs([p])

# ---------- Output ----------
results.sort()
for r in results:
    print(r)

print("Execution Time:", time() - s, "seconds")