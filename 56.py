from time import time
start = time()

max_sum = 0
for a in range(2,100):
	for b in range (2,100):
		no_sum = sum(int(x) for x in str(a**b))
		if no_sum > max_sum:
			max_sum = no_sum
print(max_sum)

print(time()-start,'seconds')
