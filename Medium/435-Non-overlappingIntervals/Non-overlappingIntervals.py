from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda interval: interval[1])
        res, lastEnd = 0, intervals[0][1]
        
        for i in range(1, len(intervals)):
            if lastEnd > intervals[i][0]:
                res += 1
            else:
                lastEnd = intervals[i][1]

        return res