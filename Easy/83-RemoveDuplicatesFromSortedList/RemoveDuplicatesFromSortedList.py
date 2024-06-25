# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while head.next:
            if head.val != head.next.val:
                tail.next = head
                tail = tail.next

            head = head.next

        tail.next = head

        return dummy.next
    

    def deleteDuplicates2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head

        while cur:
            while cur.next and cur.next.val == cur.val:
                    cur.next = cur.next.next
            cur = cur.next
        return head