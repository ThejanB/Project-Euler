#  correct cases 6,15,17
#  other cases - Time limit exceeded

import math

def find_initial_solution(p, q):
    g = math.gcd(p, q)
    p1 = p // g
    q1 = q // g
    if int(math.isqrt(p*q))**2 == p*q:
        return None
    m = 0
    while True:
        m += 1
        for sign in [-1, 1]:
            Y = m * q1 + sign * 1
            if Y <= 1:
                continue
            if Y % 2 == 0:
                continue
            val = p * Y * Y + (q - p)
            if val % q != 0:
                continue
            X2 = val // q
            if X2 < 0:
                continue
            X = math.isqrt(X2)
            if X * X != X2:
                continue
            if X <= 1:
                continue
            if X % 2 == 0:
                continue
            B = (X + 1) // 2
            T = (Y + 1) // 2
            if B * (B - 1) * q == T * (T - 1) * p:
                return (B, T)
    return None

def solve():
    t = int(input())
    results = []
    index = 1
    for _ in range(t):
        P, Q , D_min = map(int, input().split())
        index += 3
        solution = find_initial_solution(P, Q)
        if solution is None:
            print("No solution")
            continue
        B, T = solution
        if T > D_min:
            print(f"{B} {T}")
            continue
        D = P * Q
        a0 = int(math.isqrt(D))
        if a0 * a0 == D:
            print("No solution")
            continue
        m = 0
        d = 1
        a = a0
        h1, h2 = 1, 0
        k1, k2 = 0, 1
        fundamental_x = None
        fundamental_y = None
        seen = set()
        while True:
            m = d * a - m
            d = (D - m * m) // d
            a = (a0 + m) // d
            h = a * h1 + h2
            k = a * k1 + k2
            h2, h1 = h1, h
            k2, k1 = k1, k
            if h * h - D * k * k == 1:
                fundamental_x, fundamental_y = h, k
                break
        Xr = 2 * B - 1
        Yr = 2 * T - 1
        X_curr, Y_curr = Xr, Yr
        found = False
        for _ in range(1000):
            X_new = fundamental_x * X_curr + fundamental_y * Y_curr
            Y_new = fundamental_x * Y_curr + fundamental_y * D * X_curr
            X_curr, Y_curr = X_new, Y_new
            if X_curr % 2 != 1 or Y_curr % 2 != 1:
                continue
            B_new = (X_curr + 1) // 2
            T_new = (Y_curr + 1) // 2
            if B_new * (B_new - 1) * Q == T_new * (T_new - 1) * P:
                if T_new > D_min:
                    print(f"{B_new} {T_new}")
                    found = True
                    break
        if not found:
            print("No solution")
solve()