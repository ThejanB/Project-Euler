N = int(input())
seen = [False]*(N+1)
s = 0
for a in range(2, N+1):
    if not seen[a]:
        b = 2 
        powers = set()
        while a**b <= N:
            seen[a**b] = True
            powers.update(p for p in range(2*b, N*b+1, b) if p > N)
            b+= 1
        s+=len(powers) + N-1
print(s)