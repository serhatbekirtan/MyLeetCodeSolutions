from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hare = tortoise = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        ptr1 = nums[0]
        ptr2 = tortoise
        while True:
            if ptr1 == ptr2:
                return ptr1
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]

    
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise = hare = 0
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break

        tortoise2 = 0
        while True:
            tortoise = nums[tortoise]
            tortoise2 = nums[tortoise2]
            if tortoise == tortoise2:
                return tortoise