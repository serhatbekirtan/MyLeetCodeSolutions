from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not postorder:
            return None

        root = TreeNode(val=postorder[-1])
        partition = inorder.index(root.val)

        root.left = self.buildTree(inorder[:partition], postorder[:partition])
        root.right = self.buildTree(inorder[partition + 1:], postorder[partition:-1])

        return root
    

    # O(n) Time.
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        hashmap = {val: index for index, val in enumerate(inorder)}

        def build(left, right):
            if left > right:
                return None

            root = TreeNode(postorder.pop())
            partition = hashmap[root.val]

            root.right = build(partition + 1, right)
            root.left = build(left, partition - 1)

            return root

        return build(0, len(inorder) - 1)
    
