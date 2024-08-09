import heapq
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []

        def inorder(root):
            if not root:
                return

            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)
        return arr[k - 1]
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.res = root.val
        self.i = 0

        def inorder(root):
            if not root:
                return

            inorder(root.left)

            self.i += 1
            if k == self.i:
                self.res = root.val
                
            inorder(root.right)

        inorder(root)
        return self.res