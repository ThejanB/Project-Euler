# faster method

from  time import time

start = time()

numbers = list(range(2, 21))

def find_lcm(x, y):
    if x > y:
        y, x = x, y
    
    for i in range(y, x*y, y):
        if i % x == 0:
            return i
    return x*y

lcm = 1
for num in numbers:
    lcm = find_lcm(lcm, num)
print(lcm)

end = time()
print("Execution time:", end - start, "seconds")