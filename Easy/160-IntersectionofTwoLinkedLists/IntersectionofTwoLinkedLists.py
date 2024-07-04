from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodeA = headA
        nodeB = headB

        while nodeA != nodeB:
            if nodeA:
                nodeA = nodeA.next
            else:
                nodeA = headB
            
            if nodeB:
                nodeB = nodeB.next
            else:
                nodeB = headA

            # Simpler definition:
            # nodeA = nodeA.next if nodeA else headB
            # nodeB = nodeB.next if nodeB else headA
        
        return nodeA

    
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:

        def countNodes(node: ListNode, count: int):
            while node:
                count += 1
                node = node.next

            return count


        def moveNode(node: ListNode, count: int):
            while count > 0:
                node = node.next
                count -= 1
            
            return node


        nodeA = headA
        nodeB = headB
        countA = 0
        countB = 0

        countA = countNodes(node=nodeA, count=countA)
        countB = countNodes(node=nodeB, count=countB)

        commonCount = abs(countA - countB)
        nodeA = headA
        nodeB = headB
        
        if countA > countB:
            nodeA = moveNode(node=nodeA, count=commonCount)
            
        if countB > countA:
            nodeB = moveNode(node=nodeB, count=commonCount)
        
        while nodeA and nodeB:
            if nodeA == nodeB:
                return nodeA
            nodeA = nodeA.next
            nodeB = nodeB.next
        
        return None