from itertools import product,combinations_with_replacement
from time import time

def calc(limit):
    nearest = (0,0,0,100000,0)              #(x,y,x*y,abs(),rectangles)
    grid_range = 80
    for x in range(1,grid_range):          # better to get range from 1 to grid_range
        for y in range(x,grid_range+1):
            rectangles = 0
            size = (i for i in product(range(1,max(x,y)+1), repeat=2) if i[0]<x+1 and i[1]<y+1)

            for item in size:
                rectangles += ( x-(item[0]-1) )*( y-(item[1]-1) )

            if abs(limit - rectangles) < nearest[3] :
                nearest = (x,y,x*y,abs(limit - rectangles),rectangles)
            
            if rectangles > limit: # for next y , answers must be so far from this abs()
                if x == y:
                    return nearest
                break
    return nearest         

start   = time()
limit   = 2000000
ans     = calc(limit)
print('x , y , area , abs() , rectangles =',ans)
print('area of nearest solution =' ,ans[2])
print(time()-start,'seconds')
