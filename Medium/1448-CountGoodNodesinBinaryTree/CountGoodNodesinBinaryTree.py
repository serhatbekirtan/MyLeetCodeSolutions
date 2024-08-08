class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0

        def dfs(root, pathMax):
            if not root:
                return
            
            if root.val >= pathMax:
                self.res += 1
                pathMax = root.val

            dfs(root.left, pathMax)
            dfs(root.right, pathMax)

        dfs(root, root.val)
        return self.res