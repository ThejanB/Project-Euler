def prime(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2-1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:
            candidates[2*i::i] = [None]*(n//i -1)
    return [i for i in candidates[2:] if i]

limit = int(1e2)

primes = prime(limit//2)
S = [1]*(limit+1)
S[0] = 0
for i in [i**2 for i in range(int(limit**.5),1,-1)]:
    S[i] = i
    for p in primes:
        if p*i > limit:
            break
        k = 1
        while i*p*k <= limit:
            if S[i*p*k] == 1:
                S[i*p*k] = i
            k += 1

print(sum(S)%1000000007)


