
import sys


input = sys.stdin.read().split()

MOD = 10**9 + 7

idx = 0
t = int(input[idx])
idx += 1
test_cases = []
for _ in range(t):
    test_cases.append(int(input[idx]))
    idx += 1
max_amount = max(test_cases)
coins = [200, 100, 50, 20, 10, 5, 2, 1]

dp = [0] * (max_amount + 1)
dp[0] = 1  # Base case: one way to make 0 amount

for coin in coins:
    # if coin > max_amount:
    #     continue  # Skip coins larger than the maximum amount needed
    for j in range(coin, max_amount + 1):
        dp[j] = (dp[j] + dp[j - coin]) % MOD

for amount in test_cases:
    print(dp[amount] % MOD)
