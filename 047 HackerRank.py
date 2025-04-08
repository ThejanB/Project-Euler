import sys
input = sys.stdin.read().split()
n = int(input[0])
k = int(input[1])

max_num = n + k - 1
factor_counts = [0] * (max_num + 1)

for i in range(2, max_num + 1):
    if factor_counts[i] == 0:  # i is a prime
        for j in range(i, max_num + 1, i):
            factor_counts[j] += 1

result = []
for x in range(2, n + 1):
    valid = True
    for i in range(k):
        current = x + i
        if current > max_num or factor_counts[current] != k:
            valid = False
            break
    if valid:
        result.append(x)

for num in result:
    print(num)
