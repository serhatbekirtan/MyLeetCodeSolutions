from typing import Counter, List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        frequency = Counter(nums)

        for num in nums:
            if frequency[num] > 1:
                return True

        return False