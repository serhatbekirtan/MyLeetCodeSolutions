from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        self.shortest = float('inf')

        def recursive(node, depth):
            if not node:
                return

            if not node.left and not node.right:
                self.shortest = min(self.shortest, depth + 1)

            recursive(node.left, depth + 1)
            recursive(node.right, depth + 1)
        
        recursive(root, 0)
        return self.shortest
    

    def minDepthBFS(self, root: Optional[TreeNode]) -> int:
        # if root is None, return 0
        if not root:
            return 0
        
        # initialize queue with the root node
        queue = deque([root])
        
        # initialize level counter to 1
        level = 1
        
        while queue:
            
            # loop through the nodes at current level
            for i in range(len(queue)):
                
                # pop the node from the left of the queue
                node = queue.popleft()
                
                # if the node is a leaf node, return the current level
                if not node.left and not node.right:
                    return level
                
                # add the children of the current node to the queue
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # increment level counter for next level
            level += 1
            
        return level