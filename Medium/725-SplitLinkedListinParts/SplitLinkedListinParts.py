from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        curr, listLen, res = head, 0, []
        while curr:
            listLen += 1
            curr = curr.next

        mod = listLen % k if listLen > k else 0
        n = listLen // k

        for _ in range(k):
            res.append(head)
            
            for _ in range(n - (0 if mod else 1)):
                if head: head = head.next

            mod -= 1 if mod else 0
            
            if head:
                head.next, head = None, head.next

        return res