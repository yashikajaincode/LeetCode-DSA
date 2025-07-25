from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dp = [[[-1] * n for _ in range(n)] for _ in range(n)]
        dp[0][0][0] = grid[0][0]

        for x1 in range(n):
            for y1 in range(n):
                for x2 in range(n):
                    y2 = x1 + y1 - x2
                    if y2 < 0 or y2 >= n:
                        continue
                    if grid[x1][y1] == -1 or grid[x2][y2] == -1:
                        continue
                    val = grid[x1][y1]
                    if x1 != x2 or y1 != y2:
                        val += grid[x2][y2]
                    for dx1, dy1 in [(0, -1), (-1, 0)]:
                        for dx2, dy2 in [(0, -1), (-1, 0)]:
                            px1, py1 = x1 + dx1, y1 + dy1
                            px2, py2 = x2 + dx2, y2 + dy2
                            if 0 <= px1 < n and 0 <= py1 < n and 0 <= px2 < n and 0 <= py2 < n:
                                if dp[px1][py1][px2] != -1:
                                    dp[x1][y1][x2] = max(dp[x1][y1][x2], dp[px1][py1][px2] + val)
        return max(0, dp[n-1][n-1][n-1])
