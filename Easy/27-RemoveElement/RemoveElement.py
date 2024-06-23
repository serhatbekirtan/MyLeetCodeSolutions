from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0

        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1

        return len(nums)
    

    def removeElement2(self, nums:List[int], val: int) -> int:
        i = 0

        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        
        return i