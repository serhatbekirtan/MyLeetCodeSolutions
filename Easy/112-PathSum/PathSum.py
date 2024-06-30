from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def recursive(root, sum):
            if not root:
                return False

            sum += root.val
            
            if not root.left and not root.right:
                return sum == targetSum

            return recursive(root.left, sum) or recursive(root.right, sum)

        return (recursive(root, 0))