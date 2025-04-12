t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    
    sq1 = (n*(n+1)//2)**2
    sq2 = sq2 = n*(n+1)*(2*n+1)//6

    print(sq1 - sq2)
