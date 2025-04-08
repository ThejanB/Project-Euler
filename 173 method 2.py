from time import time
start = time()

limit = 1000000
tiles = limit // 4
print( sum( tiles//i-i for i in range(1,int(tiles**.5) + 1) ) )

print(time()-start,'seconds')

'''
-This question is about a square.
 So we can consider only one side of the sqrare.

Thejan -> 2021-05-17
'''
