import heapq
from typing import List


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        for i in range(len(stones)):
            stones[i] = (stones[i] * (-1))

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second_largest = heapq.heappop(stones)

            if largest < second_largest:
                largest -= second_largest
                heapq.heappush(stones, largest)

        return (-1 * stones[0]) if stones else 0