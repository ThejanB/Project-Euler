import time
start = time.time()

def Hn(length):
    H = 0
    length -= 2
    i = 1
    while length > 0:
        H += i*int(length*(length+1)/2)             # 1+2+3+....+n
        length -= 3
        i += 1
    return H

ans = 0
length = 12345
for i in range(3,length+1):
    ans += Hn(i)

print(ans)
print(time.time()-start , 'seconds')
