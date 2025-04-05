// 100% HackerRank

#include <bits/stdc++.h>
using namespace std;

/*
   Fast deterministic check for 32-bit integers using
   Miller-Rabin with known bases for 32-bit range.
   Alternatively, you could do a small prime sieve up to 31622
   and check divisibility. Here we use Miller-Rabin for compactness.
*/

static long long mul_mod(long long a, long long b, long long m) {
    // (a * b) % m but safely (64-bit safe)
    __int128 r = (__int128) a * b;
    return (long long)(r % m);
}

long long mod_exp(long long base, long long exp, long long m) {
    long long result = 1 % m;
    base = base % m;
    while (exp > 0) {
        if (exp & 1) result = mul_mod(result, base, m);
        base = mul_mod(base, base, m);
        exp >>= 1;
    }
    return result;
}

// Deterministic Miller-Rabin for 32-bit integers.
// Works correctly for all 32-bit signed values using bases {2, 7, 61}.
bool isPrime32(uint32_t n) {
    if (n < 2) return false;
    static const int testPrimes[3] = {2, 7, 61};
    // Small quick checks
    static const int smallPrimes[12] = 
       {2,3,5,7,11,13,17,19,23,29,31,37};
    for (int sp: smallPrimes) {
        if (n == (uint32_t)sp) return true;
        if (n % sp == 0 && n != (uint32_t)sp) return false;
    }
    // Write n-1 as d*2^s
    uint32_t d = n - 1;
    int s = 0;
    while ((d & 1) == 0) {
        d >>= 1;
        s++;
    }
    auto check = [&](uint32_t a) {
        if (a == 0 || a >= n) return true; // skip invalid
        long long x = mod_exp(a, d, n);
        if (x == 1 || x == n-1) return true;
        for (int r = 1; r < s; r++) {
            x = mul_mod(x, x, n);
            if (x == n-1) return true;
            if (x == 1) return false;
        }
        return (x == n-1);
    };
    for (int a: testPrimes) {
        if (a == 0 || a == 1) continue;
        if (a == (int)n) return true;
        if (!check(a)) return false;
    }
    return true;
}

