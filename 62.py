from time import time
from itertools import permutations
start = time()

cubes_list = []
i,count = 0,0
while count != 5:
    i += 1
    cube = list(str(i**3))
    cube.sort()             # sort(permutations of its digit list) are equal -> sort(list("123")) == sort(list("213"))
    cubes_list.append(cube)
    count = cubes_list.count(cube)

n = cubes_list.index(cube)+1
print("number = ",n ,"cube = ",n**3)

print("\n",time()-start,"seconds")
