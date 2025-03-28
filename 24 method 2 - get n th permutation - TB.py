from time import time
start = time()

def fac(x):         # return x!
    if x == 0 or x == 1:
        return 1
    else:
        return x*fac(x-1)
    
a=['0','1','2','3','4','5','6','7','8','9']
count = 1
number = ''
while len(a)>0:
    i=0
    while count <= 10**6:
        count += fac(len(a)-1)
        i+=1
    count -= fac(len(a)-1)
    i -= 1
    
    number += a[i]
    del a[i]

print(number)
print (time()-start,"seconds")



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
