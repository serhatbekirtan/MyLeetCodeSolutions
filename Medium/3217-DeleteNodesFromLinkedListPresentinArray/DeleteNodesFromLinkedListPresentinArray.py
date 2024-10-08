from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        dummy.next = head
        curr = head
        prev = dummy

        while prev and prev.next:
            while curr and curr.val in nums:
                curr = curr.next
            prev.next = curr
            prev = curr
            if curr: curr = curr.next

        return dummy.next
    

    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        nums = set(nums)
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr.next:
            if curr.next.val in nums:
                curr.next = curr.next.next
            else:
                curr = curr.next
        
        return dummy.next