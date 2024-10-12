import heapq
from typing import List


class Solution:
    def minGroups(self, intervals: List[List[int]]) -> int:
        pq = []
        for left, right in sorted(intervals):
            if pq and pq[0] < left:
                heapq.heappop(pq)
            heapq.heappush(pq, right)
        return len(pq)