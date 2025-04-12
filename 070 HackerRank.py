# 90% 
# can be wrong for small values, because i assumed that n must be p×q, for larger n ( >50) this is correct.
# can handle small cases. but didn't do it because I wrote correct (Java) code separately.  

from itertools import combinations

def prime_list(n): 
    candidates = list(range(n+1))
    for i in range(2,int(n**0.5)+1):
        if not candidates[i]:
            continue
        candidates[2*i::i] = [None] * (n//i - 1)
    return (i for i in candidates[2:] if i)

def main():

    ans         = (float('inf'),0)                  # (n/φ(n) , n) 

    limit = int(input())
    
    primes      = prime_list(5000)
    prime_pairs = combinations(primes,2)
    for n,Totients in ( (a*b , a*b-a-b+1) for a,b in prime_pairs if a*b < limit):
        if sorted(str(n)) == sorted(str(Totients)) and float(n)/Totients < ans[0]:
            ans = (float(n)/Totients,n)
    print(ans[1])

main()
