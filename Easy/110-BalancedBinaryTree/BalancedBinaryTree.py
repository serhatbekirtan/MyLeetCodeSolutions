from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.balanced = True

        def recursive(root):
            if not root:
                return 0
        
            if root.left or root.right:
                depth_left = 1 + recursive(root.left)
                depth_right = 1 + recursive(root.right)

                if abs(depth_left - depth_right) > 1:
                    self.balanced= False
                
                return max(depth_left, depth_right)
        
        recursive(root)
        return self.balanced
        