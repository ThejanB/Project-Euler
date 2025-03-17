file = open("81 Project Euler.Txt")
m = []
for i in file.readlines():
    m.append( list( map(int, i.split(',')) ) )

R,C = len(m),len(m[0])

for x in range(1,R):       
    m[x][0] = m[x][0] + m[x-1][0]   # 1 st column      
    m[0][x] = m[0][x] + m[0][x-1]   # 1 st raw

for r in range(1,R):
    for c in range(1,C):
        m[r][c] = m[r][c] + min(m[r][c-1],m[r-1][c])
 
print(m[r][c])
file.close()
