from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []

        def recursive(root):
            if not root:
                return
            
            recursive(root.left)
            recursive(root.right)
            postorder.append(root.val)
        
        recursive(root)
        return postorder