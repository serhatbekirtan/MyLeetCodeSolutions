from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_table = []
        
        while head:
            if hash_table.count(hash(head)) > 0:
                return True
            hash_table.append(hash(head))
            head = head.next
        
        return False
    

    def hasCycleConstantSpace(self, head: Optional(ListNode)) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            # Floyd's Tortoise & Hare
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                return True
        
        return False