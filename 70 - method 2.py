from time import time

def main(L):
    candidates  = list(range(L+1))
    ans         = (100,0)
    for n in range(2, L+1):
        if candidates[n] == n:
            for k in range(n, L+1, n):
                candidates[k] -= candidates[k] // n
    
        # φ(n) = candidates[n]
        if sorted(str(n)) == sorted(str(candidates[n])) and float(n)/candidates[n] < ans[0]:
            ans = (n/candidates[n],n)
    return ans[1]

start = time()
print (main(10000000))
print(time()-start,"seconds")
