import heapq

class Solution:
    def swimInWater(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visited = [[False] * n for _ in range(n)]
        min_heap = [(grid[0][0], 0, 0)]  # (time, x, y)
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while min_heap:
            time, x, y = heapq.heappop(min_heap)
            if x == n - 1 and y == n - 1:
                return time
            if visited[x][y]:
                continue
            visited[x][y] = True
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                    heapq.heappush(min_heap, (max(time, grid[nx][ny]), nx, ny))
