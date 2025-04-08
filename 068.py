import time
start = time.time()

numbers = ['1','2','3','4','5','6','7','8','9','10']
count,max_no = 0,0

for n1 in range(0,6):
	a = tuple(numbers)
	numbers.pop(n1)
	for n2 in range(0,len(numbers)):
		b = tuple(numbers)
		if int(a[n1]) > int(b[n2]):
			continue
		numbers.pop(n2)
		for n3 in range(0,len(numbers)):
			c = tuple(numbers)
			if int(a[n1]) > int(c[n3]):
				continue
			numbers.pop(n3)
			for n4 in range(0,len(numbers)):
				d = tuple(numbers)
				if int(a[n1]) > int(d[n4]):
					continue
				numbers.pop(n4)
				for n5 in range(0,len(numbers)):
					e = tuple(numbers)
					if int(a[n1]) > int(e[n5]):
						continue
					numbers.pop(n5)
					if '10' in numbers:
						numbers.insert(n5,e[n5])
						continue
					for n6 in range(0,len(numbers)):
						f = tuple(numbers)
						numbers.pop(n6)
						for n7 in range(0,len(numbers)):
							g = tuple(numbers)
							numbers.pop(n7)
							for n8 in range(0,len(numbers)):
								h = tuple(numbers)
								numbers.pop(n8)
								for n9 in  range(0,len(numbers)):
									i = tuple(numbers)
									numbers.pop(n9)
									for n10 in numbers:
										if int(a[n1])+int(f[n6])+int(g[n7])==int(b[n2])+int(g[n7])+int(h[n8])==int(c[n3])+int(h[n8])+int(i[n9])==int(d[n4])+int(i[n9])+int(n10)==int(e[n5])+int(n10)+int(f[n6]):
											no = a[n1]+f[n6]+g[n7]+b[n2]+g[n7]+h[n8]+c[n3]+h[n8]+i[n9]+d[n4]+i[n9]+n10+e[n5]+n10+f[n6]
											if int(no)>max_no:
												max_no=int(no)
									numbers = list(i)
								numbers = list(h)
							numbers = list(g)
						numbers = list(f)
					numbers = list(e)
				numbers = list(d)
			numbers = list(c)
		numbers = list(b)
	numbers = list(a)
print(max_no)
print("\n" , time.time()-start , 'seconds')
