def sieve(n):
    """Generate a list of primes up to n using the Sieve of Eratosthenes."""
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n**0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val]

MAX_N = 1000
primes = sieve(MAX_N)

dp = [0] * (MAX_N + 1)
dp[0] = 1  # 

for prime in primes:
    for i in range(prime, MAX_N + 1):
        dp[i] += dp[i - prime]

T = int(input())
for _ in range(T):
    N = int(input())
    print(dp[N])
