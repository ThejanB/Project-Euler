import time
start = time.time()

def rad(n):
    candidates = [1]*(n+1)
    candidates[0] = 0
    for i in range(2,n+1,2):
        candidates[i] *= 2
    for i in range(3,n+1,2):
        if candidates[i] == 1:
            for j in range(i,n+1,i):
                candidates[j] *= i
    return candidates

#inputs
limit = 100000
k     = 10000

rads = rad(limit)
rads = sorted((rads[i],i) for i in range(limit+1))
    
print('k\trad\tn')
print(k,rads[k])
print(time.time()-start , 'seconds')
