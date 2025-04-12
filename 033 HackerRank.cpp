// c++ version of the python code
// 83.33%

#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>
#include <sstream>
#include <iomanip>

using namespace std;

vector<char> insert(const vector<char>& array, int count, char target) {
    vector<char> in_new(count + array.size());
    for (int k = 0; k < count; ++k) {
        in_new[k] = target;
    }
    for (size_t k = count; k < in_new.size(); ++k) {
        in_new[k] = array[k - count];
    }
    return in_new;
}

bool nextPermutation(vector<char>& array) {
    return next_permutation(array.begin(), array.end());
}

string numToCharArray(int x, int digits) {
    stringstream ss;
    ss << setw(digits) << setfill('0') << x;
    return ss.str();
}

int merge(const string& strFill, const string& mask) {
    int index = 0;
    int result = 0;
    for (char m : mask) {
        result *= 10;
        if (m == '.') {
            result += strFill[index] - '0';
            index++;
        } else {
            result += m - '0';
        }
    }
    return result;
}

int main() {
    int n_input, k_input;
    cin >> n_input >> k_input;

    int n = n_input;
    int k = k_input;
    int keep = n - k;
    int tens[] = {1, 10, 100, 1000, 10000};
    int sumN = 0;
    int sumD = 0;
    set<int> used;

    for (int d = 1; d < tens[keep]; ++d) {
        for (int num = 1; num < d; ++num) {
            string charN_str = numToCharArray(num, keep);
            string charD_str = numToCharArray(d, keep);
            vector<char> charN(charN_str.begin(), charN_str.end());
            vector<char> charD(charD_str.begin(), charD_str.end());

            for (int i = tens[k - 1]; i < tens[k]; ++i) {
                string in_str = numToCharArray(i, k);
                vector<char> in(in_str.begin(), in_str.end());
                bool isAscending = true;
                for (size_t j = 1; j < in.size(); ++j) {
                    if (in[j - 1] > in[j]) {
                        isAscending = false;
                        break;
                    }
                }

                if (isAscending) {
                    vector<char> in_with_dots_vec = insert(in, keep, '.');
                    string in_with_dots(in_with_dots_vec.begin(), in_with_dots_vec.end());

                    vector<char> charInsertN_vec(in_with_dots.begin(), in_with_dots.end());
                    do {
                        string charInsertN_str(charInsertN_vec.begin(), charInsertN_vec.end());
                        int newN = merge(charN_str, charInsertN_str);
                        if (newN >= tens[n - 1]) {
                            vector<char> charInsertD_vec(in_with_dots.begin(), in_with_dots.end());
                            do {
                                string charInsertD_str(charInsertD_vec.begin(), charInsertD_vec.end());
                                int newD = merge(charD_str, charInsertD_str);
                                if (static_cast<long long>(newN) * d == static_cast<long long>(newD) * num) {
                                    int id = newN * 10000 + newD;
                                    if (used.find(id) == used.end()) {
                                        sumN += newN;
                                        sumD += newD;
                                        used.insert(id);
                                    }
                                }
                            } while (nextPermutation(charInsertD_vec));
                        }
                    } while (nextPermutation(charInsertN_vec));
                }
            }
        }
    }

    cout << sumN << " " << sumD << endl;

    return 0;
}
