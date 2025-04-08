from time import time
start = time()

tot_rmax = 0

for a in range(3,1001):
    rmax = 2*a*((a-1)//2)
    tot_rmax += rmax

print(tot_rmax)

print(time()-start,"seconds")

 
'''
Explanation
n=1 : (a-1) + (a 1) = 2a
n=2 : (a-1)^2 + (a 1)^2 = 2a^2 + 2
n=3 : (a-1)^3 + (a 1)^3 = 2a^3 + 6a
n=4 : (a-1)^4 + (a 1)^4 = 2a^4 + 12a^2 + 2
n=5 : (a-1)^5 + (a 1)^5 = 2a^5 + 20a^3 + 10a

remainer (MOD a^2)
n=1 : 2a
n=2 : 2
n=3 : 6a
n=4 : 2
n=5 : 10a

So we get that for any even value of n we get 2 as the remainder,and for any odd value we get 2*n*a as the remainder

if n = a/2 -> reminer = 0      (a^2 / a^2)
Since we are dealing with modular arithmetic increasing itmeans that the expression must be maximized for the value n = (a-1)//2.
not int(a/2-1)

so rmax = 2*a*n
        = 2*a*((a-1)//2)

Thejan -> 19-2-2021
'''


