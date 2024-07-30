import heapq
from typing import Counter, List


class Solution:
    # O(klogn)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        result = []

        for key in freq:
            heap.append((-freq[key], key))

        heapq.heapify(heap)

        for i in range(k):
            occur, num = heapq.heappop(heap)
            result.append(num)

        return result
    

    # O(n) with bucket sort idea.
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        bucket = [[]] * len(nums)
        result = []

        for key in freq:
            bucket[freq[key]].append(key)

        for i in range(1, len(bucket) - 1, -1):
            if bucket[i]:
                for num in bucket[i]:
                    result.append(num)
        
        return result