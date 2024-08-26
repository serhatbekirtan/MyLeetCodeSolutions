from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        res = []
        
        def recursive(curr):
            if not curr:
                return

            for child in curr.children:
                recursive(child)
            
            res.append(curr.val)

        recursive(root)
        return res
    

    def postorder(self, root: 'Node') -> List[int]:
        res = []

        if not root:
            return res
        
        stack = [(root, False)]

        while stack:
            node, visited = stack.pop()
            if visited:
                res.append(node.val)
            else:
                stack.append(node, True)
                for child in reversed(node.children):
                    stack.append((child, False))

        return res