from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        level = 0

        while queue:
            if level % 2 == 1:
                L, R = 0, len(queue) -1

                while L < R:
                    queue[L].val, queue[R].val = queue[R].val, queue[L].val
                    L += 1
                    R -= 1
            
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                    queue.append(node.right)

            level += 1
        
        return root