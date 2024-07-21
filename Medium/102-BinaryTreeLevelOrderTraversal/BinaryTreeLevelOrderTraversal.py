from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = []
        queue = deque()
        queue.append(root)
        result.append([root.val])

        while queue:
            arr = []
            valueArray = []

            while queue:
                node = queue.popleft()
                if node.left: 
                    arr.append(node.left)
                    valueArray.append(node.left.val)
                if node.right:
                    arr.append(node.right)
                    valueArray.append(node.right.val)

            for node in arr:
                queue.append(node)

            if arr: result.append(valueArray)

        return result
    

    def levelOrderLittleCleaner(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
            
        result = [[root.val]]
        queue = deque([root])
        arr = []

        while queue:
            node = queue.popleft()
            if node.left: arr.append(node.left)
            if node.right: arr.append(node.right)

            if not queue:
                for node in arr:
                    queue.append(node)

                if arr: 
                    result.append([node.val for node in arr])
                    arr = []

        return result