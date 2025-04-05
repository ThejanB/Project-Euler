#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <algorithm>
#include <set>

using namespace std;

vector<long> generatePolygonalNumbers(int s, long n_min, long n_max) {
    vector<long> numbers;
    for (long n = 1; ; ++n) {
        long num;
        if (s == 3) {
            num = n * (n + 1) / 2;
        } else if (s == 4) {
            num = n * n;
        } else if (s == 5) {
            num = n * (3 * n - 1) / 2;
        } else if (s == 6) {
            num = n * (2 * n - 1);
        } else if (s == 7) {
            num = n * (5 * n - 3) / 2;
        } else if (s == 8) {
            num = n * (3 * n - 2);
        } else {
            break;
        }
        if (num >= n_min && num <= n_max) {
            numbers.push_back(num);
        } else if (num > n_max) {
            break;
        }
    }
    return numbers;
}

void dfs(long current, long start, int remaining_types, const unordered_set<int>& types_used, const unordered_set<long>& numbers_used, const unordered_map<long, vector<pair<long, int>>>& graph, vector<long>& path, set<vector<long>>& result_sets) {
    if (remaining_types == 0) {
        long last_two = current % 100;
        long first_two_start = start / 100;
        if (last_two == first_two_start) {
            result_sets.insert(path);
        }
        return;
    }
    long last_two = current % 100;
    auto it = graph.find(last_two);
    if (it != graph.end()) {
        for (const auto& entry : it->second) {
            long next_num = entry.first;
            int type = entry.second;
            if (types_used.find(type) == types_used.end() && numbers_used.find(next_num) == numbers_used.end()) {
                unordered_set<int> new_types_used = types_used;
                new_types_used.insert(type);
                unordered_set<long> new_numbers_used = numbers_used;
                new_numbers_used.insert(next_num);
                path.push_back(next_num);
                dfs(next_num, start, remaining_types - 1, new_types_used, new_numbers_used, graph, path, result_sets);
                path.pop_back();
            }
        }
    }
}

set<long> solve(const vector<int>& polygonal_types) {
    int T = polygonal_types.size();
    if (T == 1) {
        vector<long> numbers = generatePolygonalNumbers(polygonal_types[0], 1000, 9999);
        set<long> sums;
        for (long num : numbers) {
            long last_two = num % 100;
            long first_two = num / 100;
            if (last_two == first_two) {
                sums.insert(num);
            }
        }
        return sums;
    }
    unordered_map<long, vector<pair<long, int>>> graph;
    unordered_map<int, vector<long>> numbers_by_type;
    for (int s : polygonal_types) {
        vector<long> numbers = generatePolygonalNumbers(s, 1000, 9999);
        numbers_by_type[s] = numbers;
        for (long num : numbers) {
            long first_two = num / 100;
            graph[first_two].emplace_back(num, s);
        }
    }
    set<vector<long>> result_sets;
    for (int s : polygonal_types) {
        for (long num : numbers_by_type[s]) {
            vector<long> path = {num};
            unordered_set<int> types_used = {s};
            unordered_set<long> numbers_used = {num};
            dfs(num, num, T - 1, types_used, numbers_used, graph, path, result_sets);
        }
    }
    set<long> sums;
    for (const auto& cycle : result_sets) {
        long sum = 0;
        for (long num : cycle) {
            sum += num;
        }
        sums.insert(sum);
    }
    return sums;
}

int main() {
    int T;
    cin >> T;
    vector<int> polygonal_types(T);
    for (int i = 0; i < T; ++i) {
        cin >> polygonal_types[i];
    }
    set<long> sums = solve(polygonal_types);
    for (long sum : sums) {
        cout << sum << endl;
    }
    return 0;
}