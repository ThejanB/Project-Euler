mod = 1012924417

def compute_distribution(A, a):
    """Computes the probability distribution of sums using dynamic programming."""
    max_sum = A * a
    dp = [0] * (max_sum + 1)
    dp[0] = 1  # Base case: one way to make sum 0 with zero elements

    # Compute frequencies using dynamic programming
    for _ in range(A):
        new_dp = [0] * (max_sum + 1)
        for cur_sum in range(max_sum + 1):
            if dp[cur_sum] > 0:
                for num in range(1, a + 1):
                    new_dp[cur_sum + num] += dp[cur_sum]
        dp = new_dp

    return dp

def compute_wins(A, a, B, b):
    """Computes the probability of A winning over B using DP and prefix sums."""
    x_list = compute_distribution(A, a)
    y_list = compute_distribution(B, b)

    max_x = len(x_list)
    max_y = len(y_list)

    # Compute prefix sums for y_list
    prefix_y = [0] * max_y
    prefix_y[0] = y_list[0]
    for i in range(1, max_y):
        prefix_y[i] = prefix_y[i - 1] + y_list[i]

    wins = 0
    total_x = sum(x_list)
    total_y = sum(y_list)

    for x_val in range(max_x):
        if x_list[x_val] > 0:
            wins += x_list[x_val] * (prefix_y[min(x_val - 1, max_y - 1)] if x_val > 0 else 0)

    # Compute modular inverse of total cases
    total_cases = total_x * total_y
    mod_inverse = pow(total_cases, mod - 2, mod)

    return (wins * mod_inverse) % mod

# Read input and compute results
t = int(input().strip())
for _ in range(t):
    A, a, B, b = map(int, input().split())
    print(round(compute_wins(A, a, B, b), 7))
