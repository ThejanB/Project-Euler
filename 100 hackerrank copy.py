# corrct cases - 3,4,6,15 
# other cases - wrong

import sys
import math
from math import gcd

def is_perfect_square(n):
    s = int(math.isqrt(n))
    return s * s == n

def chakravala(D):
    if is_perfect_square(D):
        return None  # No solution if D is a perfect square
    m = 1
    k = 1
    a, b = 1, 0
    max_iter = 1000  # Prevent infinite loops
    iter_count = 0
    while k != 1 or b == 0:
        if iter_count > max_iter:
            return None
        iter_count += 1
        abs_k = abs(k)
        if abs_k == 0:
            return None
        m_start = max(int(math.isqrt(D)) - 10, 1)
        found = False
        for m_candidate in range(m_start, m_start + 20):
            if (a + b * m_candidate) % abs_k == 0:
                m = m_candidate
                found = True
                break
        if not found:
            return None
        a_prev, b_prev, k_prev = a, b, k
        a = (a_prev * m + D * b_prev) // abs_k
        b = (a_prev + b_prev * m) // abs_k
        k = (m**2 - D) // k_prev
    return (a, b)

def find_min_solution(P, Q, D):
    K = Q - P
    if K <= 0:
        return None
    product = Q * P
    if is_perfect_square(product):
        return None
    sol_pell = chakravala(product)
    if not sol_pell:
        return None
    up, vp = sol_pell
    x0, y0 = None, None
    for m in range(1, 100000):
        rhs = Q * m**2 - K
        if rhs % P != 0:
            continue
        y_sq = rhs // P
        y = math.isqrt(y_sq)
        if y * y != y_sq:
            continue
        x0, y0 = m, y
        break
    if x0 is None:
        return None
    u_prev, v_prev = x0, y0
    min_T = None
    for _ in range(100):
        T_candidate = (v_prev + 1) // 2
        B_candidate = (u_prev + 1) // 2
        if T_candidate > D:
            if (min_T is None) or (T_candidate < min_T):
                min_T = T_candidate
                best_B = B_candidate
        u_next = u_prev * up + P * v_prev * vp
        v_next = v_prev * up + Q * u_prev * vp
        if v_next > 2 * (10**18):
            break
        u_prev, v_prev = u_next, v_next
    return (best_B, min_T) if min_T is not None else None

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
