import time
start = time.time()

count,power = 0,0
for x in range(1,1000):
	no = 0
	while len(str(power)) <= x+1:
		no += 1
		power = no**x
		if x == len(str(power)):
			count += 1
print(count)

print("\n" , time.time()-start , 'seconds')