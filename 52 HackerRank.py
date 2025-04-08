def has_same_digits(x, k):
    """Check if x, 2x, ..., kx have the same digits"""
    sorted_x = sorted(str(x))  # Sort digits of x
    for i in range(2, k + 1):
        multiple = x * i
        if sorted(str(multiple)) != sorted_x:  # Compare sorted digits
            return False
    return True

def find_valid_numbers(N, K):
    """Find all numbers x <= N that satisfy the condition"""
    results = []
    for x in range(1,N + 1):  # Start search from the lowest bound
        if has_same_digits(x, K):
            results.append([x] + [x * i for i in range(2, K + 1)])
    return results

N, K = map(int, input().split())

valid_numbers = find_valid_numbers(N, K)
for numbers in valid_numbers:
    print(" ".join(map(str, numbers)))
