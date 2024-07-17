from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        self.flag = False
        self.result = False

        def traverseMain(root):
            if not root:
                return

            if root.val == subRoot.val:
                self.flag = True
                traverseSub(root, subRoot)
                if self.flag:
                    self.result = True
                    return

            traverseMain(root.left)
            traverseMain(root.right)

        def traverseSub(root, subRoot):
            if not root and not subRoot:
                return

            if root and subRoot and root.val == subRoot.val:
                traverseSub(root.left, subRoot.left)
                traverseSub(root.right, subRoot.right)
            else:
                self.flag = False

        traverseMain(root)
        return self.result
    

    # Neetcode solution.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.sameTree(root, subRoot):
            return True

        return (self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))
        

    def sameTree(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            return (self.sameTree(root.left, subRoot.left) and
                    self.sameTree(root.right, subRoot.right))
        
        return False
    

    # Cleaner version of my first solution.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(root, subRoot):
            if not root and not subRoot:
                return True

            if (root and not subRoot) or (subRoot and not root):
                return False

            if root.val != subRoot.val:
                return False

            return sameTree(root.left, subRoot.left) and sameTree(root.right, subRoot.right)

        if not root:
            return False

        if sameTree(root, subRoot):
            return True
        
        return (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot))