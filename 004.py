'''
max palindromic number = abccba < 999*999 
                       = 100000a + 10000b + 1000c + 100c + 10b + a
                       = 100001a + 10010b + 1100c
                       = 11(9091a + 910b + 100c)
so 1 number must divide by 11
'''

from time import time
start = time()

maxproduct,maxy,maxx = 0,0,0

for x in range(990,100,-11):            # x divides by 11
        for y in range(999,100,-1):
                product = x*y
                if product < maxproduct:
                        break
                if product == int(str(product)[::-1]):
                        maxproduct,maxx,maxy = product,x,y
                        break
print("x =" , maxx)
print("y =" , maxy)
print("max product =" , maxproduct)

print(time()-start , 'seconds')
