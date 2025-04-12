import time
start = time.time()

no_count,prime_count = 1,0
i,no = 2,1

def is_prime(k):
    global prime_count
    if k%2 ==0:
        return 0
    for x in range(3,int(k**0.5)+1,2):
        if k%x == 0:
            return 0
    prime_count += 1
    return 1

while True:
    for j in range(4):      #to run same loop 4 times
        no += i
        is_prime(no)
    no_count += 4
    
    if (prime_count/no_count)*100 < 10:
        print("length = ",i+1)
        print(prime_count,"/",no_count)
        break
    i += 2
    
print(time.time()-start , 'seconds')
