#include <iostream>
#include <vector>
#include <unordered_set>
#include <algorithm>

using namespace std;

vector<int> get_proper_divisor_sums(int limit) {
    vector<int> divisor_sums(limit + 1, 1);
    divisor_sums[0] = 0;
    for (int i = 2; i <= limit / 2; ++i) {
        for (int j = 2 * i; j <= limit; j += i) {
            divisor_sums[j] += i;
        }
    }
    return divisor_sums;
}

vector<int> get_abundant_numbers(const vector<int>& divisor_sums, int limit) {
    vector<int> abundants;
    for (int i = 1; i <= limit; ++i) {
        if (i < divisor_sums[i]) {
            abundants.push_back(i);
        }
    }
    return abundants;
}

unordered_set<int> get_sum_of_two_abundants(const vector<int>& abundants, int limit) {
    unordered_set<int> sum_of_2_abundants;
    for (size_t i = 0; i < abundants.size(); ++i) {
        for (size_t j = i; j < abundants.size(); ++j) {
            int sum = abundants[i] + abundants[j];
            if (sum <= limit) {
                sum_of_2_abundants.insert(sum);
            } else {
                break;
            }
        }
    }
    return sum_of_2_abundants;
}

int main() {
    int n;
    cin >> n;
    vector<int> number_list(n);
    int limit = 0;
    
    for (int i = 0; i < n; ++i) {
        cin >> number_list[i];
        limit = max(limit, number_list[i]);
    }
    
    vector<int> divisor_sums = get_proper_divisor_sums(limit);
    vector<int> abundants = get_abundant_numbers(divisor_sums, limit);
    unordered_set<int> sum_of_2_abundants = get_sum_of_two_abundants(abundants, limit);
    
    for (int num : number_list) {
        if (sum_of_2_abundants.find(num) != sum_of_2_abundants.end()) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }
    
    return 0;
}
