from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sortedArr = sorted(set(arr))
        indexes = {}
        res = []
        
        for i, p in enumerate(sortedArr):
            indexes[p] = i + 1

        for num in arr:
            res.append(indexes[num])

        return res