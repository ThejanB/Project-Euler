# 100% HackerRank

from collections import defaultdict, deque
import heapq

all_chars = set()
graph = defaultdict(set)
in_degree = defaultdict(int)

for _ in range(int(input())):
    attempt = input()
    if len(attempt) != 3:
        print("SMTH WRONG")
        break
    a, b, c = attempt[0], attempt[1], attempt[2]
    all_chars.update([a, b, c])

    # Add edge a -> b
    if b not in graph[a]:
        graph[a].add(b)
        in_degree[b] += 1

    # Add edge b -> c
    if c not in graph[b]:
        graph[b].add(c)
        in_degree[c] += 1

    # Ensure all characters are in in_degree
    in_degree.setdefault(a, 0)
    in_degree.setdefault(b, 0)
    in_degree.setdefault(c, 0)

# Prepare for topological sort using a min-heap for lex order
heap = []
for ch in all_chars:
    if in_degree[ch] == 0:
        heapq.heappush(heap, ch)

passcode = []
while heap:
    if len(heap) > 1:
        pass  # Multiple choices, pick lex smallest
    u = heapq.heappop(heap)
    passcode.append(u)

    for v in graph[u]:
        in_degree[v] -= 1
        if in_degree[v] == 0:
            heapq.heappush(heap, v)

if len(passcode) != len(all_chars):
    print("SMTH WRONG")
else:
    print(''.join(passcode))
