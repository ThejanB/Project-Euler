#include <iostream>
#include <vector>
#include <sstream>
#include <limits>
#include <algorithm>

using namespace std;

vector<vector<long long>> matrix;
long long rows, cols;

// Compute the minimal path sum from left to right
long long min_path_sum() {
    vector<vector<long long>> dp = matrix; // Copy the matrix for DP updates

    // Process column by column from left to right
    for (long long c = 1; c < cols; c++) {
        // First pass: move from left (right movement)
        for (long long r = 0; r < rows; r++) {
            dp[r][c] += dp[r][c - 1]; // Directly from left
        }

        // Second pass: move top-down (downward movement)
        for (long long r = 1; r < rows; r++) {
            dp[r][c] = min(dp[r][c], dp[r - 1][c] + matrix[r][c]);
        }

        // Third pass: move bottom-up (upward movement)
        for (long long r = rows - 2; r >= 0; r--) {
            dp[r][c] = min(dp[r][c], dp[r + 1][c] + matrix[r][c]);
        }
    }

    // The answer is the minimum value in the last column
    long long min_value = dp[0][cols - 1];
    for (long long r = 1; r < rows; r++) {
        min_value = min(min_value, dp[r][cols - 1]);
    }

    return min_value;
}

int main() {
    long long t;
    cin >> t;
    cin.ignore(); // Ignore newline after input

    matrix.resize(t);
    
    for (long long i = 0; i < t; i++) {
        string line;
        getline(cin, line);
        stringstream ss(line);
        long long num;
        while (ss >> num) {
            matrix[i].push_back(num);
        }
    }

    rows = matrix.size();
    cols = matrix[0].size();

    cout << min_path_sum() << endl;

    return 0;
}
