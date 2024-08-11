import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []

        for coordinate in points:
            x, y = coordinate
            distance = (x ** 2) + (y ** 2)
            heapq.heappush(res, [-distance, coordinate])
            if len(res) > k:
                heapq.heappop(res)

        return [coor[1] for coor in res]