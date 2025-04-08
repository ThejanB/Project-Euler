from time import time
start = time()

def is_right_triangle(x1, y1, x2, y2):
    return (x1 == 0 and y2 == 0) or (x1 * (x2 - x1) + y1 * (y2 - y1) == 0) or (x2 * (x2 - x1) + y2 * (y2 - y1) == 0)

LIMIT = 50
count = sum(1
           for x1 in range(LIMIT+1)
           for y1 in range(LIMIT+1)
           for x2 in range(LIMIT+1)
           for y2 in range(LIMIT+1)

            if (0,0)<(x1,y1)<(x2,y2) and is_right_triangle(x1, y1, x2, y2) )   

print(count)
print(time()-start,'seconds')



'''
note 1: not to get same traingle twice->
    method 1 :
    if (x1,y1) has a larger angle than (x2,y2),
        y2/x2 < y1/x1
      = y2*x1 < y1*x2

    method 2 :
    (x1,y1)<(x2,y2)
        if x1<x2 , it returns True
        if x1==x2 , then if y1<y2 ,it returns True


note 2: get right angled traingles
1 - right angle is on (0,0)
        x1 == 0 and y2 == 0

2 -   This contains 2 situations
        -(right angle is on X axis or Y axis)
        -(right angle is not on X axis or Y axis and 2 points of the traingle in X axis)  
            x1 * (x2 - x1) + y1 * (y2 - y1) == 0

3 -   This contains 2 situations
        -(right angle is not on X axis or Y axis)
        -(2 points of the traingle in Y axis)
            x2 * (x2 - x1) + y2 * (y2 - y1) == 0

Thejan -> 2021-03-07


'''
