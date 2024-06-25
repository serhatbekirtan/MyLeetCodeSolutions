from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # Left
        # Root
        # Right

        stack = []
        current = root
        result = []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left
            
            current = stack.pop()
            result.append(current.val)
            current = current.right

        return result
    

    def inorderTraversalRecursive(self, root: Optional[TreeNode], traversal: List[int]) -> List[int]:
        if root:
            traversal = Solution.inorderTraversalRecursive(self, root.left, traversal)
            traversal.append(root.val)
            traversal = Solution.inorderTraversalRecursive(self, root.right, traversal)
        
        return traversal