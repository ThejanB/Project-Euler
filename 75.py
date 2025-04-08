from math import gcd,sqrt
from time import time
start = time()
limit = 1500000

ans = set()
not_ans = set()
for n in range(1,int(sqrt(limit)/2)+1):
    for m in range(n+1,int(sqrt(limit/2))+1,2):
        if gcd(m,n) != 1 :
            continue
        if 2*m*(m+n) > limit:
            break
        L = 2*m*(m+n)
        for k in range(1,int(limit//L+1)):
            not_ans.add(k*L) if k*L in ans else ans.add(k*L)
            
print(len(ans-not_ans))

print(time() -start,'seconds')


'''
I searched in google as 'pythagorean triples formula Wikipedia' ,
The theory on Pythagorean triplets as given on Wikipedia ->
    a = m**2 - n**2
    b = 2*m*n
    c = m**2 + n**2
    
    here    - m,n are positive integers
            - m > n
            - m,n are coprime and both should not be odd numbers(if coprime -> gcd(m,n) = 1)

length = a+b+c     <= limit
length = 2*m*(m+n) <= limit
        m>n so 2*n*(2*n) < limit
                     n    < limit**.5 /2

        2*m*(m+n) <= limit
        2*m*(m+0) < limit
             m    < (limit/2)**.5 

a,b,c is a pythagorean triple
ka,kb,kc is also a pythagorean triple
we have to check them also

Thejan -> 2021-05-21
'''
