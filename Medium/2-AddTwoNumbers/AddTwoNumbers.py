from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        curr = dummy

        while l1 and l2:
            total = l1.val + l2.val + carry
            newNodeVal = total % 10
            carry = total // 10

            newNode = ListNode(newNodeVal)
            curr.next = newNode
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        
        if l1:
            while l1:
                total = l1.val + carry
                newNodeVal = total % 10
                carry = total // 10

                newNode = ListNode(newNodeVal)
                curr.next = newNode
                curr = curr.next
                l1 = l1.next

        if l2:
            while l2:
                total = l2.val + carry
                newNodeVal = total % 10
                carry = total // 10

                newNode = ListNode(newNodeVal)
                curr.next = newNode
                curr = curr.next
                l2 = l2.next

        if carry:
            newNode = ListNode(carry)
            curr.next = newNode
            curr = curr.next
        
        return dummy.next
    

    # Cleaner.
    def addTwoNumbersClean(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        curr = dummy
        carry = 0

        while l1 or l2 or carry:

            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            total = l1_val + l2_val + carry
            newNodeVal = total % 10
            carry = total // 10
            
            curr.next = ListNode(newNodeVal)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next