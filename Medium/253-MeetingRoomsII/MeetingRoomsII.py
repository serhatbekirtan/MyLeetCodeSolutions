from typing import List


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda interval: interval.end)
        res, visit = [], set()
        
        while len(visit) != len(intervals):
            i = 0
            curr = []

            while intervals[i] in visit:
                i += 1
            
            curr.append(intervals[i])
            visit.add(intervals[i])

            for j in range(i + 1, len(intervals)):
                if curr[-1].end <= intervals[j].start and intervals[j] not in visit:
                    curr.append(intervals[j])
                    visit.add(intervals[j])

            res.append(curr)
        
        return len(res)
    

    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        start = sorted([interval.start for interval in intervals])
        end = sorted([interval.end for interval in intervals])

        i, j, res, count = 0, 0, 0, 0
        
        while i < len(start):
            if start[i] < end[j]:
                i += 1
                count += 1
            else:
                j += 1
                count -= 1

            res = max(res, count)
        
        return res