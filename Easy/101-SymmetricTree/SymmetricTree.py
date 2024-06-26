from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        queue = []
        
        p = root.left
        q = root.right

        queue.append(p)
        queue.append(q)

        while queue:
            p = queue.pop(0)
            q = queue.pop(0)

            if not p and not q:
                continue

            if not p or not q or p.val != q.val:
                return False

            queue.append(p.left)
            queue.append(q.right)
            queue.append(p.right)
            queue.append(q.left)

        return True