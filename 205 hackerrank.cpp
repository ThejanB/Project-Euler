#include <iostream>
#include <vector>
using namespace std;

const int MOD = 1012924417;

// Function to compute the probability distribution of sums using dynamic programming
vector<long long> compute_distribution(int A, int a) {
    int max_sum = A * a;
    vector<long long> dp(max_sum + 1, 0);
    dp[0] = 1; // Base case: one way to make sum 0 with zero elements

    // Compute frequencies using DP
    for (int i = 0; i < A; i++) {
        vector<long long> new_dp(max_sum + 1, 0);
        for (int cur_sum = 0; cur_sum <= max_sum; cur_sum++) {
            if (dp[cur_sum] > 0) {
                for (int num = 1; num <= a; num++) {
                    if (cur_sum + num <= max_sum) {
                        new_dp[cur_sum + num] += dp[cur_sum];
                    }
                }
            }
        }
        dp = new_dp;
    }

    return dp;
}

// Function to compute modular inverse using Fermat’s theorem (modular exponentiation)
long long mod_inverse(long long base, long long exp, long long mod) {
    long long result = 1;
    while (exp > 0) {
        if (exp % 2 == 1) {
            result = (result * base) % mod;
        }
        base = (base * base) % mod;
        exp /= 2;
    }
    return result;
}

// Function to compute the probability of A winning over B
long long compute_wins(int A, int a, int B, int b) {
    vector<long long> x_list = compute_distribution(A, a);
    vector<long long> y_list = compute_distribution(B, b);

    int max_x = x_list.size();
    int max_y = y_list.size();

    // Compute prefix sums for y_list
    vector<long long> prefix_y(max_y, 0);
    prefix_y[0] = y_list[0];
    for (int i = 1; i < max_y; i++) {
        prefix_y[i] = prefix_y[i - 1] + y_list[i];
    }

    long long wins = 0;
    long long total_x = 0, total_y = 0;
    for (int i = 0; i < max_x; i++) {
        total_x += x_list[i];
    }
    for (int i = 0; i < max_y; i++) {
        total_y += y_list[i];
    }

    for (int x_val = 0; x_val < max_x; x_val++) {
        if (x_list[x_val] > 0) {
            wins += x_list[x_val] * (x_val > 0 ? prefix_y[min(x_val - 1, max_y - 1)] : 0);
        }
    }

    // Compute modular inverse of total cases
    long long total_cases = total_x * total_y % MOD;
    long long mod_inv = mod_inverse(total_cases, MOD - 2, MOD);

    return (wins % MOD * mod_inv % MOD) % MOD;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int A, a, B, b;
        cin >> A >> a >> B >> b;
        cout << compute_wins(A, a, B, b) << endl;
    }
    return 0;
}
