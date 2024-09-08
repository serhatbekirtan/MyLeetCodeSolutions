from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        linked = []
        while head:
            linked.append(str(head.val))
            head = head.next

        path = []
        def traverse(node):
            if not node:
                return False
            
            path.append(str(node.val))
            if len(path) >= len(linked):
                if checkContains():
                    return True
            
            checkLeft = traverse(node.left)
            checkRight = traverse(node.right)
            path.pop()
            
            return checkLeft or checkRight
            
        def checkContains():
            nonlocal linked
            pathStr = "".join(path)
            linkedStr = "".join(linked)
            return linkedStr in pathStr
            
        return traverse(root)
    

    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if self.isSame(head, root):
            return True
        
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

    def isSame(self, listNode: Optional[ListNode], treeNode: Optional[TreeNode]) -> bool:
        if not listNode:
            return True

        if not treeNode or listNode.val != treeNode.val:
            return False
        
        return self.isSame(listNode.next, treeNode.left) or self.isSame(listNode.next, treeNode.right)