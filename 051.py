from time import time
from collections import Counter         # to count same digits in a str(number) / to get duplicates
start = time()

def prime_list(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2 -1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:candidates[i*i::i] = [None]*(n//i -(i-1))
    return [i for i in candidates[2:] if i]

def is_prime(n):
    if n%2 == 0:
        return 0
    for i in range(3,int(n**.5)+1,2):
        if n%i == 0:
            return 0
    return 1

def families(s):
    s = str(s)
    sol = []
    for duplicate in (Counter(s) - Counter(set(s))):
        a = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        temp = [int(s.replace(duplicate, x)) for x in a]
        if s.index(duplicate) == 0:         # remove numbers like 0023
            del temp[0]
        sol.append(temp)
    return sol

def check(l):
    for k in range(len(l)):
        if is_prime(l[k]) == 0:
            l[k] = None
    return len([x for x in l if x])

primes = prime_list(1000000)                # list of primes upto 1 million
primes = [x for x in primes if len(str(x)) - len(set(str(x))) > 0]  # primes with replacable places

done = False
i = 0
Target = 8
while not done:
    replacements = families(primes[i])
    for j in replacements:
        if check(j) >= Target:
            print(j[0])
#            print(j)             # all family numbers
            done = True       
    i += 1

print(time()-start,"seconds")

'''
-at 1st wrote a def to get list of prime numbers. -> def prime_list(n)
-wrote a def to check whether prime or not -> def is_prime(n)

-then wrote a def to take a number and return a list of families.  -> def families(s)
    Example ->
    11233
    families -> [ [233, 11233, 22233, 33233, 44233, 55233, 66233, 77233, 88233, 99233] ,
                [11200, 11211, 11222, 11233, 11244, 11255, 11266, 11277, 11288, 11299] ]
-it works for not adjacent digits also.
-i didn't try to change single digits becouse the question says "not necessarily adjacent digits".
-1123 is a prime ,but 0023 cannot get as a family prime

-then wrote a def to take a list and remove all the values which are not prime numbers,and finally return the number of prime numbers. -> def check(l)

Thejan -> 22-02-2021
'''
