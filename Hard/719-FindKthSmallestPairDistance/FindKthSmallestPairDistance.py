from typing import List


class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def countPairs(dist):
            left = 0
            count = 0

            for right in range(len(nums)):
                while nums[right] - nums[left] > dist:
                    left += 1
                count += right - left

            return count

        L, R = 0, max(nums)
        while L < R:
            mid = (L + R) // 2
            pairs = countPairs(mid)
            
            if pairs >= k:
                R = mid
            else:
                L = mid + 1

        return R