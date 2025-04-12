from collections import OrderedDict

code_p = { 0:2, 1:3, 2:5, 3:7, 4:11, 5:13, 6:17, 7:19, 8:23, 9:29}

N, K = map(int, input().split())

n, N = N, N - 1 if N in [ 10**i for i in range(3, 7)] else N

primes = [ 0 for _ in range(10**len(str(N))-1) ]

for i in range(2, len(primes)):
    for j in range(i*2, len(primes), i):
        if primes[i]:
            continue
        primes[j] = 1

def rootval(n):
    s = 1
    while n > 0:
        s *= code_p[n % 10]
        n //= 10
    return(s)

primes_d, k_vals = OrderedDict(), OrderedDict()
for j in ( i for i in range(2, len(primes)) if primes[i] == 0 and i >= 1487 ):
    if j < n:
        k_vals[j] = {}
    val = rootval(j)
    if not val in primes_d:
        primes_d[val] = [j]
    else:
        for k in primes_d[val]:
            if k in k_vals:
                for x in k_vals[k]:
                    if (j-k) % x == 0:
                        k_vals[k][x].append((j-k)//x)
                if not j-k in k_vals[k]:
                    k_vals[k][j-k] = [1]
        primes_d[val].append(j)

for i in k_vals:
    if len(k_vals[i]) < K-1:
        continue
    for j in sorted(set(k_vals[i])):
        try:
            if k_vals[i][j][K-2] == K - 1:
                print(*[ i+(x*j) for x in range(K)], sep='')
        except IndexError as e:
            pass
			# no need to handle