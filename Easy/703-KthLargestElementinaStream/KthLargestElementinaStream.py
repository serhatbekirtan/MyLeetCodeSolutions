import heapq
from typing import List


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # Sorting take 0(nlogn) time complexity.
        self.nums = sorted(nums)
        

    def add(self, val: int) -> int:
        # Binary search takes O(logn) time to find the place to insert.
        index = self.binSearch(val)

        # Insertion takes O(n) time, so whole operation is O(n) time complexity.
        self.nums.insert(index, val)

        return self.nums[len(self.nums) - self.k]


    def binSearch(self, val: int) -> int:
        L = 0
        R = len(self.nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if self.nums[mid] == val:
                return mid

            if self.nums[mid] > val:
                R = mid - 1
            
            if self.nums[mid] < val:
                L = mid + 1

        return L
    

# Solution using heap.
class KthLargest2:

    def __init__(self, k: int, nums: List[int]):
        self.k = k

        # Even though heapify takes 0(n) time complexity,
        heapq.heapify(nums)

        # Pop operation takes O(logn) time complexity, but since we do the pop operation (n - k) times, this also takes O(nlogn) time.
        while len(nums) > k:
            heapq.heappop(nums)
            
        self.nums = nums

    
    def add(self, val: int) -> int:
        # Push is O(logn) time complexity. Executed once.
        heapq.heappush(self.nums, val)

        # Pop is also O(logn) time complexity, also executed once. So whole operation take only O(logn) time complexity.
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
            
        return self.nums[0]