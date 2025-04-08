from time import time
start = time()

def prime_list(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2 -1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:candidates[i*i::i] = [None]*(n//i -(i-1))
    return candidates

def calc():
    primes = prime_list(40000000)
    count = 0
    total = 0
    for i in primes:
        if i:
            if i*i == int(str(i*i)[::-1]):
                continue
            rev = int(str(i**2)[::-1])
            if (rev**0.5)%1 != 0:
                continue
            if primes[int(rev**0.5)]:
                count += 1
                total += i*i
                print(count,": i =",i,"\ttotal =",total)
                if count == 50:
                    return total
    return total

    
print("total =",calc())
print("%s secounds" %(time()-start))
