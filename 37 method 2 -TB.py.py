from time import time
start = time()

def is_prime(n):
    if n == 2:
        return 1
    if n <= 1 or n%2 == 0 :
        return 0
    for i in range(3,int(n**.5+1),2):
        if n%i == 0:
            return 0
    return 1

#get all combinations of left and right ([a],[b,c]--> [ab,ac])
def combine(left,right): 
    combinations = []
    for i in left:
        for j in right:
            combinations.append( int(str(i)+str(j)) )       
    return combinations

left  = [2,3,5,7]
mid   = [1,3,7,9]
right = [3,7]

truncatable_primes = [ i for i in combine(left,right) if is_prime(i) ]     # total upto 100

while len(truncatable_primes)<11:
    left  = [i for i in combine(left,mid)  if is_prime(i)] 
    right = [i for i in combine(mid,right) if is_prime(i)]

    for l in left:
        for R in right:
            if str(l)[1:] == str(R)[:-1] and is_prime(int(str(l)+str(R)[-1])) :
                truncatable_primes.append( int(str(l)+str(R)[-1]) )

truncatable_primes.sort()
print('Truncatable primes -> ' , truncatable_primes)
print('Total = ' , sum(truncatable_primes[:11]))    

print(time()-start,"seconds")
