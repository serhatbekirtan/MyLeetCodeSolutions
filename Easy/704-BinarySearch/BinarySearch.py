from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        L = 0
        R = len(nums) - 1

        while L <= R:
            mid = (L + R) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                R = mid - 1

            if nums[mid] < target:
                L = mid + 1

        return -1