from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        queue = []

        queue.append(p)
        queue.append(q)

        while queue:
            first = queue.pop(0)
            second = queue.pop(0)

            if not first and not second:
                continue

            elif not first or not second or first.val != second.val:
                return False
            
            queue.append(first.left)
            queue.append(second.left)
            queue.append(first.right)
            queue.append(second.right)

        return True
    

    def isSameTreeRecursive(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False        
            
        if p.val != q.val:
            return False
        
        return Solution.isSameTree(p.left, q.left) and Solution.isSameTree(p.right, q.right)