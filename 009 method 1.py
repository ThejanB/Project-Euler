from time import time
start = time()

'''
let a**2 + b**2 == c**2 
let a < b < c

=> b<500  <=  b<c  <=  b+c<1000
=> a<333  <=  a<b<c  <=  a+b+c<1000
'''

def Q9 ():
    for a in range (1,333):
        for b in range (a+1,500):
            c = 1000 - a - b
            if c <= b:
                break
            if a**2 + b**2 == c**2:
                print ('a = ' , a)
                print ('b = ' , b)
                print ('c = ' , c)
                print ('abc = ' , a*b*c)
                return

Q9 ()
print("\n %f seconds" % (time()-start) )