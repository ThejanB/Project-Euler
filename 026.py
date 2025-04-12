import time
start = time.time()

''' only odd numbers for d have recurring cycles

	1/d = 0.abcabcabc....
	1000//d + 1/d = abc + 0.abcabcabc....
	number of 0s in 1000 is the number of recurring cycles	'''

no,longest_cycle = 0,0
for d in range(3,1000,2):	# skip evven numbers becouse (10*_)/2 == 0
	if d%5==0:	# skip 5*  -> becouse (10*_)/5 == 0
		continue
	count = 1
	while int((10**count))%d!=1:
		count += 1
	if count > longest_cycle:
		longest_cycle = count
		no = d
print("longest_cycle ",longest_cycle,"\nnumber is ",no)
print("\n" , time.time()-start , 'seconds')
