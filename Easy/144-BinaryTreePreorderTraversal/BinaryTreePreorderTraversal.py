from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []

        def recursive(root):
            if not root:
                return
            preorder.append(root.val)
            recursive(root.left)
            recursive(root.right)
        
        recursive(root)
        return preorder