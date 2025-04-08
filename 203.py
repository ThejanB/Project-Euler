from time import time
start = time()

def prime_list(n:int):
    candidates = list(range(n+1))
    for i in range(2,int(n**.5)+1):
        if candidates[i]:
            candidates[2*i::i] = [None]*(n//i -1)
    return [i for i in candidates[2:] if i]

limit = 51
l = [1]
m = [1]
candidates = []
for i in range(limit-1):
    m += [0]
    for a in range(len(l)):
        m[a+1] += l[a]
        candidates.append(m[a+1])
    l = m[::]

candidates = sorted(set(candidates))
primes = prime_list(100)

for i in range(len(candidates)):
    if not candidates[i]:
        continue
    for p in primes:
        if candidates[i] < p**2:
            break
        if candidates[i]%(p**2) == 0:
            candidates[i] = False
            break

squarefree = [i for i in candidates if i]

print(sum(squarefree))
print(time()-start,"seconds")
