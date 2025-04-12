N, K = map(int, input().split())
# N, K = 100, 1000000 for Project Euler 53


cache = {0: 1, 1: 1}  # Cache for factorials
def factorial(n):
    if n in cache:
        return cache[n]

    result = n * factorial(n - 1)
    cache[n] = result
    return result

# n! = n1 , r! = n2 , (n-r)! = n3
count = 0
for n in range(N + 1):
    for r in range(n//2+1):
        n1 = factorial(n)
        n2 = factorial(r)
        n3 = factorial(n - r)
        if n1 // (n2 * n3) > K:
            count += n-2*r + 1
            break
print(count)
