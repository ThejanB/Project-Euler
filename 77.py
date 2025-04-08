from time import time
start = time()

def prime(n): 
    candidates = list(range(n+1))
    for i in range(2,int(n**0.5)+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return [i for i in candidates[2:] if i]

def ways(total,primes):
    if not primes:
        return 0
    count = 0
    n_1 = primes[0]
    primes = primes[1::]
    if total%n_1 == 0:
        count += 1
    for total_2 in range(0,total,n_1):
        count += ways(total - total_2,primes)
    return count

for n in range(11,1000):
    primes = prime(n)       #get prime number list below n
    primes.reverse()
    if ways(n,primes) > 5000:
        print(n)
        break

print(time()-start,"seconds")
'''
This question is very similar to Problem 31 and Problem 76.
see them

reverse the prime list to sort the loop in def_ways

Thejan -> 21-02-2021
'''
