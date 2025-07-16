from typing import List

class Solution:
    def findRedundantDirectedConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}
        candidate1 = candidate2 = None
        
        # Step 1: Check whether there is a node with two parents
        for u, v in edges:
            if v in parent:
                candidate1 = [parent[v], v]
                candidate2 = [u, v]
                break
            parent[v] = u

        def find(uf, x):
            while uf[x] != x:
                uf[x] = uf[uf[x]]
                x = uf[x]
            return x

        # Step 2: Union-Find to detect cycle
        def union_find(skip_edge):
            uf = list(range(len(edges) + 1))
            for u, v in edges:
                if [u, v] == skip_edge:
                    continue
                pu, pv = find(uf, u), find(uf, v)
                if pu == pv:
                    return [u, v]
                uf[pv] = pu
            return None

        # Case 1: A node has two parents
        if candidate1:
            # Try removing the second edge
            if not union_find(candidate2):
                return candidate2
            else:
                return candidate1
        # Case 2: No node has two parents, just a cycle
        else:
            return union_find(None)

# Example usage (for VS Code/local testing)
if __name__ == "__main__":
    sol = Solution()
    print(sol.findRedundantDirectedConnection([[1,2],[1,3],[2,3]]))           # Output: [2,3]
    print(sol.findRedundantDirectedConnection([[1,2],[2,3],[3,4],[4,1],[1,5]])) # Output: [4,1]
