import time
start = time.time()

def calc(n):
    global primes
    rad = 1
    for i in primes:
        if i > n:
            break
        if (n/i)%1 == 0:
            rad *= i
            n //= i
    return rad

def prime(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2-1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:
            candidates[i*2::i] = [None]*(n//i-1)
    return [i for i in candidates[2::] if i]

#inputs
limit = 100000
k     = 10000

primes = prime(limit)
l = [(calc(n),n) for n in range(1,limit+1)]
l.sort()

print('k\trad\tn')
print(k,l[k-1])
print(time.time()-start , 'seconds')
