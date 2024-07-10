from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None

        leftmost = self.invertTree(root.left)
        rightmost = self.invertTree(root.right)

        root.left = rightmost
        root.right = leftmost

        return root
    

    def invertTreeIterative(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

            temp = node.left
            node.left = node.right
            node.right = temp

        return root