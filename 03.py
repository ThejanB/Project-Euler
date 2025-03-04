from time import time
Start = time()

x = 600851475143

def is_prime(i):       # always i > 2 and odd
    for j in range(3,int(i**.5)+1,2):
        if i%j == 0:
            return 0
    return 1

max_prime = 0
while True:
    if x%2 == 0:
        max_prime = 2
        x = x//2
    else:
        break

while True:
    for i in range(1,int(x**0.5)+1,2):
        if x%i == 0:
            if max_prime < i and is_prime(i) == 1:
                max_prime = i
            if max_prime < x//i and is_prime(x//i) == 1:
                max_prime = x//i
            if i != 1:
                x = x//i
                break
    else:
        break                    
print(max_prime)
print(time()-Start,"seconds")
