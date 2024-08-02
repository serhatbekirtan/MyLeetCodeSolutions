from typing import List


class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        numOfOnes = nums.count(1)
        L, R = 0, numOfOnes- 1
        ones = nums[L:R + 1].count(1)
        minSwap = numOfOnes - ones

        for L in range(1, len(nums)):
            left = nums[L - 1]
            R += 1

            if R == len(nums):
                R = 0
            if nums[R] == 0 and left == 1:
                ones -= 1
            elif nums[R] == 1 and left == 0:
                ones += 1
                
            minSwap = min(minSwap, numOfOnes - ones)
        
        return minSwap


    def minSwaps(self, nums: List[int]) -> int:
        n = len(nums)
        total_ones = nums.count(1)
        L = 0
        window_ones = max_window_ones = 0

        for R in range(2 * n):
            if nums[R % n]:
                window_ones += 1
            if R - L + 1 > total_ones:
                window_ones -= nums[L % n]
                L += 1
            max_window_ones = max(max_window_ones, window_ones)

        return total_ones - max_window_ones