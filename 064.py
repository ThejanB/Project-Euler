from time import time
start = time()

def period(N):
    numerator = 0
    denominator = 1
    a = int(N**.5)
    periods = []
    check = []
    while [numerator,denominator] not in check:
        periods.append(a)
        check.append([numerator,denominator])
        
        numerator = denominator*a - numerator 
        denominator = (N-numerator**2)/denominator
        a = int ( (N**.5 + numerator) / denominator )

    return periods[1::]

count = 0
limit = 10000
for N in [i for i in range(2,limit+1) if (i**.5)%1 != 0]:
    if len(period(N))%2 == 1:
        count += 1
print(count)

print(time()-start,"seconds")
