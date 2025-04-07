from time import time
start = time()

def prime(n):
    candidates = list(range(n+1))
    candidates[2*2::2] = [None] * (n//2 - 1)
    for i in range(3,int(n**0.5)+1,2):
        if candidates[i]:
            candidates[i*i::i] = [None] * (n//i - i + 1)
    return [i for i in candidates[2:] if i]

def is_prime(n):
    if n == 2:
        return 1
    if n <= 1 or n%2 == 0 :
        return 0
    for i in range(3,int(n**.5+1),2):
        if n%i == 0:
            return 0
    return 1

primes = prime(10**6)
count,tot = 0,0
for no in primes[4::]:
    no = str(no)
    for i in range(1,len(no)):
        if is_prime(int(no[i::])) == 0:
            break
        if is_prime(int(no[:-i:])) == 0:
            break
    else:
        count += 1
        tot += int(no)
        print(count,no)
        
    if count == 11:
        print("Total = ",tot)
        break

print(time()-start,"seconds")

'''
get a prime number list below 1,000,000 .

then get both truncatable numbers from left to right and right to left ,
and check them whether prime or not.

Thejan -> 23-03-2020
'''
print( is_prime() )