import time
start = time.time()

x,n,count,product = 0,0,0,1
while count < 6:
	x += 1
	for y in str(x):
		n += 1
		if n==10**count:
			count += 1
			product *= int(y)
print(product)
print("\n" , time.time()-start , 'seconds')