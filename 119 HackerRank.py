# 100% HackerRank

import sys, math

def sum_digits_base(N, B):
    s = 0
    while N:
        s += N % B
        N //= B
    return s

def interesting_numbers(B):
    LIMIT = 10**100
    d_max = int(math.log(LIMIT-1, B)) + 1
    S_max = (B-1) * d_max

    interesting = set()
    for S in range(2, S_max+1):
        N = S * S
        k = 2
        while N < LIMIT:
            if N >= B and sum_digits_base(N, B) == S:
                interesting.add(N)
            k += 1
            N *= S

    for x in sorted(interesting):
        print(x, end=' ')
    print()

B = int(input().strip())
interesting_numbers(B)
