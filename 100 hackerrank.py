# 27.8% 

import math

def solve():
    results = []
    # Process each test case.
    for i in range(int(input())):
        P, Q, N = [int(x) for x in input().split()]
        

        if P == 1:
            if  Q == 2:
                blue,total = 3,4
                while True:
                    if total>N:
                        results.append(f"{blue} {total}")
                        break
                    blue,total = 3*blue+2*total-2,4*blue+3*total-3      # I got this equation by using "Dario Alpern's Generic two integer variable equation solver"
                continue
            
            if Q == 4:
                results.append("No solution")   # I got this equation by using "Dario Alpern's Generic two integer variable equation solver"
                continue

        found = False
        # t must be greater than N.
        t = N + 1
        # Set an arbitrary limit for t; adjust if necessary.
        limit = 10**6  
        while t <= limit:
            # For a solution, P*t*(t-1) must be divisible by Q.
            if (P * t * (t - 1)) % Q == 0:
                X = (P * t * (t - 1)) // Q  # This should equal b(b-1)
                disc = 1 + 4 * X
                s = math.isqrt(disc)
                if s * s == disc:
                    # b = (1 + s) / 2 must be an integer.
                    if (1 + s) % 2 == 0:
                        b = (1 + s) // 2
                        if b < t and b > 0:
                            # Verify the equation holds.
                            if Q * b * (b - 1) == P * t * (t - 1):
                                results.append(f"{b} {t}")
                                found = True
                                break
            t += 1
        if not found:
            results.append("No solution")
    
    for result in results:
        print(result)
    
if __name__ == '__main__':
    solve()
