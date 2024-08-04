from typing import List


class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        sums = []
        res = 0

        for i in range(len(nums)):
            total = 0
            for j in range(i, len(nums)):
                total += nums[j]
                sums.append(total)

        sums.sort()
        for k in range(left - 1, right):
            res += sums[k]

        return res % ((10**9) + 7)