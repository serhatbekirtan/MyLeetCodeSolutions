from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res, i, n = [], 0, len(intervals)

        while i < n: 
            start, end = intervals[i][0], intervals[i][1]
            
            while i < n - 1 and end >= intervals[i + 1][0]:
                end = max(end, intervals[i + 1][1])
                i += 1

            res.append([start, end])
            i += 1

        return res if res else intervals

    
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = res[-1][1]
            
            if start <= lastEnd:
                res[-1][1] = max(end, lastEnd)
            else:
                res.append([start, end])
        
        return res