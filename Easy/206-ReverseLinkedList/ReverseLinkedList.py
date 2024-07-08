from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None

        stack = []

        while head:
            stack.append(head.val)
            head = head.next

        newHead = ListNode(stack.pop())
        dummy = newHead

        while stack:
            val = stack.pop()
            node = ListNode(val)
            newHead.next = node
            newHead = newHead.next

        return dummy
    

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        current = head
        
        while current:
            current_next = current.next
            current.next = prev
            prev = current
            current = current_next
        
        return prev