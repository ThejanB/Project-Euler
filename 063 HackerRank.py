
x = int(input())
count,power = 0,0
no = 0
while len(str(power)) <= x+1:
	no += 1
	power = no**x
	if x == len(str(power)):
		print(power)

