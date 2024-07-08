from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = Counter(nums)

        for num in nums:
            if counts[num] > (len(nums)/2):
                return num

        
    def majorityElementConstantSpace(self, nums: List[int]) -> int:
        # Boyer-Moore Majority Voting Algorithm
        count = 0
        result = 0

        for num in nums:
            if num == result:
                result = num
                count += 1

            if num != result and (count - 1) < 0:
                result = num
                count += 1

            if num != result:
                count -= 1

        return result