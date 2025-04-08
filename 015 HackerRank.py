

cache = {}
def factorial(n):
    if n<=1:
        return 1
    if n in cache:
        return cache[n]
    return n*factorial(n-1)
    
t = int(input())

for _ in range(t):
    
    n, m = [int(i) for i in input().split()]
    
    if n > m:
        n, m = m, n
        
    a = factorial(n)
    cache[n] = a
    b = factorial(m)
    cache[m] = b
    c = factorial(n+m)
    cache[n+m] = c
    
    print((c//(a*b))%1000000007)
print(cache)
