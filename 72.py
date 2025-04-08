from time import time

def main(L):
    candidates  = list(range(L+1))
    for n in range(2, L+1):
        if candidates[n] == n:
            for k in range(n, L+1, n):
                candidates[k] -= candidates[k] // n
    
    # φ(n) = candidates[n]

    return sum(candidates[2::])

start = time()
print (main(1000000))
print(time()-start,"seconds")
