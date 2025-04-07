from collections import defaultdict

queries = []
for _ in range(int(input())):
    queries.append(int(input()))

tile_limit = max(queries)

sum_counts = defaultdict(int)

seq1 = [i for i in range(8,tile_limit+1,8)]         # with 1 middle tile
seq2 = [i for i in range(12,tile_limit+1,8)]        # without a middle tile

def counter(seq):
    global tile_limit, sum_counts
    for i in range(len(seq)):
        current_sum = 0
        for j in range(i, len(seq)):
            current_sum += seq[j]
            if current_sum > tile_limit:
                break
            sum_counts[current_sum] += 1

counter(seq1)       # Count sums for sequence 1
counter(seq2)       # Count sums for sequence 2

# Precompute answers for all possible N
answer = [0] * (tile_limit + 1)
count = 0
for n in range(1, tile_limit + 1):
    if 1 <= sum_counts.get(n, 0) <= 10:
        count += 1
    answer[n] = count

for q in queries:
    print(answer[q])
print(answer)