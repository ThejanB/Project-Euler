from time import time
start = time()

STARTING_DIGITS = 123
COUNT = 678910

def p(STARTING_DIGITS, COUNT):
    n = 2
    count = 0
    pow = 1
    while count < COUNT:
        n *= 2
        if n >= STARTING_DIGITS+1:
            n /= 10.0
        elif n // 1 == float(STARTING_DIGITS):
            count += 1
        pow += 1
    print(pow)
        
p(STARTING_DIGITS, COUNT)

print("%s secounds" %(time()-start))

# answer = 193060223
# took about 30 seconds
