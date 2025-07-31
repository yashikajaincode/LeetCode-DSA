class Solution:
    def hitBricks(self, grid: list[list[int]], hits: list[list[int]]) -> list[int]:
        m, n = len(grid), len(grid[0])
        
        # Mark bricks to be hit
        for x, y in hits:
            if grid[x][y] == 1:
                grid[x][y] = 2  # Mark to distinguish from original bricks

        # Union-Find structure
        parent = {}
        size = {}
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            xr, yr = find(x), find(y)
            if xr == yr:
                return
            if size[xr] < size[yr]:
                xr, yr = yr, xr
            parent[yr] = xr
            size[xr] += size[yr]
        
        def index(i, j):
            return i * n + j
        
        # Initialize Union-Find and connect top-row bricks to "roof"
        roof = m * n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    parent[index(i, j)] = index(i, j)
                    size[index(i, j)] = 1
        parent[roof] = roof
        size[roof] = 1
        
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == 1
        
        def connect(i, j):
            if i == 0:
                union(index(i, j), roof)
            for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
                ni, nj = i + dx, j + dy
                if is_valid(ni, nj):
                    union(index(i, j), index(ni, nj))
        
        # Rebuild stable structure after all hits
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    connect(i, j)

        res = []
        for x, y in reversed(hits):
            pre_roof = size[find(roof)]
            if grid[x][y] == 2:
                grid[x][y] = 1
                parent[index(x, y)] = index(x, y)
                size[index(x, y)] = 1
                connect(x, y)
                post_roof = size[find(roof)]
                fallen = max(0, post_roof - pre_roof - 1)
                res.append(fallen)
            else:
                res.append(0)

        return res[::-1]
