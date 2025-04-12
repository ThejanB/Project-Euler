from time import time
start = time()

candidates = list(range(10**7))
candidates[0] = 1
count = 0

for i in candidates[::-1]:
    if i ==  89:
        count+= 1 
        continue
    if i == 1:
        continue
    not_candidates =[i]
    while True:
        i = sum(int(j)**2 for j in str(i))
        not_candidates.append(i)
        if candidates[i] == 89:
            count+= 1
            for n in not_candidates:
                candidates[n] = 89
            break
        elif candidates[i] == 1:
            for n in not_candidates:
                candidates[n] = 1
            break        
print("count = ",count)
print(time()-start,"seconds")
