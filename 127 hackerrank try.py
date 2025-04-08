
import sys, math
import numpy as np
from numba import njit

def sieve_rad(n):
    rad = np.ones(n+1, dtype=np.int64)
    for p in range(2, n+1):
        if rad[p] == 1:  # p is prime
            for k in range(p, n+1, p):
                rad[k] *= p
    return rad

@njit
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

@njit
def compute_best_pair(N, A_MAX, rad, best_pair):
    for a in range(1, A_MAX):
        for b in range(a+1, N - a + 1):
            c = a + b
            if c > N:
                break
            if gcd(a, b) != 1:
                continue
            prod = rad[a] * rad[b]
            if prod < best_pair[c]:
                best_pair[c] = prod
    return best_pair

class FenwBIT:
    def __init__(self, n):
        self.n = n
        self.bit = [0]*(n+1)
    def update(self, i, val):
        while i <= self.n:
            self.bit[i] += val
            i += i & -i
    def query(self, i):
        s = 0
        while i:
            s += self.bit[i]
            i -= i & -i
        return s

def main():
    data = ['2', '1.0', '1000', '1.5', '1000'] 
    if not data:
        return
    t = int(data[0])
    queries = []
    maxL = 0
    idx = 1
    for i in range(t):
        r_val = float(data[idx]); L_val = int(data[idx+1])
        queries.append((r_val, L_val, i))
        if L_val > maxL:
            maxL = L_val
        idx += 2
    N = maxL   
    rad = sieve_rad(N)
    INF = 10**12
    best_pair = np.empty(N+1, dtype=np.int64)
    for c in range(N+1):
        best_pair[c] = INF
    for c in range(3, N+1):
        best_pair[c] = rad[c-1]
    A_MAX = min(N, 1000)
    best_pair = compute_best_pair(N, A_MAX, rad, best_pair)
    best_total = np.empty(N+1, dtype=np.int64)
    for c in range(N+1):
        best_total[c] = INF
    for c in range(3, N+1):
        best_total[c] = best_pair[c] * rad[c]
    r0_arr = np.empty(N+1, dtype=np.float64)
    for c in range(N+1):
        if c < 3:
            r0_arr[c] = 10.0  # dummy high value
        else:
            r0_arr[c] = math.log(best_total[c]) / math.log(c)
    r0_list = [(r0_arr[c], c) for c in range(3, N+1)]
    r0_list.sort(key=lambda x: x[0])
    BIT = FenwBIT(N)
    queries.sort(key=lambda x: x[0])
    res = [0] * len(queries)
    ptr = 0
    total = len(r0_list)
    for r_val, L_val, qi in queries:
        while ptr < total and r0_list[ptr][0] < r_val:
            c_val = r0_list[ptr][1]
            BIT.update(c_val, c_val)
            ptr += 1
        res[qi] = BIT.query(L_val - 1)
    sys.stdout.write("\n".join(str(x) for x in res))

if __name__ == '__main__':
    main()
