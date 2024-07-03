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

    
    def postorderTraversalIterative(self, root: Optional[TreeNode]) -> List[int]:
        postorder = []
        stack1 = []
        stack2 = []

        current = root

        while current or stack1:
            while current:
                stack1.append(current)
                stack2.append(current)
                current = current.right
            
            current = stack1.pop()
            current = current.left
            
        while stack2:
            node = stack2.pop()
            postorder.append(node.val)

        return postorder