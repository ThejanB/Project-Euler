from time import time
start = time()

a,b = 1,1       # for last 10 intigers
c,d = a,b       # for first 10 intigers
k = 2
while True:
    k += 1
    b,a = (a+b)%1000000000,b
    d,c = c+d,d
    
    while len(str(d)) > 15 :
        d,c = d//10,c//10

    if set(str(d)[0:9:]) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'} :
        if set(str(b)) == {'1', '2', '3', '4', '5', '6', '7', '8', '9'} :
            print(k)
            break

print(time()-start,"seconds")
