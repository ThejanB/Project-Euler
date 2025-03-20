## woks but takes too long to run
## okay for about N = 10^5

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
    a = 1
    
    while p ** a <= N:
        b = 1
        while p ** a * q ** b <= N:
            max_val = max(max_val, p ** a * q ** b)
            b += 1
        a += 1
    
    return max_val

def compute_S(N):
    """Computes S(N) as the sum of all distinct M(p, q, N) values."""
    primes = sieve(N)
    seen_values = set()
    total_sum = 0
    
    # Iterate over all unique pairs (p, q)
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p, q = primes[i], primes[j]
            M_pqN = largest_valid_product(p, q, N)
            if M_pqN > 0 and M_pqN not in seen_values:
                seen_values.add(M_pqN)
                total_sum += M_pqN

    return total_sum

# Compute S(10^7)
N = 10**7
result = compute_S(N)
print(result)

print("Time:", time()-start, "seconds")