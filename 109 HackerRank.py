import sys
def main():
    mod = 10**9 + 9

    N = int(input())
    if N <= 0:
        print(0)
        return

    max_score = 60
    a = [0]*(max_score+1)    
    doubles = []
    for s in range(1,21):
        a[s] += 1
    a[25] += 1
    for d in range(1,21):
        a[2*d] += 1
        doubles.append(2*d)
    a[50] += 1
    doubles.append(50)
    for t in range(1,21):
        a[3*t] += 1

    D = set(doubles)
    if N <= max_score:
        u = [0]*(N+1)
        u[0] = 1
        for n in range(1, N+1):
            s = 0
            for i in range(1, min(n, max_score)+1):
                if a[i]:
                    s += a[i]*u[n-i]
            u[n] = s % mod

        f = [0]*(N+1)
        S = [0]*(N+1)
        for n in range(1, N+1):
            s = 0
            for j in doubles:
                if j <= n:
                    s += u[n-j]
            f[n] = s % mod
            S[n] = (S[n-1] + f[n]) % mod

        print(S[N])
        return

    d = max_score
    u = [0]*(d+1)
    u[0] = 1
    for n in range(1, d+1):
        s = 0
        for i in range(1, n+1):
            if a[i]:
                s += a[i]*u[n-i]
        u[n] = s % mod

    f = [0]*(d+1)
    S = [0]*(d+1)
    for n in range(1, d+1):
        s = 0
        for j in doubles:
            if j <= n:
                s += u[n-j]
        f[n] = s % mod
        S[n] = (S[n-1] + f[n]) % mod

    size = d+1
    M = [[0]*size for _ in range(size)]
    for j in range(d):
        M[0][j] = a[j+1] % mod
    for i in range(1, d):
        M[i][i-1] = 1
    for j in range(d):
        M[d][j] = a[j+1] % mod
    M[d][d] = 1

    def mat_mul(A, B):
        C = [[0]*size for _ in range(size)]
        for i in range(size):
            Ai = A[i]
            Ci = C[i]
            for k in range(size):
                aik = Ai[k]
                if aik:
                    rowB = B[k]
                    for j in range(size):
                        Ci[j] = (Ci[j] + aik * rowB[j]) % mod
        return C

    def mat_pow(mat, exp):
        R = [[0]*size for _ in range(size)]
        for i in range(size):
            R[i][i] = 1
        base = mat
        while exp:
            if exp & 1:
                R = mat_mul(R, base)
            base = mat_mul(base, base)
            exp >>= 1
        return R

    V0 = [0]*size
    for j in range(d):
        V0[j] = f[d-j]
    V0[d] = S[d]

    Mexp = mat_pow(M, N - d)
    VN = [0]*size
    for i in range(size):
        s = 0
        Mi = Mexp[i]
        for j in range(size):
            s += Mi[j]*V0[j]
        VN[i] = s % mod

    print(VN[d])


main()
