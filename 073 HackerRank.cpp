// 100%

#include <iostream>
#include <numeric>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>

std::map<long, std::vector<long>> prime_factors_cache;

std::vector<long> get_prime_factors(long num) {
    if (prime_factors_cache.count(num)) {
        return prime_factors_cache[num];
    }
    std::vector<long> factors;
    long temp_num = num;
    for (long i = 2; i * i <= temp_num; ++i) {
        if (temp_num % i == 0) {
            factors.push_back(i);
            while (temp_num % i == 0) {
                temp_num /= i;
            }
        }
    }
    if (temp_num > 1) {
        factors.push_back(temp_num);
    }
    std::sort(factors.begin(), factors.end());
    factors.erase(std::unique(factors.begin(), factors.end()), factors.end());
    prime_factors_cache[num] = factors;
    return factors;
}

long count_coprime(long l, long r, long num) {
    if (l > r) {
        return 0;
    }
    std::vector<long> prime_factors = get_prime_factors(num);
    long count = 0;
    long m = prime_factors.size();
    for (long i = 0; i < (1 << m); ++i) {
        long product = 1;
        long set_bits = 0;
        for (long j = 0; j < m; ++j) {
            if ((i >> j) & 1) {
                product *= prime_factors[j];
                set_bits++;
            }
        }
        long long term_count = (r / product) - ((l - 1) / product);
        if (set_bits % 2 == 0) {
            count += term_count;
        } else {
            count -= term_count;
        }
    }
    return count;
}

int main() {
    long a, dLimit;
    std::cin >> a >> dLimit;
    long total_count = 0;
    for (long d = 1; d <= dLimit; ++d) {
        long lowerN = d / (a + 1) + 1;
        long upperN = static_cast<long>(std::ceil(static_cast<double>(d) / a)) - 1;
        total_count += count_coprime(lowerN, upperN, d);
    }
    std::cout << total_count << std::endl;
    return 0;
}