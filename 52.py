from time import time
start = time()

numbers = ['0','1','2','3','4','5','6','7','8','9']
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
					for n6 in numbers:
						no_list.clear()
						no_list.append(z[n1])
						no_list.append(a[n2])
						no_list.append(b[n3])
						no_list.append(c[n4])
						no_list.append(d[n5])
						no_list.append(n6)
						no_list_tuple = tuple(no_list)
						no = int(z[n1]+a[n2]+b[n3]+c[n4]+d[n5]+n6)
						if no*6>10**6:
							continue
						no2 = str(no*2)
						count = 0
						for p in no2:
							if p in no_list:
								no_list.remove(p)
								count += 1
						if count == 6:
							no3 = str(no*3)
							count = 0
							no_list = list(no_list_tuple)
							for p in no3:
								if p in no_list:
									no_list.remove(p)
									count += 1
							if count == 6:
								no4 = str(no*4)
								count = 0
								no_list = list(no_list_tuple)
								for p in no4:
									if p in no_list:
										no_list.remove(p)
										count += 1
								if count == 6:
									no5 = str(no*5)
									count = 0
									no_list = list(no_list_tuple)
									for p in no5:
										if p in no_list:
											no_list.remove(p)
											count += 1
									if count == 6:
										no6 = str(no*6)
										count = 0
										no_list = list(no_list_tuple)
										for p in no6:
											if p in no_list:
												no_list.remove(p)
												count += 1
										if count == 6:
											print(no,no2,no3,no4,no5,no6)
											print("\n",time()-start,'seconds')
					numbers = list(d)
				numbers = list(c)
			numbers = list(b)
		numbers = list(a)
	numbers = list(z)
print('done')