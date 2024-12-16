import heapq
from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(n, i) for i, n in enumerate(nums)]
        heapq.heapify(heap)

        for _ in range(k):
            num, index = heapq.heappop(heap)
            heapq.heappush(heap, (num * multiplier, index))
            nums[index] = num * multiplier
        
        return nums