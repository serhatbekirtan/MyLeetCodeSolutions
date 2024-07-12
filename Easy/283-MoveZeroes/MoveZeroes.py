from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        num_of_zeros = 0
        num_of_elements = len(nums)

        j = 0

        for i in range(num_of_elements):
            if nums[i]:
                nums[j] = nums[i]
                j += 1
            else:
                num_of_zeros += 1
        
        for i in range(num_of_elements - num_of_zeros, num_of_elements):
            nums[i] = 0

        
    def moveZeroes(self, nums: List[int]) -> None:
        j = 0

        for i in range(len(nums)):
            if nums[i]:
                nums[j], nums[i] = nums[i], nums[j]
                j += 1