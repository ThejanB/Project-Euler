import heapq

def min_path_sum(matrix):
    n = len(matrix)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    heap = [(matrix[0][0], 0, 0)]
    visited = [[float('inf')] * n for _ in range(n)]
    visited[0][0] = matrix[0][0]
    
    while heap:
        current_sum, x, y = heapq.heappop(heap)
        if x == n - 1 and y == n - 1:
            return current_sum
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                new_sum = current_sum + matrix[nx][ny]
                if new_sum < visited[nx][ny]:
                    visited[nx][ny] = new_sum
                    heapq.heappush(heap, (new_sum, nx, ny))
    return -1  # Should not reach here for valid inputs

n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]

print(min_path_sum(matrix))