from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        node = head
        arr = []

        while node:
            arr.append(node.val)
            node = node.next

        i = 0
        j = len(arr) - 1

        while i <= j:
            if arr[i] != arr[j]:
                return False
            
            i += 1
            j -= 1

        return True
    

    def isPalindromeConstantSpace(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Find Middle
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        current = slow
        prev = None

        # Reverse from middle to end
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp

        # Check as it is an array
        while head and prev:
            if head.val != prev.val:
                return False

            head = head.next
            prev = prev.next
        
        return True