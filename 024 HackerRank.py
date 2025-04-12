
cache = {0:1,1:1}
def fac(x):         # return x!
    if x in cache:
        return cache[x]
    else:
        cache[x] = x*fac(x-1)
        return cache[x]
    

for i in range(int(input())):
    n = int(input())
    
    a=['a','b','c','d','e','f','g','h','i','j','k','l','m']
    count = 1
    number = ''
    while len(a)>0:
        i=0
        while count <= n:
            count += fac(len(a)-1)
            i+=1
        count -= fac(len(a)-1)
        i -= 1
        
        number += a[i]
        del a[i]

    print(number)



'''
i = 0 , 0 _ _ _ _ _ _ _ _ _      count += 9! <10**6
i = 1 , 1 _ _ _ _ _ _ _ _ _      count += 9! <10**6
i = 2 , 2 _ _ _ _ _ _ _ _ _      count += 9! <10**6
i = 3 , 3 _ _ _ _ _ _ _ _ _      count += 9! >10**6  so i = 2 is the first number (a[2] = 2) , count -= 9! ,delete 2

then,
i = 0 , 2 0 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 1 , 2 1 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 2 , 2 3 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 3 , 2 4 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 4 , 2 5 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 5 , 2 6 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 6 , 2 7 _ _ _ _ _ _ _ _      count += 8! <10**6
i = 7 , 2 8 _ _ _ _ _ _ _ _      count += 8! >10**6 so i = 6 is the 2nd number (a[6] = 7)  , count -= 8! , delete 7

in this way we can find the number

'''
