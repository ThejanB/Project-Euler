# corrct cases - 0,3,4,6,15 
# other cases - wrong

import sys
import math

def is_perfect_square(n):
    if n < 0:
        return False
    r = int(math.isqrt(n))
    return r * r == n

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def minimal_pell(D):
    if D < 2:
        return (1, 0)
    a0 = int(math.isqrt(D))
    if a0 * a0 == D:
        return (0, 0)
    
    m = 0
    d = 1
    a = a0
    num_m1, num = 1, a 
    den_m1, den = 0, 1    
    
    while True:
        m = d * a - m
        d = (D - m * m) // d
        a = (a0 + m) // d
        
        num_m2, num_m1 = num_m1, num
        den_m2, den_m1 = den_m1, den
        
        num = a * num_m1 + num_m2
        den = a * den_m1 + den_m2
        
        if num * num - D * (den * den) == 1:
            return (num, den)

def solve_one_case(P, Q, Dmin):
    if gcd(P, Q) != 1:
        return None  # No solution
    
    product = P * Q
    if is_perfect_square(product):
        return None
    
    target = Q - P  # right side of Q*X^2 - P*Y^2 = Q - P
    X0, Y0 = None, None
    limit_initial_search = 200000  # adjust if needed
    found_initial = False
    
    # Only search odd m (starting from 3 to skip trivial m==1) and require y is odd.
    for m in range(3, limit_initial_search + 1, 2):
        lhs = Q * (m * m) - target
        if lhs < 0:
            continue
        if lhs % P != 0:
            continue
        y_sq = lhs // P
        y = int(math.isqrt(y_sq))
        if y * y != y_sq:
            continue
        # Ensure non-trivial (m,y) with both odd:
        if y % 2 == 0:
            continue
        X0, Y0 = m, y
        found_initial = True
        break
    
    if not found_initial:
        return None
    
    (up, vp) = minimal_pell(product)
    if up == 0 and vp == 0:
        return None
    
    u_curr, v_curr = X0, Y0
    best_T = None
    best_B = None
    max_iterations = 2000
    
    for _ in range(max_iterations):
        # Only consider if both u_curr and v_curr are odd
        if (u_curr % 2 == 1) and (v_curr % 2 == 1):
            B_candidate = (u_curr + 1) // 2
            T_candidate = (v_curr + 1) // 2
            if B_candidate > 0 and T_candidate > 0:
                lhs = B_candidate * (B_candidate - 1) * Q
                rhs = P * T_candidate * (T_candidate - 1)
                if lhs == rhs and T_candidate > Dmin:
                    if best_T is None or T_candidate < best_T:
                        best_T = T_candidate
                        best_B = B_candidate
        
        # Compute next solution using the Pell transformation:
        u_next = u_curr * up + P * v_curr * vp
        v_next = v_curr * up + Q * u_curr * vp
        u_curr, v_curr = u_next, v_next
        
        if v_curr > 2 * (10**18):
            break
    
    if best_T is not None:
        return (best_B, best_T)
    else:
        return None

data = sys.stdin.read().strip().split()
t = int(data[0])
idx = 1
for _ in range(t):
    P = int(data[idx]); Q = int(data[idx+1]); D = int(data[idx+2])
    idx += 3
    ans = solve_one_case(P, Q, D)
    if ans is None:
        print("No solution")
    else:
        b, t_ = ans
        print(b, t_)
