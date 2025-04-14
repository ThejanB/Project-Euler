# 66.67% HackerRank
# 1 case timelimit exceeded
#
# Wrote same code in java and it passed all test cases

MOD = 10**9+7
def NumberOfways(N):
    global MOD
    
    dp = [0] * (N + 1)
    dp[0] = 1

    for row in range(1, N + 1):
        for col in range(row, N + 1):
            dp[col] = (dp[col] + dp[col - row])%MOD

    return dp

inputs = []
for _ in range(int(input())):
    N = int(input())
    inputs.append(N)

ans = NumberOfways(max(inputs))
    
for i in inputs:
    print(ans[i])
