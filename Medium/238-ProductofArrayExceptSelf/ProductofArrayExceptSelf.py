from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = suffix = [0] * n
        prefix[0] = suffix[-1] = 1
        result = []

        for i in range(n - 1):
            prefix[i + 1] = prefix[i] * nums[i]
            suffix[n - i - 2] = suffix[n - i - 1] * nums[n - i - 1]

        for i in range(n):
            result.append(prefix[i] * suffix[i])

        return result
    

    # Follow-up Solution. O(1) space.
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [1]
        total = 1

        for i in range(n - 1):
            result.append(result[i] * nums[i])

        for i in range(n - 1, 0, -1):
            total *= nums[i]
            result[i - 1] = result[i - 1] * total

        return result