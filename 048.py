import time

# method 1
start = time.time()

tot = 0 
for x in range(1,1001):
    tot = tot + x**x
tot = str(tot)
print(tot[-10:])

print(time.time()-start , 'seconds\n')


#  method 2 - faster
start = time.time()

number = 1000
modulo = 10**10  # We only need last 10 digits
tot = sum(pow(x, x, modulo) for x in range(1, number + 1)) % modulo
print(tot)

print(time.time()-start , 'seconds')
