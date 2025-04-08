# 91.18% in HackerRank
# I converted the code to C++. The C++ code got 100% in HackerRank.

import math

def is_palindrome_int(x):
    if x < 0:
        return False
    original = x
    rev = 0
    while x > 0:
        rev = rev * 10 + (x % 10)
        x //= 10
    return rev == original


for _ in range(int(input())):
    limit_, d = map(int, input().split())

    pal_sums = set()

    k = 1
    while True:
        C_k = (d*d) * (k*(k-1)*(2*k - 1) // 6)

        B_k = d * k * (k-1)
        S1 = k*1*1 + B_k*1 + C_k  # = k + B_k + C_k

        if S1 >= limit_:
            break

        D_ = limit_ - 1 - C_k
        if D_ < 0:
            k += 1
            continue

        disc = B_k*B_k + 4*k*D_
        if disc <= 0:
            k += 1
            continue

        sqrt_disc = int(math.isqrt(disc))
        n_max = ( -B_k + sqrt_disc ) // (2*k)
        if n_max < 1:
            k += 1
            continue

        S = S1
        if is_palindrome_int(S):
            pal_sums.add(S)

        for n in range(1, n_max):
            S += k*(2*n + 1) + B_k
            if S >= limit_:
                break
            if is_palindrome_int(S):
                pal_sums.add(S)

        k += 1

    print(sum(pal_sums))
