// 27.78%

#include <bits/stdc++.h>
using namespace std;
 
typedef long long ll;
 
ll isqrt128(__int128 n) {
    ll low = 0, high = 1;
    while((__int128) high * high < n)
        high *= 2;
    while(low < high) {
        ll mid = (low + high) / 2;
        __int128 midsq = (__int128) mid * mid;
        if(midsq < n)
            low = mid + 1;
        else
            high = mid;
    }
    return low;
}
 
bool isPerfectSquare128(__int128 n, ll &r) {
    if(n < 0) return false;
    r = isqrt128(n);
    return (__int128) r * r == n;
}
 
ll modInv(ll a, ll m) {
    ll m0 = m, x0 = 0, x1 = 1;
    if(m == 1)
        return 0;
    while(a > 1) {
        ll q = a / m;
        ll t = m;
        m = a % m;
        a = t;
        t = x0;
        x0 = x1 - q * x0;
        x1 = t;
    }
    if(x1 < 0)
        x1 += m0;
    return x1;
}
 
pair<ll,ll> combineCRT(ll a, ll m, ll b, ll n) {
    ll inv = modInv(m, n);
    ll k = ((b - a) % n + n) % n;
    k = (k * inv) % n;
    ll x = a + m * k;
    return { x % (m*n), m * n };
}
 
vector<pair<ll,ll>> factorize(ll n) {
    vector<pair<ll,ll>> factors;
    for(ll i = 2; i * i <= n; i++){
        if(n % i == 0){
            ll modVal = 1;
            while(n % i == 0){
                modVal *= i;
                n /= i;
            }
            factors.push_back({i, modVal});
        }
    }
    if(n > 1)
        factors.push_back({n, n});
    return factors;
}
 
void dfsCRT(int idx, ll current_mod, ll current_rem, const vector<pair<ll,ll>> &fac, vector<ll> &res) {
    if(idx == fac.size()){
        res.push_back(current_rem % current_mod);
        return;
    }
    ll mod_val = fac[idx].second; // p^k
    for (int option = 0; option < 2; option++) {
        ll r_new = option;  
        auto combined = combineCRT(current_rem, current_mod, r_new, mod_val);
        dfsCRT(idx+1, combined.second, combined.first, fac, res);
    }
}
 
vector<ll> getValidResidues(ll M) {
    if(M == 1) return {0};
    vector<pair<ll,ll>> factors = factorize(M);
    vector<ll> residues;
    dfsCRT(0, 1, 0, factors, residues);
    for(auto &r : residues)
        r %= M;
    sort(residues.begin(), residues.end());
    residues.erase(unique(residues.begin(), residues.end()), residues.end());
    return residues;
}
 
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
 
    int T;
    cin >> T;
    while(T--){
        ll P, Q, N;
        cin >> P >> Q >> N;
 
        if(P == 1 && Q == 2) {
            ll b = 1, t = 1;
            while(t <= N){
                ll new_b = 3 * b + 2 * t - 2;
                ll new_t = 4 * b + 3 * t - 3;
                b = new_b; 
                t = new_t;
            }
            cout << b << " " << t << "\n";
            continue;
        }
 
        ll d = gcd(P, Q);
        ll Pp = P / d, Qp = Q / d;
        ll M = Qp;   
 
        vector<ll> validRes = getValidResidues(M);
 
        priority_queue<pair<ll,ll>, vector<pair<ll,ll>>, greater<pair<ll,ll>>> pq;
        for(auto r : validRes){
            ll base = N + 1;
            ll rem = base % M;
            ll candidate;
            if(rem <= r)
                candidate = base + (r - rem);
            else
                candidate = base + (M - rem + r);
            pq.push({candidate, r});
        }
 
        bool found = false;
        ll best_b = 0, best_t = 0;
        const ll maxIterations = 10000000;
        ll iterations = 0;
        while(!pq.empty() && iterations < maxIterations){
            auto cur = pq.top();
            pq.pop();
            ll t = cur.first;
            ll r = cur.second;  
 
            __int128 T_val = t;
            __int128 product = (__int128)P * T_val * (T_val - 1);
            if(product % Q == 0){
                __int128 X = product / Q;  
                __int128 disc = 1 + 4 * X;
                ll s;
                if(isPerfectSquare128(disc, s)){
                    if((s + 1) % 2 == 0){
                        ll b = (s + 1) / 2;
                        if(b < t && b > 0){
                            best_b = b;
                            best_t = t;
                            found = true;
                            break;
                        }
                    }
                }
            }
            pq.push({t + M, r});
            iterations++;
        }
 
        if(found)
            cout << best_b << " " << best_t << "\n";
        else
            cout << "No solution" << "\n";
    }
    return 0;
}
