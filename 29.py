import time
start = time.time()

print(len(set( [a**b for a in range(2,101) for b in range(2,101)] )))

print(time.time()-start , 'seconds')
