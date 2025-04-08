// 100% in HackerRank

#include <iostream>
#include <vector>
#include <cmath>
#include <unordered_set>
#include <map>
using namespace std;

bool isPalindrome(long long x) {
    long long original = x, rev = 0;
    while(x > 0) {
        rev = rev * 10 + (x % 10);
        x /= 10;
    }
    return (rev == original);
}

vector<long long> findPalindromes(long long n, long long limit, long long gap) {
    vector<long long> result;
    long long sum = n * n;
    long long curr = n;
    while (true) {
        curr += gap;
        long long candidate = sum + curr * curr;
        if (candidate >= limit)
            break;
        sum = candidate;
        if (isPalindrome(candidate))
            result.push_back(candidate);
    }
    return result;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int T;
    cin >> T;
    
    map<pair<long long, long long>, long long> cache;
    
    while(T--){
        long long limit, gap;
        cin >> limit >> gap;
        pair<long long, long long> key = {limit, gap};
        
        if(cache.find(key) != cache.end()){
            cout << cache[key] << "\n";
            continue;
        }
        
        unordered_set<long long> palSet;
        long long bound = (long long)(sqrt(limit / 2.0) + 1e-9);
        for (long long i = 1; i <= bound; i++) {
            vector<long long> pals = findPalindromes(i, limit, gap);
            for(auto &val: pals)
                palSet.insert(val);
        }
        
        long long answer = 0;
        for(auto &val: palSet)
            answer += val;
        
        cout << answer << "\n";
        cache[key] = answer;
    }
    
    return 0;
}
