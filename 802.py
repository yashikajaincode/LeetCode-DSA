class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        n = len(graph)
        color = [0] * n  # 0 = unvisited, 1 = visiting, 2 = safe

        def dfs(node):
            if color[node] != 0:
                return color[node] == 2
            color[node] = 1  # Mark as visiting
            for nei in graph[node]:
                if not dfs(nei):
                    return False
            color[node] = 2  # Mark as safe
            return True

        return [i for i in range(n) if dfs(i)]
