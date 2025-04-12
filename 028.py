

def function1(x):
	no,tot = 1,1
	for a in range(2,1000000000,2):
		for b in range(0,4):
			no += a
			tot += no
		if no == x**2:
			break
	return tot

def function2(x): # Better version
	no,tot = 1,1
	a = 2
	while True:
		tot += 4*no+10*a
		no += 4*a
		if no == x**2:
			break
		a += 2
	return tot


def function3(n): # Best version
    n = (n - 1) // 2
    sum_k2 = n * (n + 1) * (2 * n + 1) // 6
    sum_k = n * (n + 1) // 2
    total = 1 + 16 * sum_k2 + 4 * sum_k + 4 * n
    return total 

import time
start = time.time()
print(function3(1001))
print("\n" , time.time()-start , 'seconds')