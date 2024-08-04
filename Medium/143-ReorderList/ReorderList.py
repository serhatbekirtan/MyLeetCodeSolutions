from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        left = curr = head
        
        while curr:
            stack.append(curr)
            curr = curr.next

        while left and left.next:
            right = stack.pop()
            if right == left:
                right.next = None
                break
            
            temp = left.next
            left.next = right
            if temp != right:
                right.next = temp
            else:
                right.next = None
                break
            left = left.next.next

    
    # O(1) Space.
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        right = slow.next
        prev = slow.next = None

        while right:
            temp = right.next
            right.next = prev
            prev = right
            right = temp

        left, right = head, prev

        while right:
            temp_left, temp_right = left.next, right.next
            left.next, right.next = right, temp_left
            left, right = temp_left, temp_right