from time import time
start = time()

for n in range(2*3*5*7*11,2000000,2*3*5*7*11):
    count = 2 # for d = 1 and d = n
    for d in range(2,n):
        if ((n**2)/d)%1 == 0:
            count += 1
    if count > 1000:
        print(n,count)
        break
print(time()-start,'seconds')

'''
1/n = 1/x + 1/y
y = nx/(x-n)    , n<x<=2n

let d = x-n
    x = d+n     , 0<d<=n , x is a int for every int(d)
    
then,
    y = n(d+n)/d
    y = n + (n**2)/d    , if (n**2)/d is a int y becomes a int

to have maximum factors it must be a product of smallest prime numbers.
so i started with 2*3*5*7*11


'''
