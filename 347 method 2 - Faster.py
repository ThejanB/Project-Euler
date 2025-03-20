import math
from time import time

start = time()

def sieve(limit):
    """Returns a list of primes up to 'limit' using the Sieve of Eratosthenes."""
    is_prime = [True] * (limit + 1)
    is_prime[0] = is_prime[1] = False
    primes = []
    
    for num in range(2, limit + 1):
        if is_prime[num]:
            primes.append(num)
            for multiple in range(num * num, limit + 1, num):
                is_prime[multiple] = False
                
    return primes

def largest_valid_product(p, q, N):
    """Finds the largest integer ≤ N that is only divisible by p and q."""
    max_val = 0
    a, power_p = 1, p

    while power_p <= N:
        b, power_q = 1, q
        while power_p * power_q <= N:
            candidate = power_p * power_q
            if candidate <= N:
                max_val = max(max_val, candidate)
            if power_q > N // q:  # Prevent overflow
                break
            power_q *= q  # Multiply q exponentially
            b += 1
        if power_p > N // p:  # Prevent overflow
            break
        power_p *= p  # Multiply p exponentially
        a += 1
    
    return max_val

def compute_S(N):
    """Computes S(N) efficiently using optimized prime pair iteration and fast exponentiation."""
    primes = sieve(N)  # Use primes up to N
    seen_values = set()
    total_sum = 0
    
    for i in range(len(primes)):
        p = primes[i]
        if p * p > N:  # No need to check if p^2 > N
            break
        for j in range(i + 1, len(primes)):
            q = primes[j]
            if p * q > N:  # If even p*q is larger than N, break early
                break
            M_pqN = largest_valid_product(p, q, N)
            if M_pqN > 0 and M_pqN not in seen_values:
                seen_values.add(M_pqN)
                total_sum += M_pqN

    return total_sum

# Compute S(100) as a test case
print("S(100) =", compute_S(100))  # Should output 2262

# Compute S(10^7)
print("S(10^7) =", compute_S(10**7))  # Final large-scale computation

print("Time:", time()-start, "seconds")  