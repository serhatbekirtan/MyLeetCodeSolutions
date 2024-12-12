import heapq
from math import sqrt
from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-n for n in gifts]
        heapq.heapify(gifts)
        
        for i in range(k):
            chosen = heapq.heappop(gifts)
            heapq.heappush(gifts, -int(sqrt(-chosen)))
        
        return -sum(gifts)