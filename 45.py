import time
start = time.time()

no_y,no_z,k = 166,143,0

for x in range(286,50000000):
	f_x = x*(x+1)/2
	for y in range(no_y,50000):
		f_y = y*(3*y-1)/2
		if f_x<f_y:
			no_y = y
			break
		if f_x==f_y:
			for z in range(no_z,50000):
				f_z = z*(2*z-1)
				if f_x<f_z:
					no_z = z
					break
				if f_x==f_z:
					print(f_x)
					k = 1
					break
			if k == 1:
				break
	if k == 1:
		break
	
print("\n" , time.time()-start , 'seconds')