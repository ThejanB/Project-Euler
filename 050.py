import time
start = time.time()

#count= 0
#prime_no_list = [2,3,5,7,11,13]
tot = 7+11+13 # +2+3+5  - 1st i checked the answer with these numbers.then I remove 2,3, and 5 and checked the answer 
max_prime = 41
for no in range(15,10**6,2):
	prime2 = 1
	for i in range(3,int(no**0.5)+1):
		if no%i == 0:
			break
	else:
		#prime_no_list.append(no)
		tot += no
		if tot >10**6:
			break
		for j in range(2,int(no**0.5)+1):
			if tot%j == 0:
				prime2 = 0
				break
		if prime2 == 1:
			max_prime = tot
print(max_prime)
print("\n" , time.time()-start , 'seconds')