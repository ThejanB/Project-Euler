from time import time
start = time()
from itertools import takewhile,count,permutations

Triangle  = [int(n*(n+1)/2) for n in takewhile(lambda n: n*(n+1)/2<10000 , count(30)) if n*(n+1)/2>1000]
Square    = [int(n**2) for n in takewhile(lambda n: n**2<10000 , count(30)) if n**2>1000]
Pentagonal= [int(n*(3*n-1)/2) for n in takewhile(lambda n: n*(3*n-1)/2<10000 , count(20)) if n*(3*n-1)/2>1000]
Hexagonal = [int(n*(2*n-1)) for n in takewhile(lambda n: n*(2*n-1)<10000 , count(20)) if n*(2*n-1)>1000]
Heptagonal= [int(n*(5*n-3)/2) for n in takewhile(lambda n: n*(5*n-3)/2<10000 , count(20)) if n*(5*n-3)/2>1000]
Octagonal = [int(n*(3*n-2)) for n in takewhile(lambda n: n*(3*n-2)<10000 , count(10)) if n*(3*n-2)>1000]

def check(A,B,C,D,E,F):
        for a in A:
                for b in B:
                        if str(a)[:2:] != str(b)[2::]:
                                continue
                        for c in C:
                                if str(b)[:2:] != str(c)[2::]:
                                        continue
                                for d in D:
                                        if str(c)[:2:] != str(d)[2::]:
                                                continue
                                        for e in E:
                                                if str(d)[:2:] != str(e)[2::]:
                                                        continue
                                                for f in F:
                                                        if str(e)[:2:] != str(f)[2::]:
                                                                continue
                                                        if str(f)[:2:] != str(a)[2::]:
                                                                continue
                                                        print(a+b+c+d+e+f)
                                                        return True
        return False

for A,B,C,D,E,F in permutations([Triangle,Square,Pentagonal,Hexagonal,Heptagonal,Octagonal],6):
        if check(A,B,C,D,E,F) == True:
                break

print(time()-start,"seconds")
