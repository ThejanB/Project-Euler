from time import time
start = time()

def is_right_triangle(x1, y1, x2, y2):
    a = x1**2 + y1**2
    b = x2**2 + y2**2
    c = (x2 - x1)**2 + (y2 - y1)**2
    return (a + b == c) or (b + c == a) or (c + a == b)

LIMIT = 50
count = sum( 1
            for x1 in range(LIMIT+1)
            for y1 in range(LIMIT+1)
            for x2 in range(LIMIT+1)
            for y2 in range(LIMIT+1)

            if y2*x1 < y1*x2 and is_right_triangle(x1, y1, x2, y2) )
		
print(count)
print(time()-start,'seconds')



'''
not to get same traingle twice->
    method 1 :
    if (x1,y1) has a larger angle than (x2,y2),
        y2/x2 < y1/x1
      = y2*x1 < y1*x2

    method 2 :
    (x1,y1)<(x2,y2)
        if x1<x2 , it returns True
        if x1==x2 , then if y1<y2 ,it returns True

Thejan -> 2021-03-07
'''
