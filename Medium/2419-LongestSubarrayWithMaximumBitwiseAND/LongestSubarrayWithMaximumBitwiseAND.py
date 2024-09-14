from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        res, i = 1, 1
        maxAnd = max(nums)

        while i < len(nums):
            curr = 1
            if nums[i - 1] == maxAnd:
                while i < len(nums) and nums[i - 1] == nums[i]:
                    curr += 1
                    i += 1
            res = max(res, curr)
            i += 1

        return res
    

    def longestSubarray(self, nums: List[int]) -> int:
        maxAnd, size, res = max(nums), 0, 1

        for num in nums:
            if num == maxAnd:
                size += 1
            else:
                size = 0
            res = max(res, size)
        
        return res