import time
start = time.time()

def calc(x):
    number = x
    count = 0
    while number!=1:
        if number%2==0:
            number = int(number/2)
        else:
            number = number*3 + 1
        count += 1
        if number < x:
            return count + d[number]
    return count

maxcount,maxnumber = 0,0
d = {1:1}
for x in range(2,1000000):
    count = calc(x)
    d[x] = count
    if count>maxcount:
        maxcount = count
        maxnumber = x				
print(maxnumber)

print(time.time()-start , 'seconds')
