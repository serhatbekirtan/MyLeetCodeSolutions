from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy

        while head:
            if head.val == val:
                head = head.next
                continue

            prev.next = head
            prev = prev.next
            head = head.next

        prev.next = head

        return dummy.next