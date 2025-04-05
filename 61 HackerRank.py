import sys
from collections import defaultdict

def generate_polygonal_numbers(s, n_min, n_max):
    numbers = []
    n = 1
    while True:
        if s == 3:
            num = n * (n + 1) // 2
        elif s == 4:
            num = n * n
        elif s == 5:
            num = n * (3 * n - 1) // 2
        elif s == 6:
            num = n * (2 * n - 1)
        elif s == 7:
            num = n * (5 * n - 3) // 2
        elif s == 8:
            num = n * (3 * n - 2)
        else:
            break
        if num >= n_min and num <= n_max:
            numbers.append(num)
        elif num > n_max:
            break
        n += 1
    return numbers

def solve(polygonal_types):
    T = len(polygonal_types)
    if T == 1:
        numbers = generate_polygonal_numbers(polygonal_types[0], 1000, 9999)
        for num in numbers:
            last_two = num % 100
            first_two = num // 100
            if last_two == first_two:
                return [num]
        return []
    graph = defaultdict(list)
    numbers_by_type = defaultdict(list)
    for s in polygonal_types:
        numbers = generate_polygonal_numbers(s, 1000, 9999)
        numbers_by_type[s] = numbers
        for num in numbers:
            first_two = num // 100
            graph[first_two].append((num, s))
    result_sets = set()
    for s in polygonal_types:
        for num in numbers_by_type[s]:
            path = [num]
            types_used = {s}
            numbers_used = {num}
            stack = [(num, num, T - 1, types_used, numbers_used, path)]
            while stack:
                current, start, remaining, used_types, used_numbers, p = stack.pop()
                if remaining == 0:
                    last_two = current % 100
                    first_two_start = start // 100
                    if last_two == first_two_start:
                        result_sets.add(tuple(p))
                    continue
                last_two = current % 100
                if last_two in graph:
                    for (next_num, type_) in graph[last_two]:
                        if type_ not in used_types and next_num not in used_numbers:
                            new_used_types = used_types.copy()
                            new_used_types.add(type_)
                            new_used_numbers = used_numbers.copy()
                            new_used_numbers.add(next_num)
                            new_path = p.copy()
                            new_path.append(next_num)
                            stack.append((next_num, start, remaining - 1, new_used_types, new_used_numbers, new_path))
    sums = set()
    for cycle in result_sets:
        sums.add(sum(cycle))
    return sorted(sums)

T = int(input())
polygonal_types = list(map(int, input().split()))
sums = solve(polygonal_types)
for sum_ in sums:
    print(sum_)
