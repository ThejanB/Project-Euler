from time import time
start = time()

file = open('82 Project Euler.txt','r')
matrix = file.read().split('\n')
file.close()

raws = len(matrix)
for i in range(raws):
    matrix[i] = [int(j) for j in matrix[i].split(',')]

def calc_min(r,c):
    global matrix,raws
    candidates = [matrix[r][c+1]]
    z = 0
    for i in range(r+1,raws):
        z += matrix[i][c]
        candidates.append(z+matrix[i][c+1])
    z = 0 
    for i in range(r-1,-1,-1):
        z += matrix[i][c]
        candidates.append(z+matrix[i][c+1])
    return min(candidates)

c = len(matrix[0])-1
while c > 0:
    c -= 1
    temp = [0]*raws
    for r in range(raws):
        temp[r] = calc_min(r,c)
    
    for i in range(raws):
        matrix[i][c] += temp[i]

temp = [matrix[i][0] for i in range(raws)]
print(min(temp))

print(time()-start,'seconds')
