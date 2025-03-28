limit, K = map(int, input().split())



cubes_list = {}
i,count = 0,0
while i < limit:
    i += 1
    cube = list(str(i**3))
    cube.sort()             # sort(permutations of its digit list) are equal -> sort(list("123")) == sort(list("213"))
    cube = "".join(cube)
    if cube in cubes_list:
        cubes_list[cube] = (cubes_list[cube][0]+1,min(cubes_list[cube][1],i))
    else:
        cubes_list[cube] = (1,i)

for key in cubes_list:
    if cubes_list[key][0] == K:
        print(cubes_list[key][1]**3)
    