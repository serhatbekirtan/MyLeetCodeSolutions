from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        res = []
        prefix = [0]
        violate = 0

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                violate += 1
            prefix.append(violate)

        for start, end in queries:
            if prefix[start] != prefix[end]:
                res.append(False)
            else:
                res.append(True)

        return res