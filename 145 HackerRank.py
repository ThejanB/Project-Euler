# 33% HackerRank

def is_reversible(n):
    s = str(n)
    if s[-1] == '0':
        return False
    reversed_n = int(s[::-1])
    total = n+reversed_n
    for digit in str(total):
        if int(digit) % 2 == 0:
            return False
    return True

def precompute_reversible_numbers(limit):
    reversible = []
    for n in range(1, limit):
        if is_reversible(n):
            reversible.append(n)
    return reversible

T = int(input())
queries = []
for _ in range(T):
    queries.append(int(input()))
max_query = max(queries)
reversible_numbers = precompute_reversible_numbers(max_query + 1)
reversible_numbers.sort()
for N in queries:
    left, right = 0, len(reversible_numbers)
    while left < right:
        mid = (left + right) // 2
        if reversible_numbers[mid] < N:
            left = mid + 1
        else:
            right = mid
    print(left)

