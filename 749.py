class Solution:
    def containVirus(self, isInfected: List[List[int]]) -> int:
        m, n = len(isInfected), len(isInfected[0])
        total_walls = 0

        def neighbors(i, j):
            for x, y in ((i-1,j), (i+1,j), (i,j-1), (i,j+1)):
                if 0 <= x < m and 0 <= y < n:
                    yield x, y

        while True:
            regions = []
            frontiers = []
            walls_needed = []

            visited = [[False] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if isInfected[i][j] == 1 and not visited[i][j]:
                        region = []
                        frontier = set()
                        walls = 0
                        queue = [(i,j)]
                        visited[i][j] = True
                        while queue:
                            x, y = queue.pop()
                            region.append((x, y))
                            for nx, ny in neighbors(x, y):
                                if isInfected[nx][ny] == 0:
                                    frontier.add((nx, ny))
                                    walls += 1
                                elif isInfected[nx][ny] == 1 and not visited[nx][ny]:
                                    visited[nx][ny] = True
                                    queue.append((nx, ny))
                        regions.append(region)
                        frontiers.append(frontier)
                        walls_needed.append(walls)

            if not regions:
                break

            # Choose the most threatening region
            idx = frontiers.index(max(frontiers, key=len))
            total_walls += walls_needed[idx]

            # Quarantine the most threatening region
            for i, region in enumerate(regions):
                if i == idx:
                    for x, y in region:
                        isInfected[x][y] = -1  # quarantined
                else:
                    for x, y in frontiers[i]:
                        isInfected[x][y] = 1  # spread

        return total_walls
