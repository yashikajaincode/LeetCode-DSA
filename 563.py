class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.total_tilt = 0

        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            self.total_tilt += abs(left_sum - right_sum)
            return left_sum + right_sum + node.val

        dfs(root)
        return self.total_tilt
