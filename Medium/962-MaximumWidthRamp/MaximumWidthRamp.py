from typing import List


class Solution:
    # Monotonic Stack.
    def maxWidthRamp(self, nums: List[int]) -> int:
        n = len(nums)
        stack = []
        
        for i in range(n):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)
        
        maxWidth = 0
        
        for j in range(n - 1, -1, -1):
            while stack and nums[stack[-1]] <= nums[j]:
                maxWidth = max(maxWidth, j - stack.pop())
        
        return maxWidth
    

    def maxWidthRamp(self, nums: List[int]) -> int:
        maxArray = [0] * len(nums)
        i = len(nums) - 1
        prevMax = 0

        for num in reversed(nums):
            maxArray[i] = max(num, prevMax)
            prevMax = maxArray[i]
            i -= 1
        
        res = 0
        L = 0
        for R in range(len(nums)):
            while nums[L] > maxArray[R]:
                L += 1
            res = max(res, R - L)

        return res