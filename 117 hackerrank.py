MOD = 10**9 + 7

def matrix_mult(A, B):
    """Multiplies two 4x4 matrices under modulo MOD."""
    return [[sum(A[i][k] * B[k][j] for k in range(4)) % MOD for j in range(4)] for i in range(4)]

def matrix_exponentiation(matrix, exp):
    """Computes matrix exponentiation in O(log n) time."""
    result = [[1 if i == j else 0 for j in range(4)] for i in range(4)]
    base = matrix
    
    while exp:
        if exp % 2:
            result = matrix_mult(result, base)
        base = matrix_mult(base, base)
        exp //= 2
    
    return result

def count_ways(n):
    """Returns the number of ways to tile a row of length n using matrix exponentiation."""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    elif n == 4:
        return 8
    
    # Transformation matrix
    T = [
        [1, 1, 1, 1],  # f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4)
        [1, 0, 0, 0],  # f(n-1) = f(n-1)
        [0, 1, 0, 0],  # f(n-2) = f(n-2)
        [0, 0, 1, 0]   # f(n-3) = f(n-3)
    ]
    
    # Compute T^(n-4)
    T_exp = matrix_exponentiation(T, n-4)
    
    # Base cases as a vector
    F = [8, 4, 2, 1]  # [f(4), f(3), f(2), f(1)]
    
    # Compute f(n) using matrix multiplication
    result = sum(T_exp[0][i] * F[i] for i in range(4)) % MOD
    return result

### For Hackerrank ###
T = int(input().strip())
for _ in range(T):
    n = int(input().strip())
    print(count_ways(n))


