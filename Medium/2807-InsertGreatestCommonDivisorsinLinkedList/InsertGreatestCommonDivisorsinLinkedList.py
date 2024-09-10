from typing import Optional
import math

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        def getGCD(val1, val2):
            gcd = 1
            for i in range(2, min(val1 + 1,val2 + 1)):
                if val1 % i == 0 and val2 % i == 0:
                    gcd = i
            return gcd

        while curr and curr.next:
            val1, val2 = curr.val, curr.next.val
            gcd = getGCD(val1, val2)
            curr.next = ListNode(gcd, curr.next)
            curr = curr.next.next

        return head
    

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        def getGCD(val1, val2):
            while val2 > 0:
                val1, val2 = val2, val1 % val2
            return val1

        while curr.next:
            val1, val2 = curr.val, curr.next.val
            curr.next = ListNode(getGCD(val1, val2), curr.next)
            curr = curr.next.next

        return head
    

    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            val1, val2 = curr.val, curr.next.val
            curr.next = ListNode(math.gcd(val1, val2), curr.next)
            curr = curr.next.next

        return head