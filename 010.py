from time import time
start = time()

def prime_list(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2 -1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:candidates[i*i::i] = [None]*(n//i -(i-1))
    return [i for i in candidates[2:] if i]
    
primes = prime_list(2_000_000)
print(sum(primes))
print("%s secounds" %(time()-start))
