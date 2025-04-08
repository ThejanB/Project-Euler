#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> prime_list(int n) {
    vector<int> candidates(n + 1, 1);
    candidates[0] = candidates[1] = 0; // 0 and 1 are not prime
    
    for (int i = 4; i <= n; i += 2) {
        candidates[i] = 0; // Mark even numbers as non-prime (except 2)
    }
    
    for (int i = 3; i * i <= n; i += 2) {
        if (candidates[i]) {
            for (int j = i * i; j <= n; j += i) {
                candidates[j] = 0; // Mark multiples as non-prime
            }
        }
    }
    
    vector<int> primes;
    for (int i = 2; i <= n; ++i) {
        if (candidates[i]) {
            primes.push_back(i);
        }
    }
    return primes;
}

int main() {
    int t;
    cin >> t;
    vector<int> inputs(t);
    int max_n = 0;
    
    for (int i = 0; i < t; i++) {
        cin >> inputs[i];
        if (inputs[i] > max_n) {
            max_n = inputs[i];
        }
    }
    
    vector<int> primes = prime_list(max_n);
    
    for (int i = 0; i < t; i++) {
        int n = inputs[i];
        long long tot = 0;
        for (int p : primes) {
            if (p > n) break;
            tot += p;
        }
        cout << tot << endl;
    }
    
    return 0;
}