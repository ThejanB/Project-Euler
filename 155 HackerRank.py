# 88.24% Hackerrank
# 2 cases time limit exceeded

# solution for n = 17 -> 1529533
# solution for n = 18 -> 3857447

import math

n = int(input())

if n == 0:
    print(0)
else:
    dp = [set() for _ in range(n + 1)]
    dp[1].add((1, 1))  # (numerator, denominator)

    for k in range(2, n + 1):
        for i in range(1, k // 2 + 1):
            j = k - i
            for a_num, a_den in dp[i]:
                for b_num, b_den in dp[j]:
                    sum_num = a_num * b_den + b_num * a_den
                    sum_den = a_den * b_den
                    gcd_val = math.gcd(sum_num, sum_den)
                    dp[k].add((sum_num // gcd_val, sum_den // gcd_val))
                    series_num = a_num * b_num
                    series_den = a_num * b_den + b_num * a_den
                    if series_den != 0:
                        gcd_val = math.gcd(series_num, series_den)
                        dp[k].add((series_num // gcd_val, series_den // gcd_val))
    
    total = set()
    for k in range(1, n + 1):
        total.update(dp[k])
    
    print(len(total))