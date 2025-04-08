import time
start = time.time()

def prime_list(n):
    candidates = list(range(n+1))
    candidates[4::2] = [None]*(n//2 -1)
    for i in range(3,int(n**.5)+1,2):
        if candidates[i]:
            candidates[2*i::i] = [None]*(n//i -1)
    return [i for i in candidates[2:] if i]
    
prime_no_list = prime_list(750)

done,no = 0,644
while True:
	no += 1
	prime_factors = 0
	for i in prime_no_list:
		if i >= no:
			break
		if no%i == 0:
			prime_factors += 1
	if prime_factors != 4:
		count = 0
		continue
	count += 1
	if count == 4:
		print(no-3,no-2,no-1,no)
		break

print("\n" , time.time()-start , 'seconds')
