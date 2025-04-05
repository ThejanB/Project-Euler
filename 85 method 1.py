from itertools import product,combinations_with_replacement
from time import time
start = time()

limit   = 2000000
nearest = (0,0,0,10000,0)    #(x,y,x*y,abs(),rectangles)

for x,y in combinations_with_replacement(range(20,80),2):
    rectangles = 0
    size = (i for i in product(range(1,max(x,y)+1), repeat=2) if i[0]<x+1 and i[1]<y+1)
    
    for item in size:
        rectangles += ( x-(item[0]-1) )*( y-(item[1]-1) )
        if rectangles-limit > nearest[3]:
            break
    else:
        if abs(limit - rectangles) < nearest[3] :            
            nearest = (x,y,x*y,abs(limit - rectangles),rectangles)

print('x , y , area , abs() , rectangles =',nearest)
print('area of nearest solution =' ,nearest[2])
print(time()-start,'seconds')
