# correct cases - 3,4,11,16,17
# other cases - wrong

import sys
import math
from math import gcd

def minimal_pell(D):
    if D < 2:
        return (1, 0)
    m = 0
    d = 1
    a0 = int(math.isqrt(D))
    a = a0
    numm1 = 1
    num = a
    denm1 = 0
    den = 1
    while a != 2 * a0:
        m = d * a - m
        d = (D - m * m) // d
        if d == 0:
            break
        a = (a0 + m) // d
        numm2, numm1 = numm1, num
        denm2, denm1 = denm1, den
        num = a * numm1 + numm2
        den = a * denm1 + denm2
        if num * num - D * den * den == 1:
            return (num, den)
    return (a0, 1)

def find_min_solution(P, Q, D):
    K = Q - P
    if K <= 0:
        return None
    found = False
    for m in range(1, 100000):
        rhs = Q * m * m - K
        if rhs % P != 0:
            continue
        y_sq = rhs // P
        y = math.isqrt(y_sq)
        if y * y != y_sq:
            continue
        found = True
        x0, y0 = m, y
        break
    if not found:
        return None
    product = Q * P
    up, vp = minimal_pell(product)
    u_prev, v_prev = x0, y0
    min_T = None
    for _ in range(1000):
        T_candidate = (v_prev + 1) // 2
        B_candidate = (u_prev + 1) // 2
        if T_candidate > D:
            if min_T is None or T_candidate < min_T:
                min_T = T_candidate
                best_B = B_candidate
        u_next = u_prev * up + P * v_prev * vp
        v_next = v_prev * up + Q * u_prev * vp
        if v_next > 2 * (10**18):
            break
        u_prev, v_prev = u_next, v_next
    if min_T is not None:
        return (best_B, min_T)
    return None

def main():
    input = sys.stdin.read().split()
    T_cases = int(input[0])
    ptr = 1
    for _ in range(T_cases):
        P = int(input[ptr])
        Q = int(input[ptr+1])
        D = int(input[ptr+2])
        ptr += 3
        if gcd(P, Q) != 1:
            print("No solution")
            continue
        sol = find_min_solution(P, Q, D)
        if sol:
            print(sol[0], sol[1])
        else:
            print("No solution")

if __name__ == "__main__":
    main()
