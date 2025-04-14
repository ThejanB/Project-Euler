# 100% HackerRank

limit = int(input())
tiles = limit // 4
print( sum( tiles//i-i for i in range(1,int(tiles**.5) + 1) ) )


'''
-This question is about a square.
 So we can consider only one side of the sqrare.
'''
