from typing import List
from collections import deque

class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        if not forest or not forest[0]:
            return -1
        
        m, n = len(forest), len(forest[0])
        
        # Corrected line
        trees = sorted((forest[i][j], i, j) for i in range(m) for j in range(n) if forest[i][j] > 1)
        
        def bfs(sx: int, sy: int, tx: int, ty: int) -> int:
            if sx == tx and sy == ty:
                return 0
            visited = [[False] * n for _ in range(m)]
            queue = deque([(sx, sy, 0)])
            visited[sx][sy] = True
            while queue:
                x, y, d = queue.popleft()
                for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny] and forest[nx][ny] != 0:
                        if nx == tx and ny == ty:
                            return d + 1
                        visited[nx][ny] = True
                        queue.append((nx, ny, d + 1))
            return -1
        
        total_steps = 0
        cx, cy = 0, 0
        
        for _, tx, ty in trees:
            steps = bfs(cx, cy, tx, ty)
            if steps == -1:
                return -1
            total_steps += steps
            cx, cy = tx, ty
        
        return total_steps

# Example usage (for VS Code/local testing)
if __name__ == "__main__":
    solution = Solution()
    forest = [[1,2,3],[0,0,4],[7,6,5]]
    print(solution.cutOffTree(forest))  # Output: 6
