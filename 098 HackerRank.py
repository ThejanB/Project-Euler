# 100% HackerRank
# 
# the largest set of square anagrams for a number with N digits
# This is easy than the project euler problem 98

from math import isqrt

N = int(input  ())  # N = digits

numbers_memo = {}
for i in range(isqrt(10**(N-1)), isqrt(10**N)+1):
    no = i**2

    str_no = list(str(no))
    str_no.sort()
    str_no = ''.join(str_no)

    if str_no in numbers_memo:
        numbers_memo[str_no] = [  numbers_memo[str_no][0]+1, max(numbers_memo[str_no][1], no) ]
    else:
        numbers_memo[str_no] = [1, no]

max_count = 0
max_no = 0
for key in numbers_memo:
    if numbers_memo[key][0] > max_count:
        max_count, max_no = numbers_memo[key]
    elif numbers_memo[key][0] == max_count and numbers_memo[key][1] > max_no:
        max_no = numbers_memo[key][1]

print(max_no)



    

