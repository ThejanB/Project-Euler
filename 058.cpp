#include <iostream>
using namespace std;

typedef long long ll;

// Modular exponentiation (a^d) % n
ll power(ll a, ll d, ll n) {
    ll result = 1;
    a = a % n;
    while (d > 0) {
        if (d & 1)
            result = (__int128)result * a % n;
        a = (__int128)a * a % n;
        d >>= 1;
    }
    return result;
}

// Miller-Rabin Primality Test (deterministic for n < 2^64)
bool is_prime(ll n) {
    if (n < 2) return false;
    if (n == 2 || n == 3) return true;
    if (n % 2 == 0) return false;

    ll d = n - 1;
    int r = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        r++;
    }

    // Witnesses for deterministic test up to 2^64
    int bases[] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37};
    for (int a : bases) {
        if (a >= n) break;
        ll x = power(a, d, n);
        if (x == 1 || x == n - 1) continue;

        bool witness = false;
        for (int i = 1; i < r; i++) {
            x = (__int128)x * x % n;
            if (x == n - 1) {
                witness = true;
                break;
            }
        }
        if (!witness) return false;
    }
    return true;
}

int main() {
    int limit;
    cin >> limit;   // 10  for project euler

    ll number = 1;
    int prime_count = 0;
    int total_diagonals = 1;
    int step = 2;

    while (true) {
        for (int i = 0; i < 4; ++i) {
            number += step;
            if (is_prime(number)) {
                prime_count++;
            }
        }
        total_diagonals += 4;

        if ((100.0 * prime_count / total_diagonals) < limit) {
            cout << (step + 1) << endl;
            break;
        }
        step += 2;
    }

    return 0;
}
