from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        minNum = nums[0]

        if nums[0] < nums[-1]:
            return nums[0]

        L, R = 0, len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] >= minNum:
                L = mid + 1
            else:
                minNum = nums[mid]
                R = mid - 1
        
        return minNum

    
    def findMin(self, nums: List[int]) -> int:
        L = 0
        R = len(nums) - 1

        while L < R:
            mid = (L + R) // 2

            if nums[mid] > nums[R]:
                L = mid + 1
            else:
                R = mid

        return nums[R]