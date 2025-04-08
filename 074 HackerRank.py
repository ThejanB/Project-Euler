# 100%

from collections import defaultdict

factorial = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
chain_lengths = {}
length_to_numbers = defaultdict(list)

def get_next_in_chain(n):
    return sum(factorial[int(digit)] for digit in str(n))

def pre_comp_optimized(number_limit):
    global chain_lengths, length_to_numbers

    for i in range(number_limit + 1):
        if i in chain_lengths:
            continue

        chain = []
        current = i
        while current not in chain and current not in chain_lengths and len(chain) < 60:
            chain.append(current)
            current = get_next_in_chain(current)

        if current in chain:
            start_index = chain.index(current)
            cycle_length = len(chain) - start_index
            for j in range(start_index, len(chain)):
                num = chain[j]
                chain_lengths[num] = cycle_length
                length_to_numbers[cycle_length].append(num)

            length = len(chain) - start_index
            for j in range(start_index - 1, -1, -1):
                length += 1
                num = chain[j]
                chain_lengths[num] = length
                length_to_numbers[length].append(num)
        elif current in chain_lengths:
            length = len(chain) + chain_lengths[current]
            for j in range(len(chain)):
                num = chain[j]
                current_length = length - j
                chain_lengths[num] = current_length
                length_to_numbers[current_length].append(num)
        else:
            for index, num in enumerate(chain):
                current_length = len(chain) - index
                if num not in chain_lengths:
                    chain_lengths[num] = current_length
                    length_to_numbers[current_length].append(num)

    for length in length_to_numbers:
        length_to_numbers[length] = sorted(list(set(length_to_numbers[length])))


inputs = []
for _ in range(int(input())):
    number, limit = map(int, input().split())
    inputs.append((number, limit))

limit_pre_comp = max([i[0] for i in inputs])
pre_comp_optimized(limit_pre_comp)

for number, limit in inputs:
    found_numbers = [num for num in length_to_numbers[limit] if num <= number]
    if found_numbers:
        print(*found_numbers)
    else:
        print(-1)