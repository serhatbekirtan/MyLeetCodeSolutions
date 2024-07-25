from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        traverse = head
        numNodes = 0

        while traverse:
            traverse = traverse.next
            numNodes += 1

        if numNodes == 1:
            return None
        
        delete = numNodes - n
        count = 0
        current = head

        if delete == 0:
            return head.next

        while count + 1 < delete:
            current = current.next
            count += 1

        current.next = current.next.next

        return head
    

    # Follow up one-pass solution with two pointers.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        i = head
        iVal = 1
        j = head
        jVal = 1

        while i.next:
            if iVal > n:
                j = j.next

            i = i.next
            iVal += 1

        if iVal != 1:
            if iVal != n:
                j.next = j.next.next
            else:
                return head.next
        else:
            return None

        return head
    

    # Follow up cleaner.
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        left = dummy
        right = head

        while n > 0 and right:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next