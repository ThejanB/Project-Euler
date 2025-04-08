import math

l = []

i = 2
while i < 1e3:
    j = 1
    while True:
        no = i**j
        if no > 10**100:         #i'm checking numbers below 100 digit numbers
            break
        if sum(int(i) for i in str(no)) == i:
            l.append(no)
        j+=1
    i+=1

l = [i for i in set(l) if i > 9]
l.sort()

for i in range(len(l)):
    print('a',i+1,' = ',l[i])


# Extend this code for any given base

