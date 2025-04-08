import time
start = time.time()

f = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
ans=0
for n in range(10,100_000):
  if n == sum( f[int(d)] for d in str(n) ):
    ans += n
print(ans)

print("\n" , time.time()-start , 'seconds')
