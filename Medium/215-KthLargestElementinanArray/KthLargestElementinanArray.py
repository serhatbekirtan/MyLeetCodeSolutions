import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)
        
        return heapq.heappop(nums)

    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap = []

        for num in nums:
            heapq.heappush(minHeap, num)
            if len(minHeap) > k:
                heapq.heappop(minHeap)

        return heapq.heappop(minHeap)


    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k

        def quickSelect(L, R):
            p = L
            for i in range(L, R):
                if nums[i] <= nums[R]:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            nums[p], nums[R] = nums[R], nums[p]

            if p > k: return quickSelect(L, p - 1)
            elif p < k: return quickSelect(p + 1, R)
            else: return nums[p]

        return quickSelect(0, len(nums) - 1)