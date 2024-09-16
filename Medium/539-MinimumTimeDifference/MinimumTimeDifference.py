from typing import List


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        def convertToMinutes(t):
            h, m = t.split(":")
            return (int(h) * 60) + int(m)

        timePoints.sort()
        res, n = 1440, len(timePoints)

        for i in range(n):
            curr, prev = convertToMinutes(timePoints[i]), convertToMinutes(timePoints[(i - 1) % n])
            res = min(res, (curr - prev) % 1440)

        return res