from time import time
from itertools import permutations

start = time()
x = list(permutations([str(i) for i in range(0,10)]))

z = str()
for a in x[1000000-1]: #x[0] is the 1st permutation,so x[1000000-1] is the 1000000th permutation
        z+=a
print(int(z))

print(time()-start,"seconds")
