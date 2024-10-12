import heapq
from typing import List


class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = [(t[0], t[1], i) for i, t in enumerate(times)]
        times.sort()

        usedChairs = []
        availableChairs = [i for i in range(len(times))]

        for arrive, leave, i in times:
            while usedChairs and usedChairs[0][0] <= arrive:
                l, chair = heapq.heappop(usedChairs)
                heapq.heappush(availableChairs, chair)

            chair = heapq.heappop(availableChairs)
            heapq.heappush(usedChairs, (leave, chair))

            if i == targetFriend:
                return chair