
def prime_list(n):
    candidates = list(range(n+1))
    candidates[:2] = [None]*2
    candidates[4::2] = [None]*(n//2 -1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:candidates[i*i::i] = [None]*(n//i -(i-1))
    return candidates

def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3,int(n**.5)+1,2):
        if n % i == 0:
            return False
    return True

n = int(input())

primes = prime_list(n)

total = 2 # sum of primes below 100 = 446 given in the problem
# add cerculer primes
for i in range(3,n,2):
    if primes[i]:
        temp = set()
        for j in range(1, len(str(i))):
            rotation = int(str(i)[j:] + str(i)[:j])
            # print(rotation)
            if rotation > n and not is_prime(rotation):
                break
            elif not primes[rotation]:
                break
            temp.add(rotation)
        else:
            temp.add(i)
            for number in temp:
                if number <= n:
                    primes[number] = None
                total += number
            # total += i
            # print("i:",i)

print(total)