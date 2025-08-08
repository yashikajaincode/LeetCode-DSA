class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ""
        
        left = self.tree2str(root.left)
        right = self.tree2str(root.right)
        
        if not root.left and root.right:
            return f"{root.val}()({right})"
        if not root.right:
            return f"{root.val}({left})" if root.left else f"{root.val}"
        
        return f"{root.val}({left})({right})"
