def collatz_length(n, cache):
    if n in cache:
        return cache[n]
    
    original_n = n
    count = 0
    while n not in cache:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        count += 1
    
    cache[original_n] = count + cache[n]
    return cache[original_n]

def preprocess(limit, cache, precomputed):
    max_length, max_number = 1, 1
    
    for x in range(1, limit + 1):
        length = collatz_length(x, cache)
        if length >= max_length:
            max_length, max_number = length, x
        precomputed[x] = max_number

def precompute(limit):
    global precomputed, cache
    if limit > len(precomputed) - 1:
        precomputed.extend([0] * (limit - len(precomputed) + 1))
    preprocess(limit, cache, precomputed)

# Input handling
t = int(input())
queries = [int(input()) for _ in range(t)]

# Determine if precomputation is needed
MAX_LIMIT = max(queries)
cache = {1: 1}
precomputed = [0] * (MAX_LIMIT + 1)
precompute(MAX_LIMIT)
    
# Output results
for limit in queries:
    print(precomputed[limit])
