names = []
for _ in range(int(input())):
	names.append(input())
names.sort()

for _ in range(int(input())):
	name = input()
	count = names.index(name)+1
	tot = 0
	for y in name:
		tot += (ord(y)-64)
	print(tot*count)
