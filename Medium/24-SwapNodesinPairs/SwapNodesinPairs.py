from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        
        dummy = ListNode()
        dummy.next = head
        current = head
        prev = dummy

        while current and current.next:
            
            temp = current.next

            current.next = temp.next
            temp.next = current
            prev.next = temp
            
            prev = current
            current = current.next

        return dummy.next