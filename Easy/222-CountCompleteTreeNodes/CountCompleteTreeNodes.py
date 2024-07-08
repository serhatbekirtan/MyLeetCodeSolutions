from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
            
        queue = []
        queue.append(root)
        i = 0

        while root.left or root.right:
            if root.left: queue.append(root.left)
            if root.right: queue.append(root.right)
            i += 1
            root = queue[i]

        return len(queue)
    

    def countNodesRecursiveFaster(self, root: Optional[TreeNode]) -> int:
        
        def leftDepth(root: Optional[TreeNode]):
            depth = 0

            while root:
                root = root.left
                depth += 1

            return depth

        def rightDepth(root: Optional[TreeNode]):
            depth = 0

            while root:
                root = root.right
                depth += 1

            return depth

        left_depth = leftDepth(root)
        right_depth = rightDepth(root)

        if left_depth == right_depth:
            return (pow(2, left_depth) - 1)
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)