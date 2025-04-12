from time import time
start = time()

p,q,count =3,2,0

for x in range(1000):
	p,q = (p+2*q),(p+q)
	if len(str(p))>len(str(q)):
		count += 1
print(count)

print(time()-start , 'seconds')