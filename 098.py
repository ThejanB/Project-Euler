from collections import defaultdict

def match(a, b, squares):
    max_square = 0
    for i in squares:
        for j in squares:
            if i == j:
                continue
            replace_a = str(i)
            replace_b = str(j)
            if len(replace_a) != len(a) or len(replace_b) != len(b):
                continue
            replace_table = {}
            valid = True
            for k in range(len(replace_a)):
                original = replace_a[k]
                if original in replace_table and replace_table[original] != a[k]:
                    valid = False
                    break
                replace_table[original] = a[k]
            if not valid:
                continue
            if len(set(replace_table.values())) != len(replace_table):
                continue
            aa = ''.join([replace_table[c] for c in replace_a])
            if aa != a:
                continue
            bb = []
            for c in replace_b:
                if c in replace_table:
                    bb.append(replace_table[c])
                else:
                    valid = False
                    break
            if not valid:
                continue
            bb = ''.join(bb)
            if bb != b:
                continue
            if max_square < i:
                max_square = i
            if max_square < j:
                max_square = j
    return max_square


file = open('098 Project Euler.txt', 'r')
line = file.readline()         # there is only 1 line in the file
file.close()

words = line.split(',')
anagrams = defaultdict(list)
for word in words:  # remove the quotes from the words - [1:-1]
    sorted_word = ''.join(sorted(word[1:-1]))
    anagrams[sorted_word].append(word[1:-1])

max_digits = 0
for key in anagrams:
    if len(anagrams[key]) > 1:      # only consider anagrams with more than 1 word, there must be at least 1 pair  - skip for speedup
        if max_digits < len(anagrams[key][0]):
            max_digits = len(anagrams[key][0])


max_number = 10 ** max_digits
permutations = defaultdict(list)
fingerprint_length = defaultdict(set)
base = 1
while base * base <= max_number:
    square = base * base
    id = "".join(sorted(str(square)))
    permutations[id].append(square)
    num_digits = len(str(square))
    fingerprint_length[num_digits].add(id)
    base += 1

result = 0
for key in anagrams:
    pairs = anagrams[key]
    if len(pairs) < 2:      # only consider anagrams with more than 1 word - skip for speedup
        continue
    length = len(pairs[0])
    for i in range(len(pairs)):
        for j in range(i + 1, len(pairs)):
            for fid in fingerprint_length.get(length, []):
                current_max = match(pairs[i], pairs[j], permutations[fid])
                if result < current_max:
                    result = current_max
print(result)



