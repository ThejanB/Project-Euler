from time import time
start = time()

numbers = 0
for no in range(1,10000):
	count,lychrel_no = 0,0
	x = no
	while count < 50:
		count += 1
		x = x + int(str(x)[::-1])
		if x == int(str(x)[::-1]):
			lychrel_no = 1
		if lychrel_no == 1:
			break
	if lychrel_no == 0:
		numbers += 1

print(numbers)
print(time()-start,'seconds')
