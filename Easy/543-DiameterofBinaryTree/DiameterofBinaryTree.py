from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.total = 0

        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            self.total = max(self.total, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)

        return self.total