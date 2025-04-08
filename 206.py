from time import time
start = time()

#last numbers must be 0
# next blank must be 3 or 7

i = (int((1929394959697989900)**.5)//100)*100 +70  
while True:
    i -= 40                                 # becouse last numbers can be 30
    if str(i**2)[::2] == '1234567890':break
    i -= 60                                 # becouse last numbers can be 70
    if str(i**2)[::2] == '1234567890':break
print(i)

print(time()-start , "seconds")

'''
This is my 1st code ->

i = (int((1020304050607080900)**.5)//100)*100 +30  
while True:
    i += 40                                 # becouse last numbers can be 70
    if str(i**2)[::2] == '1234567890':break
    i += 60                                 # becouse last numbers can be 30
    if str(i**2)[::2] == '1234567890':break
print(i)
print(time()-start , "seconds")


it took 4.5 seconds
then i ran it's reversed code
it takes only 0.001 seconds
'''