from time import time
start = time()

#return a list of sum of proper divisors
def divisors_sum (limit):
    candidates = [1]*(limit)
    for i in range(2,limit//2+1):
        candidates[i*2::i] = [j+i for j in candidates[i*2::i] ]
    return candidates

limit = 10000
amicable_sum = 0
divisors = divisors_sum(limit)

for a in range(2,limit):
    b = divisors[a]
    if b < limit and b != a and divisors[b] == a:
        amicable_sum += a

print(amicable_sum)
print(time()-start,"seconds")
