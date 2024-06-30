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
            if not root or not self.balanced:
                return 0
        
            depth_left = recursive(root.left)
            depth_right = recursive(root.right)

            if abs(depth_left - depth_right) > 1:
                self.balanced= False
            
            return 1 + max(depth_left, depth_right)
        
        recursive(root)
        return self.balanced
        