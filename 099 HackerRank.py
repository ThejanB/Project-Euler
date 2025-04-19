# 100% HackerRank	

import math

sorted_numbers = [] # (lg_k, a, b)
for _ in range(int(input())):
    a, b = map(int, input().split())
    lg_k = b*math.log10(a)
    sorted_numbers.append((lg_k, a, b))

sorted_numbers.sort()
K = int(input())
lg_k, max_a, max_b = sorted_numbers[K-1] 
print(max_a, max_b)
