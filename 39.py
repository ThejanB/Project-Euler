from time import time
start = time()

max_count,max_p= 0,0
for p in range(750,1000):
	count = 0
	for a in range(1,int(p)//2+1):
		for b in range(1,int(p)//2+1):
			c = p-a-b
			if a+b<c or a+c<b or b+c<a or c<1:
				continue
			if a**2+b**2 ==c**2:
				count += 1
	if max_count < count/2:
		max_count= int(count/2) 	# becouse same numbers come 2 times
		max_p = p
		print(max_count,max_p)

print('\n',time()-start , 'seconds')