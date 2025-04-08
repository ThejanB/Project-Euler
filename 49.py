import time
start = time.time()

prime_no_list = []
for x in range(10**3+1,10**4,2):
	prime = 1
	for i in range(3,int(x**0.5)+1):
		if x%i == 0:
			prime = 0
			break
	if prime == 1:
		prime_no_list.append(x)

for i in range(0,len(prime_no_list)-2):
	for j in range(i+1,len(prime_no_list)-1):
		if prime_no_list[j]-prime_no_list[i]>10**4//2:
			break
		if set(str(prime_no_list[j]))!=set(str(prime_no_list[i])):
			continue
		for k in range(j+1,len(prime_no_list)):
			if set(str(prime_no_list[i]))!=set(str(prime_no_list[k])):
				continue
			if prime_no_list[j]-prime_no_list[i] == prime_no_list[k]-prime_no_list[j]:
				print(prime_no_list[i],prime_no_list[j],prime_no_list[k])

print("\n" , time.time()-start , 'seconds')
