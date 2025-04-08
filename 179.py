from time import time

def divisors(limit):
    candidates = [2]*limit
    for i in range(2,limit//2+1):
        candidates[2*i::i] = [1+j for j in candidates[2*i::i]]
    candidates[:2:] = [0,1]
    return candidates

start = time()
limit = 10000000
ans = 0
divisor_list = divisors(limit)

for i in range(1,limit-1):
    if divisor_list[i] == divisor_list[i+1]:
        ans += 1

print(ans)
print(time()-start,"seconds")


'''
This takes about 8.5 seconds

Thejan -> 2021-05-17
'''
