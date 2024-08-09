from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root = TreeNode(val=preorder[0])
        partition = inorder.index(root.val)
        root.left = self.buildTree(preorder[1:partition + 1], inorder[:partition])
        root.right = self.buildTree(preorder[partition + 1:], inorder[partition + 1:])

        return root