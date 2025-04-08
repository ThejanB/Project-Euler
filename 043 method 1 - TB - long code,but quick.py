from time import time
from itertools import permutations

start = time()

rest = {'0','1','2','3','4','5','6','7','8','9'}
ans  = 0 
cc = 0
for d in {'0','2','4','6','8'}:
	for f in {'0','5'} - {d}:
		rest_1 = rest - {d,f}
		for g,h in permutations(rest_1,2):
			if int(f+g+h)%11 == 0:
				rest_2 = rest_1 - {g,h}
				for i in rest_2:
					if int(g+h+i)%13 == 0:
						rest_3 = rest_2 - {i}
						for j in rest_3:
							if int(h+i+j)%17 == 0:
								rest_4 = rest_3 - {j}
								for e in rest_4:
									if int(e+f+g)%7 == 0:
										rest_5 = rest_4 - {e}
										for c in rest_5:
											if int(c+d+e)%3 == 0:
												for a,b in permutations( rest_5 - {c} , 2 ):
													if a == '0':
														continue
													ans += int(a+b+c+d+e+f+g+h+i+j)
													#print(int(a+b+c+d+e+f+g+h+i+j))

print(ans)
print(time()-start , 'seconds')