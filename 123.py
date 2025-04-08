from time import time
start = time()

def prime(n):               # to get prime number list
    candidates = list(range(n+1))
    for i in range(2,int(n**0.5)+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

primes = prime(250000)       # get prime a number list below 250,000

for n in range(1,len(primes)+1,2):      # skip even n
    remainder = 2*primes[n-1]*n
    if remainder > 10**10:
        print(n)
        break

print(time()-start)

'''

Problem 120 is very similar to this problem.see it
I solved this problem by using the theory of problem 120

remainer = 2*p*n ,for odd n
remainer = 2 ,for even n , so skip them 

Thejan -> 20-2-2021


'''
