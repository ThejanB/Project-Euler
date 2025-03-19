import time
start = time.time()

a,b = 1,1
for x in range(1,41):
        a *= x 
for x in range(1,21):
        b *= x 
print(a/(b*b))

print("\n" , time.time()-start , 'seconds')