from time import time
start = time()

left_n = 2/5
for d in reversed(range(1,1000000+1)):
    n = (3*d-1)/7
    if n%1 == 0:
        print(int(n))
        break

print("\n",time()-start,"seconds")


'''
n/d <3/7
7n < 3d

n,d are integers.
we know that the due to the inequality there is a difference on minimum 1

7n <= 3d-1
n <= (3d-1)/7

for max n ,
    n = (3d-1)/7

then we have to ensure that our answer immediately to the left of 3/7
to ensure that i used a reversed list

Thejan -> 2021-05-15
'''