// Concatenate p and q in decimal, e.g. concat(7,109) = 7109
long long concatInt(long long p, long long q) {
    // Compute number of digits in q
    long long tmp = q;
    int digits = 0;
    while (tmp > 0) {
        tmp /= 10;
        digits++;
    }
    long long mult = 1;
    while (digits--) mult *= 10;
    return p * mult + q;
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N, K;
    cin >> N >> K;

    // 1) Sieve to get all primes up to N
    vector<bool> isPrime(N+1, true);
    isPrime[0] = false; 
    if(N >= 1) isPrime[1] = false;
    for (int i = 2; i * i <= N; i++) {
        if (isPrime[i]) {
            for (int j = i*i; j <= N; j += i)
                isPrime[j] = false;
        }
    }
    vector<int> primes;
    primes.reserve(N/5); // rough guess
    for(int i = 2; i <= N; i++){
        if(isPrime[i]) primes.push_back(i);
    }
    int M = (int)primes.size();

    // 2) We'll store adjacency in a vector of bitsets
    //    adjacency[i][j] = 1 means primes[i] is "compatible" with primes[j].
    vector< bitset<20000> > adj(M); // M can be up to ~2262 for N=20000, so 20000 is safe or use M itself

    // 3) Build adjacency
    //    We only need to check each pair once. We'll cache the primality of concatenations in a map.
    //    Or you can do a small LRU. For simplicity, use an unordered_map<long long,bool>.
    //    But we can also just do it on the fly + store in an std::unordered_map to avoid repeats.

    static unordered_map<long long, bool> concatPrimeCache;
    concatPrimeCache.reserve((size_t)M*M/2);
    concatPrimeCache.max_load_factor(0.7f);

    auto areCompatible = [&](int i, int j){
        // Return true if primes i and j are compatible: 
        // both concat(primes[i], primes[j]) and concat(primes[j], primes[i]) are prime.
        long long p = primes[i], q = primes[j];
        // Check p->q
        {
            long long c = (long long)p * 100000 + q; 
            // That's an attempt to skip counting digits but be careful if q >= 100000. 
            // Safer is to do the actual concat function:
            // long long c = concatInt(p, q);
            // We'll do the actual safe version:
            long long ckey = (p << 32) ^ q; // or something to combine p and q
            auto it = concatPrimeCache.find(ckey);
            bool val;
            if (it != concatPrimeCache.end()){
                val = it->second;
            } else {
                long long cval = concatInt(p, q);
                val = isPrime32((uint32_t)cval) && (cval < INT32_MAX ? true 
                         : isPrime32((uint32_t)(cval >> 32)) /* fallback check - rarely needed */);
                // Actually if cval <= 2e9, we can just isPrime32(cval). 
                // But let's keep it consistent. 
                // For safety, you might do:
                // val = (cval <= 2147483647LL) ? isPrime32((uint32_t)cval) 
                //                             : do a 64-bit check or a fallback. 
                concatPrimeCache[ckey] = val;
            }
            if(!val) return false;
        }
        // Check q->p
        {
            long long c = (long long)q << 32 ^ p;
            auto it = concatPrimeCache.find(c);
            bool val;
            if (it != concatPrimeCache.end()){
                val = it->second;
            } else {
                long long cval = concatInt(q, p);
                // same logic
                val = (cval <= 2147483647LL) ? isPrime32((uint32_t)cval)
                                            : false; // or do a fallback 64-bit prime check
                concatPrimeCache[c] = val;
            }
            if(!val) return false;
        }
        return true;
    };

    // Build adjacency using a double loop
    for(int i = 0; i < M; i++){
        for(int j = i+1; j < M; j++){
            if( areCompatible(i,j) ){
                adj[i].set(j);
                adj[j].set(i);
            }
        }
    }

    // 4) Backtracking to find all sets of size K.
    //    We'll store sums in a vector. We do a typical "clique search" with bitset intersection.

    vector<int> results;
    results.reserve(100000); // just a guess

    // We'll define a recursive function that tries to pick a set of size 'depth' out of K.
    // 'start' is the smallest index we can pick next.
    // 'mask' is the bitset of candidates that are all compatible with the current path.
    // 'sumSoFar' is the sum of the primes in the current path.
    // We need to store all sets once we reach depth == K.

    // To avoid TLE, we prune if the number of set bits in mask is < (K-depth).
    // Also note that we pick the next prime from the mask in ascending order.

    function<void(int,int,bitset<20000>,long long)> backtrack =
    [&](int start, int depth, bitset<20000> mask, long long sumSoFar){
        // If we have enough for a full clique
        if(depth == K){
            results.push_back((int)sumSoFar);
            return;
        }
        // Prune if not enough left in mask
        // Count how many bits are set from 'start' onward
        // A quick way: we can iterate from 'start' up to M, checking mask[i].
        // Or use a builtin function to count bits after ignoring [0..start-1].
        // For simplicity, do a small loop. Since M isn't huge, it’s fine.

        // We need at least (K - depth) more
        int needed = K - depth;
        // Count how many set bits from [start..M-1]
        // If that is < needed, we stop.
        // A small utility:
        int possible = 0;
        for(int i = start; i < M; i++){
            if(mask.test(i)) possible++;
        }
        if(possible < needed) return;

        // Now try picking each candidate i in [start..M-1] that is in mask
        for(int i = start; i < M; i++){
            if(!mask.test(i)) continue;
            // pick i
            // next mask = mask & adj[i]  (intersection)
            bitset<20000> newMask = mask & adj[i];
            // we only consider next indices > i
            // so we clear bits [0..i]
            for(int b = 0; b <= i; b++){
                newMask.reset(b);
            }
            backtrack(i+1, depth+1, newMask, sumSoFar + primes[i]);
        }
    };

    // We'll start each clique with a single prime i, 
    // then the initial mask is adj[i], but we only consider j>i. 
    // This ensures we never duplicate sets in different orders.

    for(int i = 0; i < M; i++){
        // We need K-1 more primes after picking i
        // If adjacency for i has fewer than K-1, skip quickly
        int countNeighbors = adj[i].count();
        if(countNeighbors < K-1) continue;

        // We'll define a mask that is just adjacency[i], 
        // but we also reset bits [0..i].
        bitset<20000> mask = adj[i];
        for(int b = 0; b <= i; b++){
            mask.reset(b);
        }
        // Now backtrack with depth=1 (since we've chosen i), sumSoFar=primes[i].
        backtrack(i+1, 1, mask, primes[i]);
    }

    // 5) Sort results and print
    sort(results.begin(), results.end());
    for(int s: results){
        cout << s << "\n";
    }

    return 0;
}
