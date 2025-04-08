file = open("D:/Educational/project Euler/83 Project Euler.txt")
m = []
for i in file.readlines():
   m.append( list( map(int, i.split(',')) ) )

R,C = len(m),len(m[0])

visited = []
for i in range(R):
    visited.append([False]*C)
visited[0][0] = m[0][0]

next = [[m[0][0],0,0]]

while visited[-1][-1] == False:
    next.sort()

    added = False
    while True:
        i = next.pop(0)
        
        if i[1]+1 < R:
            if visited[i[1]+1][i[2]] == False:
                visited[i[1]+1][i[2]] = i[0] + m[i[1]+1][i[2]]
                next.append([ i[0] + m[i[1]+1][i[2]] ,i[1]+1 , i[2] ])
                added = True

        if i[1]-1 >= 0:
            if visited[i[1]-1][i[2]] == False:
                visited[i[1]-1][i[2]] = i[0] + m[i[1]-1][i[2]]
                next.append([ i[0] + m[i[1]-1][i[2]] ,i[1]-1 , i[2] ])
                added = True

        if i[2]+1 < C:
            if visited[i[1]][i[2]+1] == False:
                visited[i[1]][i[2]+1] = i[0] + m[i[1]][i[2]+1]
                next.append([ i[0] + m[i[1]][i[2]+1] ,i[1] , i[2]+1 ])
                added = True

        if i[2]-1 >= 0:
            if visited[i[1]][i[2]-1] == False:
                visited[i[1]][i[2]-1] = i[0] + m[i[1]][i[2]-1]
                next.append([ i[0] + m[i[1]][i[2]-1] ,i[1] , i[2]-1 ])
                added = True
        
        if added:
            break

print(visited[-1][-1])
