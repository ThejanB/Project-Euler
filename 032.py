from time import time
start = time()

numbers = ['1','2','3','4','5','6','7','8','9']
no_list = []

for n1 in range(0,len(numbers)):
	z = tuple(numbers)
	numbers.remove(numbers[n1])
	for n2 in range(0,len(numbers)):
		a = tuple(numbers)
		numbers.remove(numbers[n2])
		for n3 in range(0,len(numbers)):
			b = tuple(numbers)
			numbers.pop(n3)
			for n4 in range(0,len(numbers)):
				c = tuple(numbers)
				numbers.pop(n4)
				for n5 in range(0,len(numbers)):
					d = tuple(numbers)
					numbers.pop(n5)
					for n6 in range(0,len(numbers)):
						e = tuple(numbers)
						numbers.pop(n6)
						for n7 in range(0,len(numbers)):
							f = tuple(numbers)
							numbers.pop(n7)
							for n8 in range(0,len(numbers)):
								g = tuple(numbers)
								numbers.pop(n8)
								for n9 in  numbers:
									no1,no2,no3 = int(z[n1]+a[n2]) , int(b[n3]+c[n4]+d[n5]) , int(e[n6]+f[n7]+g[n8]+n9)
									if no1*no2 == no3:
										if no3 in no_list:
											zz=5
										else:
											no_list.append(no3)
									no1,no2,no3 = int(z[n1]) , int(a[n2]+b[n3]+c[n4]+d[n5]) , int(e[n6]+f[n7]+g[n8]+n9) 
									if no1*no2 == no3:
										if no3 in no_list:
											zz=5
										else:
											no_list.append(no3)
								numbers = list(g)
							numbers = list(f)
						numbers = list(e)
					numbers = list(d)
				numbers = list(c)
			numbers = list(b)
		numbers = list(a)
	numbers = list(z)
no_list.sort()
print(sum(no_list))
print(no_list)

print(time()-start,'seconds')