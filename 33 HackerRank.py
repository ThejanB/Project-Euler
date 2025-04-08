#  66.67% HackerRank
#  wrote same in C++ and then it got  83.33%
#  and then I wrote it in Go and it got 100%   -  (Go has very fast comilation)
#
#   Language	|    Compilation Time  |   Execution Time |       Notes
#   ---------------------------------------------------------------------------------
#   Python	    |    🚫 No compilation|   🐢 Slowest	 | Interpreted, great for quick prototyping, not for speed
#   C++	        |    🐌 Slow	      |   ⚡ Very Fast	| Powerful but long compile times, especially with templates
#   Go	        |    ⚡ Very Fast	 |   ⚡ Fast	       | One of Go’s biggest strengths — fast compiles and good performance

def insert(array, count, target):
    return [target] * count + array

def next_permutation(array):
    i = len(array) - 2
    while i >= 0 and array[i] >= array[i + 1]:
        i -= 1
    if i < 0:
        return False
    j = len(array) - 1
    while array[j] <= array[i]:
        j -= 1
    array[i], array[j] = array[j], array[i]
    array[i + 1:] = reversed(array[i + 1:])
    return True

def num_to_char_array(x, digits):
    result = str(x)
    while len(result) < digits:
        result = "0" + result
    return list(result)

def merge(str_fill, mask):
    index = 0
    result = 0
    for m in mask:
        result *= 10
        if m == '.':
            result += int(str_fill[index])
            index += 1
        else:
            result += int(m)
    return result

def solve():
    n_input, k_input = map(int, input().split())
    n = n_input
    k = k_input
    keep = n - k
    tens = [1, 10, 100, 1000, 10000]
    sum_n = 0
    sum_d = 0
    used = set()

    for d in range(1, tens[keep]):
        for num in range(1, d):
            char_n = num_to_char_array(num, keep)
            char_d = num_to_char_array(d, keep)
            for i in range(tens[k - 1], tens[k]):
                in_num = num_to_char_array(i, k)
                is_ascending = True
                for j in range(1, len(in_num)):
                    if in_num[j - 1] > in_num[j]:
                        is_ascending = False
                        break
                if is_ascending:
                    in_with_dots = insert(list(in_num), keep, '.')
                    char_insert_n = list(in_with_dots)
                    while True:
                        new_n = merge(char_n, char_insert_n)
                        if new_n >= tens[n - 1]:
                            char_insert_d = list(in_with_dots)
                            while True:
                                new_d = merge(char_d, char_insert_d)
                                if new_n * d == new_d * num:
                                    identifier = new_n * 10000 + new_d
                                    if identifier not in used:
                                        sum_n += new_n
                                        sum_d += new_d
                                        used.add(identifier)
                                if not next_permutation(char_insert_d):
                                    break
                        if not next_permutation(char_insert_n):
                            break

    print(f"{sum_n} {sum_d}")

if __name__ == "__main__":
    solve()