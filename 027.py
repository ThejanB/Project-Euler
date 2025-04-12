import time
start = time.time()

def prime(n): 
    candidates = list(range(n+1))
    candidates[4::2] = [None] * (n//2 - 1)
    for i in range(3,int(n**0.5)+1,2):
        if not candidates[i]:
            continue
        candidates[i*i::i] = [None] * (n//i-i+1)
    return [i for i in candidates[2:] if i]

prime_no_list = prime(1000)

max_count,max_a,max_b = 0,0,0
for a in range(-999,1000):
	for b in prime_no_list:
		count,p = 0,0
		for n in range(len(prime_no_list)):
			if n**2+a*n+b in prime_no_list:
				count +=1
			else:
				break
		if max_count<count:
			max_count = count
			max_a = a
			max_b = b

print('prouduct = ',max_a*max_b)

print(time.time()-start , 'seconds')
