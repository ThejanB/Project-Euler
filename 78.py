from time import time
start = time()
# Function to find the total number of ways to represent N as the sum of integers over the range [1, K]
def NumberOfways(N, K, div_by):
    mod = 10_000_000
    
    dp = [0] * (N + 1)
    dp[0] = 1

    for row in range(1, K + 1):
        for col in range(row, N + 1):
            dp[col] = (dp[col] + dp[col - row])%mod

        if dp[row]%div_by == 0:
            print("ANSWER FOUND")
            return (row, dp[row])
    
    print("ANSWER NOT FOUND")
    return (N, dp[N])

# N = number
# K = maxinum number 
# eg -> for N = 6 K = 3 , 7 ways
#           6 = 1+1+1+1+1+1
#           6 = 1+1+1+1+2
#           6 = 1+1+2+2
#           6 = 2+2+2
#           6 = 1+1+1+3
#           6 = 1+2+3
#           6 = 3+3

# In this case both N and K are same
K = N = 60_000
div_by = 1_000_000

ans = NumberOfways(N, K, div_by)
print(ans)

print(time()-start,"seconds")

# answer = 55374
# took 144 seconds (2 min 24 seconds)
'''
# code to find number of ways
def NumberOfways(N, K):
    
    dp = [0] * (N + 1)
    dp[0] = 1

    for row in range(1, K + 1):
        for col in range(row, N + 1):
            dp[col] = (dp[col] + dp[col - row])%mod
    
    return dp[N]

##### Mr.T ##### 
'''