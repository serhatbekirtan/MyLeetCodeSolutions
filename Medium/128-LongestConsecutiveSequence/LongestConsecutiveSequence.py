from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1

        result = 1
        count = 1
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i - 1] == nums[i] - 1:
                count += 1
                result = max(result, count)
            elif nums[i - 1] == nums[i]:
                continue
            else:
                count = 1

        return result
    
    # O(n) Time, O(n) Space.
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = set(nums)
        result = 0

        for num in nums:
            if num - 1 not in nums:
                count = 1
                while (num + count) in nums:
                    count += 1
                    
                result = max(result, count)

        return result