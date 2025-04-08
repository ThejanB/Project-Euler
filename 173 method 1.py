from time import time
start = time()

def counter(list_n):
    global count,tile_limit
    for i in range(len(list_n)):
        for j in range(i,len(list_n)):
            tiles = sum(list_n[i:j+1:])
            if tiles > tile_limit:
                break
            count+=1    

tile_limit = 1000000

count = 0
tile_limit //= 4
list_1 = [i for i in range(2,tile_limit+1,2)]         # with 1 middle tile
list_2 = [i for i in range(3,tile_limit+1,2)]        # without a middle tile

counter(list_1)
counter(list_2)

print('count =',count)
print(time()-start,'seconds')

'''
-This question is about a square.
 So we can consider only one side of the sqrare.

Thejan -> 2021-05-17
'''

