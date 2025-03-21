import sys
import math

def sieve(limit):
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(math.sqrt(limit)) + 1):
        if sieve[i]:
            sieve[i*i : limit+1 : i] = [False] * len(sieve[i*i : limit+1 : i])
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    return primes

def is_prime(n):
    if n < 2:
        return False
    for p in [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]:
        if n % p == 0:
            return n == p
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in [2, 325, 9375, 28178, 450775, 9780504, 1795265022]:
        if a >= n:
            continue
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(s - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_primes():
    initial_primes = sieve(5000000)
    sum_primes = sum(initial_primes)
    candidate = initial_primes[-1] + 2 if initial_primes else 2
    while sum_primes <= 10**12:
        if is_prime(candidate):
            initial_primes.append(candidate)
            sum_primes += candidate
            if sum_primes > 10**12:
                break
        candidate += 1
    return initial_primes

primes = generate_primes()
prefix_sums = [0] * (len(primes) + 1)
for i in range(len(primes)):
    prefix_sums[i+1] = prefix_sums[i] + primes[i]

def find_largest_prime(N):
    left, right = 0, len(primes)
    while left < right:
        mid = (left + right) // 2
        if primes[mid] > N:
            right = mid
        else:
            left = mid + 1
    for p in reversed(primes[:left]):
        if p <= N and is_prime(p):
            return p
    return 2  # Fallback

def solve_case(N):
    L_max = 0
    low, high = 0, len(prefix_sums) - 1
    while low <= high:
        mid = (low + high) // 2
        if prefix_sums[mid] <= N:
            L_max = mid
            low = mid + 1
        else:
            high = mid - 1

    best_sum = None
    best_len = 0

    for L in range(L_max, 0, -1):
        sum_first = prefix_sums[L]
        if sum_first > N:
            continue
        if is_prime(sum_first):
            return (sum_first, L)
        low_i = 1
        high_i = len(primes) - L
        i_max = 0
        while low_i <= high_i:
            mid_i = (low_i + high_i) // 2
            s = prefix_sums[mid_i + L] - prefix_sums[mid_i]
            if s <= N:
                i_max = mid_i
                low_i = mid_i + 1
            else:
                high_i = mid_i - 1
        for i in range(1, i_max + 1):
            s = prefix_sums[i + L] - prefix_sums[i]
            if s > N:
                break
            if is_prime(s):
                if best_len < L or (best_len == L and s < best_sum):
                    best_sum = s
                    best_len = L
                    break  # Earliest i gives smallest sum for current L
        if best_sum is not None:
            break  # Break outer loop since we're checking from largest L down

    if best_sum is not None:
        return (best_sum, best_len)
    else:
        largest_p = find_largest_prime(N)
        return (largest_p, 1)

def main():
    input = sys.stdin.read().split()
    T = int(input[0])
    idx = 1
    for _ in range(T):
        N = int(input[idx])
        idx += 1
        if N == 2:
            print("2 1")
            continue
        elif N <= 3:
            print("3 1")
            continue
        result = solve_case(N)
        if result[1] == 1:
            print(result[0])
        else:
            print(f"{result[0]} {result[1]}")

main()
