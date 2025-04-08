from time import time
from itertools import combinations
start = time()

file = open("105 Project Euler.Txt",'r')
sets = file.read()
sets = sets.split('\n')         #add all numbers to list of raws
number_list = list()            #list of (list of numbers in raw) - [[],[],[],[],[]]
for x in sets:
        number_raw_list = x.split(',')
        number_list.append([int(i) for i in number_raw_list])     # a list of number list raws


def check(l):
    sub_set_sum =[[] for i in range(len(l)-1)]          # a list of lists
    for i in range(1,len(l)):
        for k in combinations(l,i):
            sum_k = sum(k)
            if sum_k in sub_set_sum[i-1]:               # S(B) ≠ S(C) and B = C
                return False 
            for j in range(1,i-1):                      # S(B) ≠ S(C) and B>C
                for number in sub_set_sum[j]:
                    if sum_k <= number:
                        return False
            sub_set_sum[i-1].append(sum_k)
    return True


ans = 0
for l in number_list:
    if check(l):
        ans += sum(l)
print(ans)

print(time()-start,"seconds")




'''
sub_set_sum[0] is a list of (combinations of 1 number)
sub_set_sum[1] is a list of (combinations of 2 numbers)
sub_set_sum[2] is a list of (combinations of 3 numbers)
sub_set_sum[3] is a list of (combinations of 4 numbers)
sub_set_sum[4] is a list of (combinations of 5 numbers)

Thejan -> 2021-03-10
'''
