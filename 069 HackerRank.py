
def precompute_primorials():
    primes = []
    is_prime = [True] * 100
    is_prime[0] = is_prime[1] = False
    for i in range(2, 100):
        if is_prime[i]:
            primes.append(i)
            for j in range(i*i, 100, i):
                is_prime[j] = False
    primorials = []
    product = 1
    for p in primes:
        if product * p > 1e18:
            break
        product *= p
        primorials.append(product)
    return primorials

primorials = precompute_primorials()

for _ in range(int(input())):
    N = int(input())
    left = 0
    right = len(primorials) - 1
    best = 2  # default answer for N >=3 is at least 2
    while left <= right:
        mid = (left + right) // 2
        if primorials[mid] < N:
            best = primorials[mid]
            left = mid + 1
        else:
            right = mid - 1
    print(best)
