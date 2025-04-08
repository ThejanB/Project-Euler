from time import time
start = time()

def prime(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2-1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:candidates[i*2::i] = [None]*(n//i-1)
    return [i for i in candidates[2::] if i]

#input
limit = 100_000_000

primes = prime(limit//2)
k = len(primes)
count = 0
for i in range(k):
    for j in range(i,k):
        if primes[i]*primes[j] > limit:
            break
        else:
            count += 1
   
print(count)
print(time()-start,'seconds')
