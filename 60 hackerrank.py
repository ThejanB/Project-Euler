# 100% HackerRank

import math

# --- 1. isPrime32: Deterministic Miller–Rabin for 32-bit numbers ---
def isPrime32(n):
    if n < 2:
        return False
    smallPrimes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
    for sp in smallPrimes:
        if n == sp:
            return True
        if n % sp == 0:
            return False
    # Write n-1 as d * 2^s.
    d = n - 1
    s = 0
    while d % 2 == 0:
        s += 1
        d //= 2
    for a in [2, 7, 61]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                break
            if x == 1:
                return False
        else:
            return False
    return True

# --- 2. concatInt: Concatenate two integers in decimal ---
def concatInt(p, q):
    tmp = q
    digits = 0
    while tmp > 0:
        digits += 1
        tmp //= 10
    mult = 10 ** digits
    return p * mult + q



N, K = map(int, input().split())

# Sieve to generate primes up to N.
isprime = [True] * (N + 1)
if N >= 0: isprime[0] = False
if N >= 1: isprime[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if isprime[i]:
        for j in range(i * i, N + 1, i):
            isprime[j] = False
primes = [i for i in range(2, N + 1) if isprime[i]]
M = len(primes)

# We will represent the adjacency of each prime (by index) as an integer bitmask.
# Bit i is set in adj[j] if primes[j] is adjacent (compatible) with primes[?].
adj = [0] * M

# Cache for concatenation-primality tests.
concatPrimeCache = {}

def areCompatible(i, j):
    p = primes[i]
    q = primes[j]
    # Check order: p then q.
    key = (p << 32) ^ q
    if key in concatPrimeCache:
        ok = concatPrimeCache[key]
    else:
        cval = concatInt(p, q)
        lower = cval & 0xffffffff  # mimic (uint32_t)cval
        if cval < 2147483647:
            ok = isPrime32(lower)
        else:
            ok = isPrime32(lower) and isPrime32(cval >> 32)
        concatPrimeCache[key] = ok
    if not ok:
        return False
    # Check order: q then p.
    key = (q << 32) ^ p
    if key in concatPrimeCache:
        ok = concatPrimeCache[key]
    else:
        cval = concatInt(q, p)
        if cval <= 2147483647:
            lower = cval & 0xffffffff
            ok = isPrime32(lower)
        else:
            ok = False
        concatPrimeCache[key] = ok
    return ok

# Build the compatibility graph.
for i in range(M):
    for j in range(i + 1, M):
        if areCompatible(i, j):
            # Set bit j in adj[i] and bit i in adj[j]
            adj[i] |= (1 << j)
            adj[j] |= (1 << i)

# --- 4. DFS Backtracking for K-cliques ---
results = []

def backtrack(start, depth, mask, sumSoFar):
    if depth == K:
        results.append(sumSoFar)
        return
    # Prune: count bits in 'mask' from index 'start' upward.
    possible = bin(mask >> start).count("1")
    if possible < (K - depth):
        return
    for i in range(start, M):
        if not ((mask >> i) & 1):
            continue
        newMask = mask & adj[i]
        # Clear bits 0 through i.
        newMask &= ~((1 << (i + 1)) - 1)
        backtrack(i + 1, depth + 1, newMask, sumSoFar + primes[i])

# Start DFS from every prime as the first element.
for i in range(M):
    # Skip if this prime does not have enough neighbors.
    if bin(adj[i]).count("1") < (K - 1):
        continue
    # Initial mask: neighbors with index > i.
    mask = adj[i] & ~((1 << (i + 1)) - 1)
    backtrack(i + 1, 1, mask, primes[i])

results.sort()
print("\n".join(str(r) for r in results))
