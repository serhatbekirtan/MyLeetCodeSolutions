from typing import List


class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = 0
        L = 0

        for R in range(len(nums)):
            while nums[R] - nums[L] > 2 * k:
                L += 1
            
            res = max(res, R - L + 1)
        
        return res