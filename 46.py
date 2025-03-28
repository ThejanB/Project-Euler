import time
start = time.time()

import math
prime_no_list = [2,3,5,7,11,13]

for no in range(15,100000000000,2):
	prime = 1
	for x in range(3,int(math.sqrt(no))+1):
		if no%x == 0:
			prime = 0
			break
	if prime == 1:
		prime_no_list.append(no)
	else:
		correct = 1
		for i in prime_no_list:
			if (((no-i)/2)**0.5)%1 == 0:
				correct = 0
				break
		if	correct == 1:
			print(no)
			break
print("\n" , time.time()-start , 'seconds')
