import time
start = time.time()

totsum = 0

for a in range(1,10000):
	sum1,sum2 = 0,0
	for x in range(1,int(a**0.5)):
		if a%x == 0:
			sum1 += x +a//x
	if a%(a**0.5)==0:
		sum1 += a**0.5

	b = sum1 -a     # a%1 == 0  -> sum1 += 1+a ,so we have to cutback a
	if 0<b<= 10000 and a!=b!=0:
		for x in range(1,int(b**0.5)):
			if b%x == 0:
				sum2 += x+b//x
		if b%(b**0.5)==0:
			sum2 += b**0.5

		if sum2-b == a:
			totsum += a

print(totsum)
print(time.time()-start , 'seconds')
