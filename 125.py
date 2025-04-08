from time import time

def squares(n):     # find all the sums starting with n**2
    global limit
    candidates = [n**2]
    while candidates[-1]<limit:
        n += 1
        candidates.append(candidates[-1]+n**2)
    return candidates[1:-1:]
        
def find(n):
    global limit
    candidates = squares(n)
    ans = []
    for i in candidates:
        if str(i) == str(i)[::-1]:
            ans.append(i)
    return ans 

#input
limit = 1000

start = time()
ans   = []
for i in range(1,int((limit/2)**.5+1)):
    ans += find(i)
print(sum(set(ans)))
print(time()-start,"seconds")
    
