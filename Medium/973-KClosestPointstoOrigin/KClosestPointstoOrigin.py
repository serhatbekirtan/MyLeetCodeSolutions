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


    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        res = []

        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            heap.append([dist, x, y])

        heapq.heapify(heap)

        for _ in range(k):
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])

        return res