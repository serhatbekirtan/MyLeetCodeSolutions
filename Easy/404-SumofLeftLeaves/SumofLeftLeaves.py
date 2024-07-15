from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        result = 0
        current = root
        stack = []

        while current or stack:
            while current:
                stack.append(current)
                if current.left:
                    if not current.left.left and not current.left.right:
                        result += current.left.val
                current = current.left
            
            current = stack.pop()
            current = current.right

        return result
    

    def sumOfLeftLeavesRecursive(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        result = 0
        
        if root.left:
            if not root.left.left and not root.left.right:
                result += root.left.val
            else:
                result += self.sumOfLeftLeaves(root.left)
        
        result += self.sumOfLeftLeaves(root.right)
        
        return result