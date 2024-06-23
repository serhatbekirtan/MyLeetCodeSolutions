from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start < end:
            middle = (start + end) // 2
            if nums[middle] < target:
                start = middle + 1

            if nums[middle] > target:
                end = middle - 1

            if nums[middle] == target:
                return middle
            
        if start == end:
            if nums[start] > target:
                return start
            if nums[start] < target:
                return start + 1
            if nums[start] == target:
                return start
        
        if start > end:
            return start
        
        if end < start:
            return end
        

    def searchInsert2(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            middle = (start + end) // 2
            
            if nums[middle] == target:
                return middle
            
            if nums[middle] < target:
                start = middle + 1

            if nums[middle] > target:
                end = middle - 1
            
        return start