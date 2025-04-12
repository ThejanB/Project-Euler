import time
start = time.time()

previousno,no = 1,1
count = 2
while no <= 10**999:
	previousno,no = no,no+previousno
	count += 1
print('index is ' , count)

print(time.time()-start , 'seconds')
