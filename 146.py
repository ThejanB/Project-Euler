import sys
from math import prod

def is_probable_prime(n: int) -> bool:
    if n < 2:
        return False

    small_primes = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97)
    for p in small_primes:
        if n % p == 0:
            return n == p
    # write n-1 = d * 2^s
    d = n - 1
    s = (d & -d).bit_length() - 1  # number of trailing zeros
    d >>= s

    def check(a: int) -> bool:
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(s - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False

    # Deterministic set for 64-bit
    for a in (2, 3, 5, 7, 11, 13, 17):
        if a % n == 0:
            return True
        if not check(a):
            return False
    return True

WHEEL_PRIMES = (2, 3, 5, 7, 11, 13)
WHEEL_MOD = prod(WHEEL_PRIMES)

def admissible_residues(offsets):
    
    A = list(offsets)
    good = []
    for r in range(WHEEL_MOD):
        ok = True
        for p in WHEEL_PRIMES:
            rp2 = (r * r) % p
            for a in A:
                if (rp2 + a) % p == 0:
                    ok = False
                    break
            if not ok:
                break
        if ok:
            good.append(r)
    return good

def solve_one(L, offsets):
    a = sorted(offsets)
    # build list of positions inside [a1, a6] that must be composite
    a_set = set(a)
    gap_check = [b for b in range(a[0], a[-1] + 1) if b not in a_set]

    residues = admissible_residues(a)
    total = 0
    for r in residues:
        # iterate n === r (mod WHEEL_MOD)
        n = r
        if n == 0:
            n += WHEEL_MOD
        while n < L:
            s = n * n
            # primality of the six key positions
            good = True
            for ai in a:
                if not is_probable_prime(s + ai):
                    good = False
                    break
            if good:
                # ensure consecutiveness: every in-between value is composite
                for b in gap_check:
                    if is_probable_prime(s + b):
                        good = False
                        break
                if good:
                    total += n
            n += WHEEL_MOD
    return total


test_cases = int(input())
for _ in range(test_cases):
    L = int(input())
    offs = [int(i) for i in input().split()]
    print(str(solve_one(L, offs)))
