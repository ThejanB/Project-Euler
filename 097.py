from time import time
start = time()

no = 28433
for x in range(7830457):
        no = (no*2)%(10**10)

print(no+1)
print("\n" , time()-start , 'seconds')
