from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        arr = []
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            arr.append(root.val)
            inorder(root.right)

        inorder(root)

        for i in range(1, len(arr)):
            if arr[i] <= arr[i - 1]:
                return False

        return True
    

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(root, left, right):
            if not root:
                return True
            
            if not (left < root.val < right):
                return False
            
            return validate(root.left, left, root.val) and validate(root.right, root.val, right)

        return validate(root, float('-inf'), float('inf'))