# 150% HackerRank

import heapq

N , K = map(int, input().split())

arr = []
index = 2
for i in range(N):
    row = list(map(int, input().split()))
    arr.append(row)
    index += (i + 1)

partial_sum = []
for i in range(N):
    row_psum = [0] * (i + 1)
    row_psum[0] = arr[i][0]
    for j in range(1, i + 1):
        row_psum[j] = row_psum[j - 1] + arr[i][j]
    partial_sum.append(row_psum)

heap = []

for r in range(N):
    for c in range(r + 1):
        current_sum = 0
        max_size = N - r
        for s in range(1, max_size + 1):
            row_idx = r + s - 1
            col_start = c
            col_end   = c + (s - 1)

            row_segment = partial_sum[row_idx][col_end]
            if col_start > 0:
                row_segment -= partial_sum[row_idx][col_start - 1]

            current_sum += row_segment

            if len(heap) < K:
                heapq.heappush(heap, -current_sum)  # store negative
            else:
                if -current_sum > heap[0]:
                    heapq.heapreplace(heap, -current_sum)

result = [-val for val in heap]
result.sort()

for val in result:
    print(val)

