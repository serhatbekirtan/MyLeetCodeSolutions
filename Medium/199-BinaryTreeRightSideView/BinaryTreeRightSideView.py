from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue = deque()
        queue.append([root, 1])
        maxDepth = 1
        res = [root.val]

        while queue:
            node, depth = queue.popleft()
            if depth > maxDepth:
                res.append(node.val)
                maxDepth = depth

            if node.right: queue.append([node.right, depth + 1])
            if node.left: queue.append([node.left, depth + 1])

        return res
    

    # Alternate Solution.
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        queue = deque([root])

        while queue:
            rightMostNode = None
            queueLength = len(queue)

            for i in range(queueLength):
                node = queue.popleft()

                if node:
                    rightMostNode = node
                    queue.append(node.left)
                    queue.append(node.right)

            if rightMostNode:
                res.append(rightMostNode.val)

        return res