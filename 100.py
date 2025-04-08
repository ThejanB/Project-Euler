from time import time
from math import isqrt,sqrt
start = time()

blue,total = 85,120
while True:
    blue,total = 3*blue+2*total-2,4*blue+3*total-3      # I got this equation by using "Dario Alpern's Generic two integer variable equation solver"
    if total>10**12:
        print("blue = ",blue)
        break
    
print(time()-start , "seconds")

P= 3
Q= 8
t= 1520
b = sqrt(1+4*P*t*(t-1)/Q)
print(1+4*P*t*(t-1)/Q)
print((1+sqrt(1+4*P*t*(t-1)/Q))/2)
# print(sqrt(.25))