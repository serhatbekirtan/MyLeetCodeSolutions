from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:

        def traverse(root, string, result):
            if not root:
                return

            if not root.left and not root.right:
                string += str(root.val)
                result.append(string)
                return
            
            string += f"{root.val}->"

            traverse(root.left, string, result)
            traverse(root.right, string, result)

        result = []
        traverse(root, "", result)

        return result