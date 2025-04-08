import time
start = time.time()

T_no,x,count = 0,0,0

### calculate the numbers of factors of number i
def fact(i):
        count = 2       #for 1 and itself
        for x in range (2,int(i**0.5)):
                if i%x == 0:
                        count += 2
        if (i**0.5)%1 == 0:
                count +=1
        return count

while count <= 500 :
	x += 1
	T_no += x
	count = fact(T_no)

print(T_no)
print(time.time()-start , 'seconds')

''' Euler 12 - method 2
    took 2s , not satisfied yet
    Completed on Mon, 16 Mar 2020
    _Mr.T_
'''