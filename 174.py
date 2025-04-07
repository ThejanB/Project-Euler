from time import time
start = time()

def counter(list_n):
    global tile_limit,L
    for i in range(len(list_n)):
        for j in range(i,len(list_n)):
            tiles = sum(list_n[i:j+1:])
            if tiles > tile_limit:
                break
            L[tiles] += 1
               

tile_limit = 1000000 
L = [0]*(tile_limit+1)  #L(n) = [t=0,t=1,t=2,t=3.....t=tile_limit] 

list_1 = [i for i in range(8,tile_limit+1,8)]         # with 1 middle tile
list_2 = [i for i in range(12,tile_limit+1,8)]        # without a middle tile

counter(list_1)
counter(list_2)

N = 0                   # ∑ N(n) for 1 ≤ n ≤ 10
for i in L:
    if 1<= i<=10:
        N+=1

print('∑ N(n) =', N )
print(time()-start,'seconds')
