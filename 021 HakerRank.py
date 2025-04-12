def sum_of_divisors(n):
    """Returns the sum of proper divisors of n"""
    sum_div = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            sum_div += i
            if i != n // i:
                sum_div += n // i
    return sum_div

def precompute_amicable_numbers(limit):
    """Precomputes the sum of all amicable numbers up to a given limit"""
    amicable_sums = [0] * (limit + 1)
    divisor_sums = {}

    for i in range(1, limit + 1):
        divisor_sums[i] = sum_of_divisors(i)

    for a in range(1, limit + 1):
        b = divisor_sums[a]
        if b != a and b <= limit and divisor_sums.get(b, 0) == a:
            amicable_sums[a] = a
            amicable_sums[b] = b

    # Create a prefix sum array to allow quick queries
    for i in range(1, limit + 1):
        amicable_sums[i] += amicable_sums[i - 1]

    return amicable_sums

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    T = int(data[0])
    queries = list(map(int, data[1:T+1]))
    
    max_N = max(queries)
    amicable_sums = precompute_amicable_numbers(max_N)

    for N in queries:
        print(amicable_sums[N])

if __name__ == "__main__":
    main()
