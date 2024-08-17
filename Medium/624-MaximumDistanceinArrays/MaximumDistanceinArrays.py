from typing import List

class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        res = 0
        minSoFar, maxSoFar = arrays[0][0], arrays[0][-1]

        for i in range(1, len(arrays)):
            res = max(res, arrays[i][-1] - minSoFar, maxSoFar - arrays[i][0])
            minSoFar = min(minSoFar, arrays[i][0])
            maxSoFar = max(maxSoFar, arrays[i][-1])

        return res