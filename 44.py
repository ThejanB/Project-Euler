import time
start = time.time()

list1 = []		# pentagon number list
for i in range(1,2500):
	list1.append(i*(i*3-1)/2)

'''		no = i*(i*3-1)/2
		i = (1+(24*no+1)**0.5)/6
		i must be a intiger
		so i%1 == 0 					'''

k = 0
for i in list1:
        for j in list1:
                if i > j:
                        if ((1+(24*(i+j)+1)**0.5)/6)%1==0:
                                if ((1+(24*(i-j)+1)**0.5)/6)%1==0:
                                        print(i-j)
                                        k = 1
        if k==1:
                break

print("\n" , time.time()-start , 'seconds')
