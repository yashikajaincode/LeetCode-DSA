from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = list(range(len(edges) + 1))

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        def union(x, y):
            rootX, rootY = find(x), find(y)
            if rootX == rootY:
                return False
            parent[rootY] = rootX
            return True

        for u, v in edges:
            if not union(u, v):
                return [u, v]

# Example usage (for VS Code/local testing)
if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantConnection([[1,2],[1,3],[2,3]]))          # Output: [2,3]
    print(sol.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))  # Output: [1,4]
