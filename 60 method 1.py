from time import time
start = time()

def function_prime(k):		
	for x in range(2,int(int(k)**0.5+1)):
		if k%x ==  0:
			return 0
	return 1

from sys import exit

prime_no_list = [3,5,7,11,13,17]		#removed 2
for no in range(19,8500,2):
    if function_prime(no) == 1:
        prime_no_list.append(no)

for a in range(0,len(prime_no_list)-4):
	for b in range(a+1,len(prime_no_list)-3):
		if function_prime(int(str(prime_no_list[a])+str(prime_no_list[b]))) == 0 or function_prime(int(str(prime_no_list[b])+str(prime_no_list[a]))) == 0:
			continue
		for c in range(b+1,len(prime_no_list)-2):
			if function_prime(int(str(prime_no_list[a])+str(prime_no_list[c]))) == 0 or function_prime(int(str(prime_no_list[c])+str(prime_no_list[a]))) == 0:
				continue
			if function_prime(int(str(prime_no_list[b])+str(prime_no_list[c]))) == 0 or function_prime(int(str(prime_no_list[c])+str(prime_no_list[b]))) == 0:
				continue
			for d in range(c+1,len(prime_no_list)-1):
				if function_prime(int(str(prime_no_list[a])+str(prime_no_list[d]))) == 0 or function_prime(int(str(prime_no_list[d])+str(prime_no_list[a]))) == 0:
					continue
				if function_prime(int(str(prime_no_list[b])+str(prime_no_list[d]))) == 0 or function_prime(int(str(prime_no_list[d])+str(prime_no_list[b]))) == 0:
					continue
				if function_prime(int(str(prime_no_list[c])+str(prime_no_list[d]))) == 0 or function_prime(int(str(prime_no_list[d])+str(prime_no_list[c]))) == 0:
					continue
				for e in range(d+1,len(prime_no_list)):
					if function_prime(int(str(prime_no_list[a])+str(prime_no_list[e]))) == 0 or function_prime(int(str(prime_no_list[e])+str(prime_no_list[a]))) == 0:
						continue
					if function_prime(int(str(prime_no_list[b])+str(prime_no_list[e]))) == 0 or function_prime(int(str(prime_no_list[e])+str(prime_no_list[b]))) == 0:
						continue
					if function_prime(int(str(prime_no_list[c])+str(prime_no_list[e]))) == 0 or function_prime(int(str(prime_no_list[e])+str(prime_no_list[c]))) == 0:
						continue
					if function_prime(int(str(prime_no_list[d])+str(prime_no_list[e]))) == 0 or function_prime(int(str(prime_no_list[e])+str(prime_no_list[d]))) == 0:
						continue
					print(prime_no_list[a],prime_no_list[b],prime_no_list[c],prime_no_list[d],prime_no_list[e])
					print("sum =",prime_no_list[a]+prime_no_list[b]+prime_no_list[c]+prime_no_list[d]+prime_no_list[e])
					print("\n",time()-start,"seconds")
					exit()
