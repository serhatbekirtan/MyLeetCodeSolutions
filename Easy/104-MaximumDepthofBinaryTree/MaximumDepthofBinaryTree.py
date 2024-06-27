from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:        
        if not root:
            return 0
        
        if root.left or root.right:
            return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        
    
    def maxDepthBFS(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 0
        queue = deque([root])

        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            depth = depth + 1
        
        return depth
    

    def maxDepthDFS(self, root: Optional[TreeNode]) -> int:
        result = 0
        stack = [[root, 1]]

        while stack:
            node, depth = stack.pop()
            
            if node:
                result = max(result, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])

        return result
