from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, target, parents) -> List[TreeNode]:
            parents.append(root)
            if root.val == target:
                return parents
            elif root.val > target:
                return dfs(root.left, target, parents)
            else:
                return dfs(root.right, target, parents)

        lca_p = dfs(root, p.val, [])
        lca_q = dfs(root, q.val, [])

        res = root
        i = j = 0
        while i < len(lca_p) and j < len(lca_q) and lca_p[i].val == lca_q[j].val:
            res = lca_p[i]
            i += 1
            j += 1

        return res
    

    # Recursive Cleaner.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(root, p, q):
            if root.val > p.val and root.val > q.val:
                return dfs(root.left, p, q)
            elif root.val < p.val and root.val < q.val:
                return dfs(root.right, p, q)
            else:
                return root
        
        return dfs(root, p, q)
    
    # Iterative Cleaner.
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root

        while curr:
            if curr.val > p.val and curr.val > q.val:
                curr = curr.left
            elif curr.val < p.val and curr.val < q.val:
                curr = curr.right
            else:
                return curr