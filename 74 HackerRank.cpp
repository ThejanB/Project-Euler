// 100% 

#include <bits/stdc++.h>
using namespace std;
  
vector<int> factorial = {1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880};
unordered_map<int, int> memo;
  
int getChainLen(int n) {
    if(memo.count(n)) return memo[n];
    vector<int> chain;
    unordered_map<int,int> pos;
    int cur = n;
    while (true) {
        if(memo.count(cur)) {
            int known = memo[cur];
            int total = chain.size() + known;
            for (int i = 0; i < (int)chain.size(); i++)
                memo[chain[i]] = total - i;
            return memo[n];
        }
        if(pos.count(cur)) {
            int cycleStart = pos[cur];
            int cycleLen = chain.size() - cycleStart;
            for(int i = cycleStart; i < (int)chain.size(); i++)
                memo[chain[i]] = cycleLen;
            for(int i = 0; i < cycleStart; i++)
                memo[chain[i]] = cycleLen + (cycleStart - i);
            return memo[n];
        }
        pos[cur] = chain.size();
        chain.push_back(cur);
        int next = 0, temp = cur;
        if(temp == 0)
            next = factorial[0];
        else {
            while(temp) {
                next += factorial[temp % 10];
                temp /= 10;
            }
        }
        cur = next;
        if(chain.size() > 60) break;
    }
    int total = chain.size();
    for (int i = 0; i < (int)chain.size(); i++)
        memo[chain[i]] = total - i;
    return memo[n];
}
  
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
  
    int T;
    cin >> T;
    vector<pair<int,int>> queries(T);
    int maxX = 0;
    for(int i = 0; i < T; i++){
         int a, b;
         cin >> a >> b;
         queries[i] = {a, b};
         maxX = max(maxX, a);
    }
    vector<int> chainLengths(maxX+1, 0);
    memo[0] = 2;
    chainLengths[0] = 2;
    for (int i = 1; i <= maxX; i++)
         chainLengths[i] = getChainLen(i);
  
    int maxChain = 100;
    vector<vector<int>> numbersByChain(maxChain+1);
    for (int i = 0; i <= maxX; i++){
         int cl = chainLengths[i];
         if(cl <= maxChain)
              numbersByChain[cl].push_back(i);
    }
  
    for(auto &q : queries){
         int X = q.first, L = q.second;
         if(L > maxChain || numbersByChain[L].empty()){
             cout << -1 << "\n";
             continue;
         }
         bool printed = false;
         for (int num : numbersByChain[L]){
             if(num > X) break;
             cout << num << " ";
             printed = true;
         }
         if(!printed) cout << -1;
         cout << "\n";
    }
    return 0;
}
