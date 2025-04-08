#include <iostream>
#include <unordered_map>
#include <cmath>
#include <vector>

using namespace std;

unordered_map<int, int> cache; // Store computed results
vector<int> max_values = {1, 1}; // Store last checked index and triangle number
int last_cache_value = 0;

int count_factors(int n) {
    if (cache.find(n) != cache.end()) {
        return cache[n];
    }

    int count = 0;
    int sqrt_n = static_cast<int>(sqrt(n));

    for (int x = 1; x <= sqrt_n; ++x) {
        if (n % x == 0) {
            count += 2; // Count both `x` and `n/x`
        }
    }

    if (sqrt_n * sqrt_n == n) { // If n is a perfect square, adjust count
        count -= 1;
    }

    return count;
}

int first_triangle_with_divisors(int n) {
    if (cache.find(n) != cache.end()) {
        return cache[n];
    }

    int x = max_values[0]; // Start from last checked triangle number
    int T_no = max_values[1];
    int count = count_factors(T_no);

    while (count <= n) {
        x += 1;
        T_no += x;
        count = count_factors(T_no);

        if (cache.find(count - 1) == cache.end()) {
            for (int k = last_cache_value + 1; k < count; ++k) {
                cache[k] = T_no;
            }
            last_cache_value = count - 1;
        }
    }

    if (cache.find(n) == cache.end()) {
        cache[n] = T_no;
    }

    max_values[0] = x;  // Update last checked index
    max_values[1] = T_no; // Update last checked triangle number

    return T_no;
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n;
        cin >> n;
        cout << first_triangle_with_divisors(n) << endl;
    }

    return 0;
}
