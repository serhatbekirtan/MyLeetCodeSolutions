from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        res = 0
        totalSum = 0

        for i, num in enumerate(arr):
            totalSum += num
            if ((i * (i + 1)) // 2) == totalSum:
                res += 1

        return res